import json
import os
import time  # Import the time module for measuring execution time
from base_variables import base_instruction, product_name, compliance_criteria
from create_assistant_with_files import create_thread, create_run_and_get_output, add_message_to_thread
from spinner import spinner_loader  # Import the spinner_loader function
import asyncio

# Consolidate individual document assessments into one
async def update_req_object_with_consolidated_assessment(requirement, mdr_expert):
    # Instruction for consolidation
    instruction = f"""We have used a set of relevant documents to make assessments of various requirements for product {product_name}.
    Below you will find an object, which contains assessments for a given requirement from various relevant documents, 
    and now we need to consolidate these assessments into a single aggregated assessment for the level of which the specific requirement is compliant with the MDR.

    The information you need from the assessment of individual docs is in this object: {requirement}

    overall_compliance_grade: {compliance_criteria}. IMPORTANT: The overall documentation is compliant if multiple documents in combination satisfy the requirement or if one document is fully compliant.
    datiled_compliance_explanation: Create an extremely detailed explanation of the compliance grade leaving out no details. Which documents were checked, what were the short comings of each, how does this sum up to an overall assessment. What is the impact of the grade, ie. what consequences can it have if the requirement is not compliant. If relevant, provide clear suggestions on improvements. 
    overall_sub_req_compliance_grade: create an aggregated compliance grad for the sub requirement based on the grade from the various documents. If one is fully compliant, then the documentation as a whole is compliant with that requirement. If the documents have different shortcomings, but together cover everything, the documentation as a whole is fully compliant.
    non_conformities: based on the assessment of sub requirements, overall assessments and identification of gaps and shortcomings, create an array of strings with detailed explanations of each non-conformities that were identified. The description should be highly detailed, rooted in you knowledge about MDR with concrete reference. Use extensive and elaborate examples from the documentation to argue why the non conformity is identified. 
    overall_sub_req_compliance_grade: the combined compliance for the sub requirement. IMPORTANT: The overall documentation is compliant if multiple documents in combination satisfy the requirement or if one document is fully compliant.
    task_list: a list of actionable task that the manufacturer can perform to ensure compliance. Should be an array with object in the following form {{title: string, short_description: string, user_input: "", }}
    required_follow_up_checks: Use the existing list to make a consolidated list where e.g. each document is only mentioned once, and if the original had multiple mentions of a document, consolidate into one object.
    IMPORTANT! Your response should solely consist of a json object with the relevant information filled in, and nothing else. The json object must have the exact structure outline below
    {{
        "requirement": string, #identical to the input
        "reference": string, #identical to the input,
        "description": string, #identical to the input,
        "checked_documents": array, #identifical to input
        "individual_document_grades": dictionary, #identical to input overall_compliance_grade 
        "individual_document_grades_explanations": dictionary, #use the explanations of sub requirements to generate a compliance explanation for each document
        "overall_compliance_grade": string, #you need to make the assessment according to the instructions above
        "datiled_compliance_explanation": string, #You should generate this in accordance with the instructions above
        "non_conformities": array, #array of strings that you need to generate in accordance with the insctructions above
        "task_list": array, #you should generate this in accordance with instructions above
        "required_follow_up_checks": #Create a consolidated list in accordance with instructions above
        "sub_requirements": [
            {{
                "description": string, #identifical to input
                "individual_document_grades": dictionary, #identifical to what was before compliance_grade for that subrequirement
                "overall_sub_req_compliance_grade": string, #you should generate this in accordance with instructions above
                "detailed_compliance_explanation": string, #you should generate this in accordance with instructions above
                "detailed_compliance_explanation_individual_docs": dictionary, #identical to detailed_compliance_explanation from orignal object
                "non_conformities": array, #array of strings that you need to generate in accordance with the insctructions above
                "assessment_criteria": string, #identical to input
            }},
        ]
    }}
    """
    thread = await create_thread(f"{base_instruction}. {instruction}")

    # await add_message_to_thread(thread, instruction)

    # Get output from the assistant
    output = await create_run_and_get_output(thread, mdr_expert, f"consolidate requirements")

    # Extract and clean the JSON content from the output
    try:
        json_string = output["message"].strip("```json").strip("```").strip()
        json_content = json.loads(json_string)  # Parse the JSON string into a dictionary
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        json_content = {}

    return json_content

async def consolidate_requirements(requirement_name, mdr_expert):
    # Start the timer
    start_time = time.time()

    # Start the spinner for consolidating requirements
    stop_spinner_event, spinner_thread = spinner_loader(f"Consolidating requirements")

    try:
        # Define file paths based on the requirement name
        input_path = f"/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/for_consolidation/{requirement_name}_document_asssesments_for_consolidation.json"
        output_path = f"/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/consolidated/{requirement_name}_consolidated.json"
        
        # Read the requirement-based JSON file
        with open(input_path, 'r') as file:
            requirement_based = json.load(file)
        
        # Initialize a dictionary to store the consolidated data
        consolidated = {"requirements": []}

        # List to hold all tasks for processing requirements
        requirement_tasks = []

        # Iterate over each requirement in the requirement-based data
        for requirement in requirement_based["requirements"]:
            # Create a task for processing each requirement
            task = update_req_object_with_consolidated_assessment(requirement, mdr_expert)
            requirement_tasks.append(task)

        # Run all requirement tasks concurrently
        updated_requirements = await asyncio.gather(*requirement_tasks)

        # Add all updated requirements to the consolidated list
        consolidated["requirements"].extend(updated_requirements)

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write the consolidated JSON file
        with open(output_path, 'w') as outfile:
            json.dump(consolidated, outfile, indent=4)

    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Finished in {elapsed_time:.2f} seconds: Consolidating requirement {requirement_name}.")  # Print the completion message with the time taken

