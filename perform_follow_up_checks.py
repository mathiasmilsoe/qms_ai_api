import json
import os
import asyncio
from spinner import spinner_loader  # Import the spinner_loader function from spinner.py
import time  # Import the time module
import time  # Import the time module
from insert_relevant_documents import insert_relevant_documents
from base_variables import base_instruction, model, mdr_path, technical_file_directory
from create_assistant_with_files import create_assistant_with_file_search, upload_files_and_add_to_vector_store, update_assistant_to_use_vector_store
from create_mdr_expert import create_mdr_expert
from create_document_based_structure import process_and_save_document_based_structure
from create_assistant_with_files import create_thread, create_run_and_get_output, add_message_to_thread
from spinner import spinner_loader  # Import the spinner_loader function
import asyncio  # Import asyncio for asynchronous programming


files_not_found = []
files_found = []

def check_pdf_existence(pdf_path):
    """Check if the PDF exists and is a valid PDF file."""
    if pdf_path.lower().endswith('.pdf'):
        if os.path.isfile(pdf_path):
            files_found.append(pdf_path)
        else:
            files_not_found.append(pdf_path)

async def get_updated_follow_up_check(file_path, check):
    json_content = check

    new_assistant = await create_assistant_with_file_search(f"follow_up_check_{check['document_name']}_assistant", "", model)
    new_vector_store = await upload_files_and_add_to_vector_store(f"follow_up_check_{check['document_name']}_vector_store", [file_path])
    new_assistant = await update_assistant_to_use_vector_store(new_assistant, new_vector_store)

    instruction = f"""
    Please fill in assessment and status (OK, PARTLY, NOT) in the object below based on {check['document_name']}
    {check}
    IMPORTANT! Your response should only be the updated object and nothing else
    """

    thread = await create_thread(f"{instruction}")

    #message = await add_message_to_thread(thread, instruction)
    output = await create_run_and_get_output(thread, new_assistant, instruction)

    try:
        # Check if the output message has the expected format
        if output and "message" in output and output["message"]:
            # Extract the JSON-like content
            json_string = output["message"]
            
            # Ensure it starts and ends correctly for JSON format
            if json_string.startswith("```json") and json_string.endswith("```"):
                json_string = json_string.strip("```json").strip("```").strip()
                
                # Attempt to load the JSON content
                json_content = json.loads(json_string)
            else:
                print(f"Output message does not contain valid JSON format.")
        else:
            print(f"No valid output message received or it is empty.:")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        json_content = {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        json_content = {}

    return json_content


async def perform_follow_up_check(check):
    # check['assessment'] = 'checked'
    print(f"####{check}")

    document_name = check['path'].lstrip("./")
    file_path = f"{technical_file_directory}/{document_name}"

    check_pdf_existence(file_path)

    updated_check = {}

    if file_path in files_found:
        updated_check = await get_updated_follow_up_check(file_path, check)


    return updated_check
    
async def update_follow_up_checks(requirement_name):

    # Start the timer
    start_time = time.time()

    # Define the file path based on the given requirement_name
    file_path = f"/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/document_based_structure/{requirement_name}_with_relevant_documents_document_based.json"

        # Start the spinner
    loader_text = f"updating follow_up_checks"
    stop_spinner_event, spinner_thread = spinner_loader(loader_text)

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return

        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Iterate over each document in the JSON object
        for doc, requirements in data.items():
            for requirement in requirements:
                # Explicitly update each required follow-up check
                updated_checks = []
                for check in requirement.get('required_follow_up_checks', []):
                    updated_check = await perform_follow_up_check(check)
                    updated_checks.append(updated_check)
                
                # Update the requirement with the new checks
                requirement['required_follow_up_checks'] = updated_checks

        # Write the updated JSON data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

        print(f"Updated follow-up checks in: {file_path}")
    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time:.2f} seconds: {loader_text} for {requirement_name}")  # Print a completion message with time taken
