import os
import json
import shutil
import subprocess
import time
import asyncio  # Import asyncio to handle asynchronous functions
from insert_relevant_documents import insert_relevant_documents
from base_variables import base_instruction, model, mdr_path, technical_file_directory
from create_assistant_with_files import create_assistant_with_file_search, upload_files_and_add_to_vector_store, update_assistant_to_use_vector_store
from create_mdr_expert import create_mdr_expert
from create_document_based_structure import process_and_save_document_based_structure, convert_document_to_requirement_based
from create_assistant_with_files import create_thread, create_run_and_get_output
from insert_assessments_in_document_based_structure import process_and_update_document_based_structure
from consolidate_requirement_assessments import consolidate_requirements
from clean_up_functions import delete_all_assistants, delete_all_vector_stores, delete_all_files

async def main():
    start_time = time.time()

    ##"device_description_and_specification", "information_supplied_by_manufacturer"
    selected_requirement_categories = ["device_description_and_specification"]

    steps_enabled = {
        "create_mdr_expert": True,
        "insert_relevant_documents": False, #prompts mdr_expert assistant to insert most relevant documents in object template and save in prompt_out
        "insert_assessments_in_document_based_structure": True,
        "merge_document_based_assessments_to_requirement_based": False,
        "consolidate_individual_document_assessments": False,
        "clean_up": False #deletes all vectors stores and assistants associated with the openAI account
    }

    assistants = {}

    ###create mdr_expert awith access to mdr
    if steps_enabled["create_mdr_expert"]: 
        mdr_expert = create_mdr_expert()
        assistants["mdr_expert"] = mdr_expert

    ##### add relevant documents
    if steps_enabled["insert_relevant_documents"]:
        for requirement in selected_requirement_categories:
            insert_relevant_documents(requirement, mdr_expert)
            process_and_save_document_based_structure(f"{requirement}_with_relevant_documents")

    ####Update document_based_structure with assessment for relevant requirements
    if steps_enabled["insert_assessments_in_document_based_structure"]:
        # Use await here to ensure asynchronous function is called correctly
        for requirement in selected_requirement_categories:
            await process_and_update_document_based_structure(requirement)
       

    ###Merge document based asssessment to a single requirement based object
    if steps_enabled["merge_document_based_assessments_to_requirement_based"]:
        for requirement in selected_requirement_categories:
            convert_document_to_requirement_based(requirement)

    ###consolidate into a single assessment per requirement
    if steps_enabled["consolidate_individual_document_assessments"]:
        for requirement in selected_requirement_categories: 
            consolidate_requirements(requirement, mdr_expert) 

    if steps_enabled["clean_up"]:
        models_deleted = delete_all_assistants()
        vector_stores_deleted = delete_all_vector_stores()
        files_deleted = delete_all_files()
        
        print(f"Total models deleted: {models_deleted}")
        print(f"Total vector stores deleted: {vector_stores_deleted}")
        print(f"Total files deleted: {files_deleted}")
        
    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    print(f"Completed in {elapsed_minutes:.2f} minutes.")

# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())
