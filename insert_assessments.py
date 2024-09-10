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
from base_variables import base_instruction, model, mdr_path, technical_file_directory

files_not_found = []
files_found = []

def check_pdf_existence(pdf_path):
    if pdf_path.lower().endswith('.pdf'):
        if os.path.isfile(pdf_path):
            files_found.append(pdf_path)
        else:
            files_not_found.append(pdf_path)

async def create_and_setup_assistant(sub_requirement, category, requirement, file_paths):

    assistant_name = f"{category}_{requirement['requirement'].replace(' ', '_')}_{sub_requirement['description'].replace(' ', '_')}_assistant"
    assistant = await create_assistant_with_file_search(assistant_name, base_instruction, model)
    vector_store_name = f"{assistant_name}_vector_store"
    new_vector_store = await upload_files_and_add_to_vector_store(vector_store_name, [mdr_path] + file_paths)
    assistant = await update_assistant_to_use_vector_store(assistant, new_vector_store)
    return assistant

async def process_sub_requirement(sub_requirement, requirement_category, requirement):   

    relevant_docs = sub_requirement.get('relevant_documents', [])
    file_paths = []

    for doc in relevant_docs:
        file_path = os.path.join(technical_file_directory, doc.lstrip("./"))
        check_pdf_existence(file_path)
        if file_path in files_found:
            file_paths.append(file_path)

    assistant = await create_and_setup_assistant(sub_requirement, requirement_category, requirement, file_paths)

    instruction = f"""
    Please inspect the documents listed below in order to asssess the documentation against the MDR subrequirement. Please fill in non-conformities, compliance_grade, and detailed_compliance_explanation in the object under the relevant documents. 
    Additionally, you need to add two new keys: 1) please add a checked_documents key which contains an array of strings with the documents that were checked (as objects containing path and short_name, where path is exactly how they appear in the relevant_documents array) 2) please add 
    a tasks_list which contains an array of objects with specific tasks needed to be completed for the manufacturer to be compliant with MDR. The objects in the array should contain title (string), description (string), associated_document which is an array of the documents (object with path and short_name) affected by the task, user_input which should be an empty string "", and lastly the task should contain a suggestion which should be a empty string "".

    Documents to be reviewed:
    {relevant_docs}

    Requirement to be reviewed: (IMPORTANT: pay close attention to the assessment criteria and only evaluate the documentation compliance status based on this)
    {sub_requirement}

    Instructions for Assessment:
    - Document Access and Validity Check: Before providing your assessment, confirm that each document is accessible and contains relevant information. If a document is not accessible or is empty, clearly state: "Document [document name] could not be accessed or is empty." Proceed with the assessment using only the documents that are accessible and valid.
    - Assessment Criteria: Use the assessment criteria listed above to grade the documentation package and divide into
        - C (Compliant)
        - PC (Partly Compliant)
        - NC (Non-Compliant)
        - NA (Not Applicable)
    - detailed_compliance_explanation: Provide a detailed explanation for each compliance grade. Use concrete examples and provide a clear rationale for your assessment.
    - non_conformities: Provide an array of objects containing title, description, and associated documents (path and short_name). Be careful to list specifically which documents you are referring to, why the non-conformities are important, relevant, and what the consequences can be if they are not mitigated.
    - Task List: For each requirement, include a task list that outlines specific actions needed to mitigate the non-conformities identified. Each task should include:
        - title: A brief title of the task. (string)
        - description: A detailed description of what needs to be done to address the non-conformities. (string)
        - associated_documents: An array of strings listing the documents where the tasks should be implemented. (array with strings)
        - user_input: empty string "". 
        - suggestion: empty string "".

    IMPORTANT: Only return the JSON object with strict formatting and nothing else.  
    """

    thread = await create_thread(instruction)
    output = await create_run_and_get_output(thread, assistant, f"Sub-requirement assessment for {sub_requirement['description']}")
    output_json = output['json_content']

    # Check if 'requirement' key exists and update output_json if it does
    if 'requirement' in output_json:
        output_json = output_json['requirement']

    # Update the sub_requirement with the output_json
    sub_requirement.update(output_json)

    return sub_requirement

async def process_requirement(requirement, requirement_category):
    tasks = [process_sub_requirement(sub_req, requirement_category, requirement) for sub_req in requirement['sub_requirements']]
    requirement['sub_requirements'] = await asyncio.gather(*tasks)
    
    mdr_document_paths = [mdr_path] 
    
    assistant_name = f"{requirement_category}_{requirement['requirement'].replace(' ', '_')}_assistant"
    assistant = await create_assistant_with_file_search(assistant_name, base_instruction, model)
    
    new_vector_store = await upload_files_and_add_to_vector_store(f"{assistant_name}_vector_store", mdr_document_paths)
    assistant = await update_assistant_to_use_vector_store(assistant, new_vector_store)
    
    instruction = f"""
    Based on the information provided below for each sub-requirement under the "{requirement['requirement']}" requirement, please determine the overall_compliance_grade for the main requirement and provide a detailed_compliance_explanation and a short_compliance_explanation that summarizes the findings across all sub-requirements. Strictly return the information as the object below.

    When giving the grade follow C for compliant, PC for partly compliant, and NC for non-compliant.

    IMPORTANT: Only return the JSON object with strict formatting and nothing else.

    Instructions for Assessment:
    - Document Access and Validity Check: Before providing your assessment, confirm that each document is accessible and contains relevant information. If a document is not accessible or is empty, clearly state: "Document [document name] could not be accessed or is empty." Proceed with the assessment using only the documents that are accessible and valid.
    - Assessment Criteria: Use the assessment criteria listed above to grade the documentation package and divide into
        - C (Compliant)
        - PC (Partly Compliant)
        - NC (Non-Compliant)
        - NA (Not Applicable)
    - detailed_compliance_explanation: Provide a detailed explanation for each compliance grade. Use concrete examples and provide a clear rationale for your assessment.
    - short_compliance_explanation: please provide a short explanation of the compliance grade. 

    {{
      "overall_compliance_grade": "",
      "detailed_compliance_explanation": "",
      "short_compliance_explanation: ""
    }}

    Sub-requirements:
    {requirement['sub_requirements']}
    """
    
    thread = await create_thread(instruction)
    output = await create_run_and_get_output(thread, assistant, f"Requirement assessment for {requirement['requirement']}")
    output_json = output['json_content']

    requirement.update(output_json)

    return requirement

async def process_category(category):
    start_time = time.time()

    loader_text = f"Inserting assessments: {category}"
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
            await process_requirement(requirement, category)

        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    finally:
        stop_spinner_event.set()
        spinner_thread.join()

        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time:.2f} seconds: {loader_text}")

async def insert_assessments(selected_requirement_categories):
    for category in selected_requirement_categories: 
        await process_category(category)
    # await asyncio.gather(*(process_category(category) for category in selected_requirement_categories))










