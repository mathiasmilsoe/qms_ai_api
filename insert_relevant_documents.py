from base_variables import base_instruction, model, list_of_files, number_of_documents_per_requirement, mdr_path, output_directory
from create_assistant_with_files import create_assistant_with_file_search, create_thread, create_run_and_get_output, upload_files_and_add_to_vector_store, update_assistant_to_use_vector_store
from report_category_sections.device_description_and_specification import device_description_and_specification
from report_category_sections.information_supplied_by_manufacturer import information_supplied_by_manufacturer
from openai import OpenAI
import json
import os
from spinner import spinner_loader  # Import the spinner_loader function from spinner.py
import time  # Import the time module

client = OpenAI()

def insert_relevant_documents(requirement_category, mdr_expert):
    # Start the timer
    start_time = time.time()
    
    requirement_objects = {
        "device_description_and_specification": device_description_and_specification,
        "information_supplied_by_manufacturer": information_supplied_by_manufacturer
    }

    # Prepare the instruction for creating a new thread
    instruction = (
        f"Please use the file list provided below to add the {number_of_documents_per_requirement} documents (no less) for each requirement "
        f"where we are most likely to identify compliance with that requirement. Please fill in your response in this object {requirement_objects[requirement_category]}. "
        f"IMPORTANT Only change the key related to relevant_documents, and provide your reply with the updated object only and no additional text. "
        f"Available files: {list_of_files}. IMPORTANTLY! Write the filenames exactly as they are written in the list, excluding nothing and adding nothing. "
        f"We will be using the filenames and paths to find the files later."
    )
    
    # Start the spinner
    loader_text = f"Inserting relevant documents for {requirement_category}"
    stop_spinner_event, spinner_thread = spinner_loader(loader_text)

    try:
        # Create a new thread with the instructions
        thread_add_relevant_documents = create_thread(f"{base_instruction}. {instruction}")

        # Create run and get output
        output = create_run_and_get_output(thread_add_relevant_documents, mdr_expert)
        # print(output)

        # Extract and clean the JSON content from the output
        try:
            json_string = output["message"].strip("```json").strip("```").strip()
            json_content = json.loads(json_string)  # Parse the JSON string into a dictionary
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            json_content = {}

        # Save the JSON content to a file
        output_filename = f"{requirement_category}_with_relevant_documents.json"

        # Ensure the directory exists
        os.makedirs(output_directory, exist_ok=True)

        # Define the full file path
        output_filepath = os.path.join(output_directory, output_filename)

        # Save the JSON content as a normal JSON file
        with open(output_filepath, 'w') as json_file:
            json.dump(json_content, json_file, indent=4)

        # print(f"Output saved successfully to file {output_filename} at {output_filepath}")
    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time:.2f} seconds: {loader_text}")  # Print a completion message with time taken
