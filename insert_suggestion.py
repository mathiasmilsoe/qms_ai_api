import os
import json
import asyncio
import time
from create_assistant_with_files import (
    create_assistant_with_file_search,
    upload_files_and_add_to_vector_store,
    update_assistant_to_use_vector_store,
    create_thread,
    create_run_and_get_output,
)
from spinner import spinner_loader
from base_variables import base_instruction_suggestion, model, mdr_path, technical_file_directory
from base_variables import sted_path, traceability_matrix_path

def check_pdf_existence(pdf_path):
    if pdf_path.lower().endswith('.pdf'):
        if os.path.isfile(pdf_path):
            return True
        else:
            return False

async def process_suggestion(sub_requirement, requirement_category, requirement):
    tasks_list = sub_requirement.get('tasks_list', [])
    checked_documents = sub_requirement.get('checked_documents', [])

    if not tasks_list:
        return sub_requirement  # If there are no tasks, skip suggestion generation

    # Prepare the file paths for the checked documents
    file_paths = []
    for doc in checked_documents:
        file_path = os.path.join(technical_file_directory, doc['path'].lstrip("./"))
        if os.path.isfile(file_path) and check_pdf_existence(file_path):
            file_paths.append(file_path)

    assistant_name = f"suggestion_assistant_{requirement_category}_{requirement['requirement'].replace(' ', '_')}_{sub_requirement['description'].replace(' ', '_')}"
    assistant = await create_assistant_with_file_search(assistant_name, base_instruction_suggestion, model)
    vector_store_name = f"{assistant_name}_vector_store"
    new_vector_store = await upload_files_and_add_to_vector_store(vector_store_name, [mdr_path, sted_path, traceability_matrix_path] + file_paths)
    assistant = await update_assistant_to_use_vector_store(assistant, new_vector_store)

    for task in tasks_list:
        suggestion_instruction = f"""
        You are a seasoned consultant helping to create the best possible documentation for MDR compliance. Below is the sub-requirement with its description, and POTENTIAL non-conformities that the manufacturer has identified and wishes to mitigate in the documentation before submitting to a notified body. 
        For each possible non conformity, we have created a task that should be solved in order to avoid the notified body actually raising any non conformities. That mean, that if we can update and improve the documentation optimally, the notified body will not raise non conformities. 
        Your task is to write the concrete and specific suggestions for text that we can add to the documentation BEFORE submitting to the notified body, so that the documentation is on point and compliant with MDR before submitting. 

        Sub-requirement Description: {sub_requirement['description']}
        Non-conformities: {sub_requirement.get('non_conformities', [])}
        Compliance Grade: {sub_requirement.get('compliance_grade', '')}
        Detailed Explanation: {sub_requirement.get('detailed_compliance_explanation', '')}
        Assessment Criteria: {sub_requirement.get('assessment_criteria', '')}

        To write the suggestions, use compliant language and ensure the suggestion aligns with MDR requirements and remember, that these are not non conformities yet if we optimally adjust the technical documentation.
        Ideally, the manufacturer should be able to copy the suggestion directly into their documentation to make the document compliant. IMPORTANT, only give them the added and changed text, not the whole document. 
        When writing the suggestion it is critical that you take into the account that is provided in the various files in order to align the documentation with what the manufacturer has already written (e.g. intended purpose, risks, hazards, and so on). 

        Task Title: {task['title']}
        Task Description: {task['description']}
        Associated Documents: {task['associated_documents']}
        
        IMPORTANT: Mark any required user input as [[description]] for the manufacturer to fill in specific information.
        IMPORTANT: If it is not possible to provide a concrete text that the manufacturer can copy into their documentation, because the suggestion is a set of instructions 
        please just return "No text suggestion generated for this tasks, please follow the instructions outlined to mitigate the potential NC". Use you knowledge of the product and manufacturer to fill in as much information as possible. 
        IMPORTANT: Only return me a JSON object with the key 'suggestion' and then a string with the suggestion - nothing else. 

        """

        thread = await create_thread(suggestion_instruction)
        output = await create_run_and_get_output(thread, assistant, f"Suggestion for {task['title']}")
        output_json = output['json_content']

        # Log the output to see the response structure for debugging

        # Check if the 'suggestion' key exists
        if 'suggestion' in output_json:
            task['suggestion'] = output_json['suggestion']  # Fill the suggestion with the output text
        else:
            # Log the issue for debugging
            print(f"Warning: 'suggestion' key not found in output for task {task['title']}.")
            task['suggestion'] = "No text suggestion provided for this task"
        
    sub_requirement['tasks_list'] = tasks_list  # Update the sub_requirement with the new suggestions

    return sub_requirement


async def process_requirement_with_suggestion(requirement, requirement_category):
    # Process only the sub-requirements and their tasks
    tasks = [process_suggestion(sub_req, requirement_category, requirement) for sub_req in requirement['sub_requirements']]
    requirement['sub_requirements'] = await asyncio.gather(*tasks)

    return requirement


async def process_category_with_suggestions(category):
    start_time = time.time()

    loader_text = f"Inserting suggestions: {category}"
    stop_spinner_event, spinner_thread = spinner_loader(loader_text)

    try:
        output_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output"
        file_path = os.path.join(output_directory, f"{category}.json")
        
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return
        except json.JSONDecodeError:
            print(f"Invalid JSON format in file: {file_path}")
            return

        for requirement in data['requirements']:
            await process_requirement_with_suggestion(requirement, category)

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    finally:
        stop_spinner_event.set()
        spinner_thread.join()

        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time:.2f} seconds: {loader_text}")


async def insert_suggestions(selected_requirement_categories):
    for category in selected_requirement_categories: 
        await process_category_with_suggestions(category)
