from openai import OpenAI
from datetime import datetime, timedelta

client = OpenAI()


def create_assistant_with_file_search(name, instructions, model): 
    # print("#### Creating assistant with file_search enabled")
    assistant = client.beta.assistants.create(
        name=name,
        instructions=instructions,
        model=model,
        tools=[{"type": "file_search"}],
    )
    # print(f"Assistant '{name}' created with ID: {assistant.id}")

    return assistant

def upload_files_and_add_to_vector_store(name, file_paths): 
    
    # Create a vector store caled "Financial Statements"
    # print("#### Creating vector store for the files")
    vector_store = client.beta.vector_stores.create(name=name)
    # print(f"Vector store created with ID: {vector_store.id}")

    # Ready the files for upload to OpenAI
    # print("#### Preparing files for upload")
    file_paths = file_paths
    file_streams = [open(path, "rb") for path in file_paths]
    # print(f"Prepared {len(file_streams)} files for upload")
    
    # Use the upload and poll SDK helper to upload the files, add them to the vector store,
    # and poll the status of the file batch for completion.
    # print("#### Uploading files to vector store")
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
    )
    # print("Files uploaded and added to vector store")
    # print(f"File batch status: {file_batch.status}")
    # print(f"File batch contains {file_batch.file_counts} files")

    return vector_store

def update_assistant_to_use_vector_store(assistant, vector_store):
    assistant = client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

    return assistant

def create_thread(instruction): 
 
    # Create a thread and attach the file to the message
    # print("####creating thread")
    thread = client.beta.threads.create(
    messages=[
        {
        "role": "user",
        "content": instruction,
        }
    ]
    )
    
    # The thread now has a vector store with that file in its tool resources.
    # print(f"created thread: {thread}")

    return thread

def create_run_and_get_output(thread, assistant): 

    # print(f"###creating run of thread with id {thread.id} with assistant {assistant.id}")
    
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=assistant.id
    )
    # print (f"###run created. {run}")

    messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

    message_content = messages[0].content[0].text
    annotations = message_content.annotations
    citations = []
    for index, annotation in enumerate(annotations):
        message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
        
        # Replace the walrus operator with a standard if-statement
        file_citation = getattr(annotation, "file_citation", None)
        if file_citation is not None:
            cited_file = client.files.retrieve(file_citation.file_id)
            citations.append(f"[{index}] {cited_file.filename}")

    # print("#### returning message and citations")
    return {"message": message_content.value, "citations": citations}

def add_message_to_thread(thread, content):

    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=content
    )

    return message