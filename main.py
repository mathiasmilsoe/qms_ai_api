import time
import asyncio
from insert_relevant_documents import main as insert_relevant_documents_main
from base_variables import selected_requirement_categories, decoding_results
from create_mdr_expert import create_mdr_expert
from insert_assessments import insert_assessments
from clean_up_functions import delete_all_assistants, delete_all_vector_stores, delete_all_files
from create_assistant_with_files import save_api_call_log_to_file
from create_abstracts import create_abstracts
from insert_suggestion import insert_suggestions

async def main():
    start_time = time.time()

    steps_enabled = {
        "create_mdr_expert": False,
        "insert_relevant_documents": False,
        "insert_assessments": False,
        "insert_suggestions": False,
        "create_abstracts_file": False,
        "clean_up": True 
    }

    assistants = {}

    # Create mdr_expert with access to mdr
    if steps_enabled["create_mdr_expert"]: 
        mdr_expert = await create_mdr_expert()
        assistants["mdr_expert"] = mdr_expert

    # Add relevant documents
    if steps_enabled["insert_relevant_documents"]:
        await insert_relevant_documents_main(assistants["mdr_expert"], selected_requirement_categories)

    # Update document-based structure with assessment for relevant requirements
    if steps_enabled["insert_assessments"]:
        await insert_assessments(selected_requirement_categories)

    if steps_enabled["insert_suggestions"]:
        await insert_suggestions(selected_requirement_categories)

    if steps_enabled["create_abstracts_file"]:
        await create_abstracts(mdr_expert) #type:ignore

    if steps_enabled["clean_up"]:
        models_deleted = delete_all_assistants()
        vector_stores_deleted = delete_all_vector_stores()
        files_deleted = delete_all_files()
        
        print(f"Total models deleted: {models_deleted}")
        print(f"Total vector stores deleted: {vector_stores_deleted}")
        print(f"Total files deleted: {files_deleted}")

    # Log decoding issues at the end
    log_decoding_issues(decoding_results)

    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time
    elapsed_minutes = elapsed_time / 60
    save_api_call_log_to_file()
    print(f"Completed in {elapsed_minutes:.2f} minutes.")
    
def log_decoding_issues(decoding_results, file_path="decoding_issues.txt"):
    try:
        with open(file_path, 'a') as log_file:
            log_file.write(f"Successful Decodings: {decoding_results['success']}\n")
            log_file.write(f"Failed Decodings: {decoding_results['failures']}\n")

            for failure in decoding_results["failures_details"]:
                log_file.write(f"Error: {failure['error']}\n")
                log_file.write(f"Raw Output: {failure['raw_output']}\n\n")

        print(f"Decoding issues logged to {file_path}")
    except Exception as e:
        print(f"An error occurred while logging decoding issues: {e}")

# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())
