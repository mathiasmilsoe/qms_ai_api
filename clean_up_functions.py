import os
import json
import http.client
from spinner import spinner_loader  # Import the spinner_loader function
import time

# Your OpenAI API key
API_KEY = os.getenv('OPENAI_API_KEY')  # Ensure your API key is set as an environment variable

# Set headers for OpenAI API requests
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}',
    'OpenAI-Beta': 'assistants=v2'  # Required for accessing the Beta API
}

def delete_all_assistants():
    deleted_assistants_count = 0  # Initialize a counter for deleted assistants
    offset = 0  # Start with the first page of results
    limit = 20  # Number of results to request per page

    # Start the spinner
    stop_spinner_event, spinner_thread = spinner_loader("Deleting all assistants")

    try:
        while True:
            # Set up the connection
            conn = http.client.HTTPSConnection("api.openai.com")
            
            # List assistants with pagination
            conn.request("GET", f"/v1/assistants?limit={limit}&offset={offset}", headers=HEADERS)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            
            # Parse the response JSON
            assistants = json.loads(data).get('data', [])

            # If no more assistants are found, break the loop
            if not assistants:
                break

            # Iterate over each assistant
            for assistant in assistants:
                assistant_id = assistant['id']

                # Attempt to delete the assistant
                try:
                    conn = http.client.HTTPSConnection("api.openai.com")
                    conn.request("DELETE", f"/v1/assistants/{assistant_id}", headers=HEADERS)
                    delete_response = conn.getresponse()
                    delete_data = delete_response.read()
                    conn.close()

                    if delete_response.status == 200 and json.loads(delete_data).get('deleted'):
                        deleted_assistants_count += 1  # Increment the counter for each successful deletion
                    else:
                        print(f"Failed to delete assistant: {assistant_id}")

                except Exception as e:
                    print(f"Failed to delete assistant {assistant_id}: {e}")

            # Increment the offset to get the next page of results
            offset += limit

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        print(f"Completed: Deleted {deleted_assistants_count} assistants.")

    return deleted_assistants_count

def delete_all_vector_stores():
    deleted_vector_stores_count = 0  # Initialize a counter for deleted vector stores
    offset = 0  # Start with the first page of results
    limit = 20  # Number of results to request per page

    # Start the spinner
    stop_spinner_event, spinner_thread = spinner_loader("Deleting all vector stores")

    try:
        while True:
            # Hypothetical endpoint to list vector stores with pagination; replace with actual endpoint if available
            conn = http.client.HTTPSConnection("api.openai.com")
            conn.request("GET", f"/v1/vector_stores?limit={limit}&offset={offset}", headers=HEADERS)  # Placeholder
            response = conn.getresponse()
            data = response.read()
            conn.close()
            
            # Parse the response JSON
            vector_stores = json.loads(data).get('data', [])

            # If no more vector stores are found, break the loop
            if not vector_stores:
                break

            # Iterate over each vector store
            for vector_store in vector_stores:
                vector_store_id = vector_store['id']

                # Attempt to delete the vector store
                try:
                    conn = http.client.HTTPSConnection("api.openai.com")
                    conn.request("DELETE", f"/v1/vector_stores/{vector_store_id}", headers=HEADERS)  # Placeholder
                    delete_response = conn.getresponse()
                    delete_data = delete_response.read()
                    conn.close()

                    if delete_response.status == 200 and json.loads(delete_data).get('deleted'):
                        deleted_vector_stores_count += 1  # Increment the counter for each successful deletion
                    else:
                        print(f"Failed to delete vector store: {vector_store_id}")

                except Exception as e:
                    print(f"Failed to delete vector store {vector_store_id}: {e}")

            # Increment the offset to get the next page of results
            offset += limit

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        print(f"Completed: Deleted {deleted_vector_stores_count} vector stores.")

    return deleted_vector_stores_count


def delete_all_files():
    deleted_files_count = 0  # Initialize a counter for deleted files
    offset = 0  # Start with the first page of results
    limit = 20  # Number of results to request per page

    # Start the spinner
    stop_spinner_event, spinner_thread = spinner_loader("Deleting all files")

    try:
        while True:
            # Set up the connection
            conn = http.client.HTTPSConnection("api.openai.com")
            
            # List files with pagination
            conn.request("GET", f"/v1/files?limit={limit}&offset={offset}", headers=HEADERS)
            response = conn.getresponse()
            data = response.read()
            conn.close()
            
            # Parse the response JSON
            files = json.loads(data).get('data', [])

            # If no more files are found, break the loop
            if not files:
                break

            # Iterate over each file
            for file in files:
                file_id = file['id']

                # Attempt to delete the file
                try:
                    conn = http.client.HTTPSConnection("api.openai.com")
                    conn.request("DELETE", f"/v1/files/{file_id}", headers=HEADERS)
                    delete_response = conn.getresponse()
                    delete_data = delete_response.read()
                    conn.close()

                    if delete_response.status == 200 and json.loads(delete_data).get('deleted'):
                        deleted_files_count += 1  # Increment the counter for each successful deletion
                    else:
                        print(f"Failed to delete file: {file_id}")

                except Exception as e:
                    print(f"Failed to delete file {file_id}: {e}")

            # Increment the offset to get the next page of results
            offset += limit

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        print(f"Completed: Deleted {deleted_files_count} files.")

    return deleted_files_count
