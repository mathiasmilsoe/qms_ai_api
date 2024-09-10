from insert_relevant_documents import insert_relevant_documents
from base_variables import base_instruction, model, mdr_path, traceability_matrix_path, sted_path
from create_assistant_with_files import create_assistant_with_file_search, upload_files_and_add_to_vector_store, update_assistant_to_use_vector_store
from spinner import spinner_loader  # Import the spinner_loader function
import time  # Import the time module

async def create_mdr_expert():
    # Start the timer
    start_time = time.time()
    
    # Start the spinner for creating 'mdr_expert'
    stop_spinner_event, spinner_thread = spinner_loader("Creating mdr_expert")

    try:
        # Step 2: Create an assistant called 'mdr_expert' with access to the specified MDR document
        mdr_expert = await create_assistant_with_file_search("mdr_expert", base_instruction, model) 

        # Step 3: Upload files and add them to the vector store
        mdr_vector_store = await upload_files_and_add_to_vector_store("mdr_vector_store", [mdr_path, sted_path, traceability_matrix_path])

        # Step 5: Update MDR expert assistant
        mdr_expert = await update_assistant_to_use_vector_store(mdr_expert, mdr_vector_store)

    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Finished in {elapsed_time:.2f} seconds: mdr_expert created.")  # Print the completion message with the time taken

    return mdr_expert
