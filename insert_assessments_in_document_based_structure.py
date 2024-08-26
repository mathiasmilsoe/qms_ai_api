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

files_not_found = []
files_found = []

def check_pdf_existence(pdf_path):
    """Check if the PDF exists and is a valid PDF file."""
    if pdf_path.lower().endswith('.pdf'):
        if os.path.isfile(pdf_path):
            files_found.append(pdf_path)
        else:
            files_not_found.append(pdf_path)

def create_and_setup_assistant(document_name, file_path):
    """Create an assistant and set up a vector store with the specified file."""
    new_assistant = create_assistant_with_file_search(f"{document_name}_assistant", base_instruction, model)
    new_vector_store = upload_files_and_add_to_vector_store(f"{document_name}_vector_store", [mdr_path, file_path])
    new_assistant = update_assistant_to_use_vector_store(new_assistant, new_vector_store)
    return new_assistant

def process_document_object(document_object, document_name, file_path, assistant, thread):
    """Process a document object, check its existence, and create a thread for assessment."""
    json_content = document_object  # Or some default structure if needed

    instruction = f"Please use the object below to read through the {document_name} and add your assessment of the different requirements to the following object {document_object}. For compliance grade use NC for non-compliant, PC for partly compliant, C for compliant and NA for not applicable. When writing the detailed compliance explanations, be highly careful to write elaborate explanations that explain exactly why you have assessed it the way you have. Use concrete examples from the document, and where necessary use concrete examples from the MDR. IMPORTANT your response should only include the updated object, and nothing else. The object you return should have the following exact format and structure"

    message = add_message_to_thread(thread, instruction)
    output = create_run_and_get_output(thread, assistant)

    try:
        json_string = output["message"].strip("```json").strip("```").strip()
        json_content = json.loads(json_string)  # Parse the JSON string into a dictionary
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        json_content = {}

    return json_content

def process_and_update_document_based_structure(requirement_name):
    """Process and update the document-based structure for a specific requirement."""
    # Start the timer
    start_time = time.time()

    # Start the spinner
    loader_text = f"Insert assessment in document based: {requirement_name}"
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
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return

        # Loop over each document in the document-based structure
        for document_name, requirements in document_based_structure.items():
            document_name = document_name.lstrip("./")
            file_path = f"{technical_file_directory}/{document_name}"
            check_pdf_existence(file_path)

            assistant = create_and_setup_assistant(document_name, file_path) #+MDR!
            instruction = f"We need to check {document_name} for compliance with various requirements. You will gradually receive the requirements, please follow the instructions to assess compliance with specified requirements"
            thread = create_thread(f"{base_instruction}. {instruction}")
           
            if file_path in files_found:
                # Loop over each requirement in the document
                for i in range(len(requirements)):
                    document_object = requirements[i]
                    updated_document_object = process_document_object(document_object, document_name, file_path, assistant, thread)
                    requirements[i] = updated_document_object

            # Overwrite the original file with the updated structure
            with open(original_output_file_path, 'w') as json_file:
                json.dump(document_based_structure, json_file, indent=4)
        
    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time:.2f} seconds: {loader_text}")  # Print a completion message with time taken



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
