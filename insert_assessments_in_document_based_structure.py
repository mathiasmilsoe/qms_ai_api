import os
import json
import shutil
import time  # Import the time module
from insert_relevant_documents import insert_relevant_documents
from base_variables import base_instruction, model, mdr_path, technical_file_directory
from create_assistant_with_files import create_assistant_with_file_search, upload_files_and_add_to_vector_store, update_assistant_to_use_vector_store
from create_mdr_expert import create_mdr_expert
from create_document_based_structure import process_and_save_document_based_structure
from create_assistant_with_files import create_thread, create_run_and_get_output, add_message_to_thread
from spinner import spinner_loader  # Import the spinner_loader function
import asyncio  # Import asyncio for asynchronous programming
from base_variables import list_of_files

files_not_found = []
files_found = []

def check_pdf_existence(pdf_path):
    """Check if the PDF exists and is a valid PDF file."""
    if pdf_path.lower().endswith('.pdf'):
        if os.path.isfile(pdf_path):
            files_found.append(pdf_path)
        else:
            files_not_found.append(pdf_path)

async def create_and_setup_assistant(document_name, file_path):
    """Create an assistant and set up a vector store with the specified file."""
    new_assistant = await create_assistant_with_file_search(f"{document_name}_assistant", base_instruction, model)
    new_vector_store = await upload_files_and_add_to_vector_store(f"{document_name}_vector_store", [mdr_path, file_path])
    new_assistant = await update_assistant_to_use_vector_store(new_assistant, new_vector_store)
    return new_assistant

async def process_document_object(document_object, document_name, assistant):
    """Process a document object, check its existence, and create a thread for assessment."""
    json_content = document_object  # Initialize with the given object as a default structure
    
    instruction = f"""Please use the object below to read through the {document_name} and add your assessment of the different 
    requirements to the following object {document_object}. For compliance grade use NC for non-compliant, PC for partly compliant,
     C for compliant and NA for not applicable. When writing the detailed compliance explanations, be highly careful to write elaborate 
     explanations that explain exactly why you have assessed it the way you have. Use concrete examples from the document, and where 
     necessary use concrete examples from the MDR. IMPORTANT your response should only include the updated object, and nothing else. 
     The object you return should have the following exact format and structure.
     NOTE: required_follow_up_checks is an array of documents that need to be checked as a consequence of what is stated in the document. 
     For example, if the document references external tests reports, validation, tests, or other documents which are stated as being important
     for the overall compliance of that document/requirement. Each item in the array should be an object like {{origin: string, description: string, assessment_instruction: string, document_name: string, path: string, assessment: ", status: "}}
     Where decription describes what we should expect to find, origin is where we found the reference, and document_name is the name of the document as it is referenced NB! if it is already mentioned in the relevant_documents, then it should not be considered again. 
     The assessment insctruction is a string that should be detailed enough that we can pass it to a person or AI to inspect whether the criteria is satisfied. 
     To fill in the path, you need to inspect the file list below and find the path to the relevant file. IMPORTANT, write it exactly as it appears in the list.
     Status and assessment are empty for now
     {list_of_files}
     IMPORTANT! We are testing the script, so please add a random object to required_follow_up_checks as specified above.
     """

    thread = await create_thread(f"{base_instruction}. {instruction}")

    #message = await add_message_to_thread(thread, instruction)
    output = await create_run_and_get_output(thread, assistant, f"insert document assessment {document_name}")

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

async def process_and_update_document_based_structure(requirement_name):
    """Process and update the document-based structure for a specific requirement."""
    # Start the timer
    start_time = time.time()

    # Start the spinner
    loader_text = f"Insert assessment in document based"
    stop_spinner_event, spinner_thread = spinner_loader(loader_text)

    try:
        # Define paths
        output_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/document_based_structure"
        original_output_file_path = os.path.join(output_directory, f"{requirement_name}_with_relevant_documents_document_based.json")
        backup_file_path = os.path.join(output_directory, f"{requirement_name}_with_relevant_documents_document_based_backup.json")

        # Create a backup copy of the original file
        shutil.copy2(original_output_file_path, backup_file_path)

        # Load the document-based structure from the original file
        try:
            with open(original_output_file_path, 'r') as json_file:
                document_based_structure = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        # List to hold all tasks for creating assistants and threads
        document_tasks = []

        # Loop over each document in the document-based structure
        for document_name, requirements in document_based_structure.items():
            document_name = document_name.lstrip("./")
            file_path = f"{technical_file_directory}/{document_name}"
            check_pdf_existence(file_path)

            if file_path in files_found:
                # Create a task for creating assistant and thread
                document_tasks.append(create_assistant_and_process_requirements(document_name, file_path, requirements, document_based_structure))
        
        # Run all document tasks concurrently
        await asyncio.gather(*document_tasks)

        # Overwrite the original file with the updated structure
        with open(original_output_file_path, 'w') as json_file:
            json.dump(document_based_structure, json_file, indent=4)
        
    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time:.2f} seconds: {loader_text} for: {requirement_name}")  # Print a completion message with time taken

async def create_assistant_and_process_requirements(document_name, file_path, requirements, document_based_structure):
    """Create an assistant, thread, and process requirements for a document."""
    # Create the assistant and thread asynchronously
    assistant = await create_and_setup_assistant(document_name, file_path)
    # instruction = f"We need to check {document_name} for compliance with various requirements. You will gradually receive the requirements, please follow the instructions to assess compliance with specified requirements"

    # List to hold all tasks for processing document objects
    requirement_tasks = []

    # Loop over each requirement in the document
    for i in range(len(requirements)):
        document_object = requirements[i]
        # Create a task for processing the document object
        requirement_tasks.append(process_document_object(document_object, document_name, assistant))
    
    # Run all requirement tasks concurrently
    updated_requirements = await asyncio.gather(*requirement_tasks)

    # Update the requirements in the document-based structure
    for i, updated_document_object in enumerate(updated_requirements):
        requirements[i] = updated_document_object

# import os
# import json
# import shutil
# import time  # Import the time module
# from insert_relevant_documents import insert_relevant_documents
# from base_variables import base_instruction, model, mdr_path, technical_file_directory
# from create_assistant_with_files import create_assistant_with_file_search, upload_files_and_add_to_vector_store, update_assistant_to_use_vector_store
# from create_mdr_expert import create_mdr_expert
# from create_document_based_structure import process_and_save_document_based_structure
# from create_assistant_with_files import create_thread, create_run_and_get_output, add_message_to_thread
# from spinner import spinner_loader  # Import the spinner_loader function

# files_not_found = []
# files_found = []

# def check_pdf_existence(pdf_path):
#     """Check if the PDF exists and is a valid PDF file."""
#     if pdf_path.lower().endswith('.pdf'):
#         if os.path.isfile(pdf_path):
#             files_found.append(pdf_path)
#         else:
#             files_not_found.append(pdf_path)

# def create_and_setup_assistant(document_name, file_path):
#     """Create an assistant and set up a vector store with the specified file."""
#     new_assistant = create_assistant_with_file_search(f"{document_name}_assistant", base_instruction, model)
#     new_vector_store = upload_files_and_add_to_vector_store(f"{document_name}_vector_store", [mdr_path, file_path])
#     new_assistant = update_assistant_to_use_vector_store(new_assistant, new_vector_store)
#     return new_assistant

# def process_document_object(document_object, document_name, file_path, assistant, thread):
#     """Process a document object, check its existence, and create a thread for assessment."""
#     json_content = document_object  # Or some default structure if needed

#     instruction = f"Please use the object below to read through the {document_name} and add your assessment of the different requirements to the following object {document_object}. For compliance grade use NC for non-compliant, PC for partly compliant, C for compliant and NA for not applicable. When writing the detailed compliance explanations, be highly careful to write elaborate explanations that explain exactly why you have assessed it the way you have. Use concrete examples from the document, and where necessary use concrete examples from the MDR. IMPORTANT your response should only include the updated object, and nothing else. The object you return should have the following exact format and structure"

#     message = add_message_to_thread(thread, instruction)
#     output = create_run_and_get_output(thread, assistant)

#     try:
#         json_string = output["message"].strip("```json").strip("```").strip()
#         json_content = json.loads(json_string)  # Parse the JSON string into a dictionary
#     except json.JSONDecodeError as e:
#         print(f"Failed to decode JSON: {e}")
#         json_content = {}

#     return json_content

# def process_and_update_document_based_structure(requirement_name):
#     """Process and update the document-based structure for a specific requirement."""
#     # Start the timer
#     start_time = time.time()

#     # Start the spinner
#     loader_text = f"Insert assessment in document based: {requirement_name}"
#     stop_spinner_event, spinner_thread = spinner_loader(loader_text)

#     try:
#         # Define paths
#         output_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/document_based_structure"
#         original_output_file_path = os.path.join(output_directory, f"{requirement_name}_with_relevant_documents_document_based.json")
#         backup_file_path = os.path.join(output_directory, f"{requirement_name}_with_relevant_documents_document_based_backup.json")

#         # Create a backup copy of the original file
#         shutil.copy2(original_output_file_path, backup_file_path)

#         # Load the document-based structure from the original file
#         try:
#             with open(original_output_file_path, 'r') as json_file:
#                 document_based_structure = json.load(json_file)
#         except FileNotFoundError:
#             return
#         except json.JSONDecodeError:
#             return

#         # Loop over each document in the document-based structure
#         for document_name, requirements in document_based_structure.items():
#             document_name = document_name.lstrip("./")
#             file_path = f"{technical_file_directory}/{document_name}"
#             check_pdf_existence(file_path)

#             assistant = create_and_setup_assistant(document_name, file_path) #+MDR!
#             instruction = f"We need to check {document_name} for compliance with various requirements. You will gradually receive the requirements, please follow the instructions to assess compliance with specified requirements"
#             thread = create_thread(f"{base_instruction}. {instruction}")
           
#             if file_path in files_found:
#                 # Loop over each requirement in the document
#                 for i in range(len(requirements)):
#                     document_object = requirements[i]
#                     updated_document_object = process_document_object(document_object, document_name, file_path, assistant, thread)
#                     requirements[i] = updated_document_object

#             # Overwrite the original file with the updated structure
#             with open(original_output_file_path, 'w') as json_file:
#                 json.dump(document_based_structure, json_file, indent=4)
        
#     finally:
#         # Stop the spinner after the task is completed
#         stop_spinner_event.set()
#         spinner_thread.join()

#         # Calculate the elapsed time
#         elapsed_time = time.time() - start_time
#         print(f"Completed in {elapsed_time:.2f} seconds: {loader_text}")  # Print a completion message with time taken
