from datetime import datetime, timedelta, timezone
from openai import AsyncOpenAI
import asyncio
import json
import random
from base_variables import decoding_results

client = AsyncOpenAI()

# Global dictionary to store API call logs
api_call_log = {
    "create_assistant_with_file_search": [],
    "upload_files_and_add_to_vector_store": [],
    "update_assistant_to_use_vector_store": [],
    "create_thread": [],
    "create_run_and_get_output": [],
    "add_message_to_thread": []
}

# List to store timestamps of recent API calls for estimating token usage
recent_api_calls = []

# Estimate each API call uses 20,000 tokens
estimated_tokens_per_call = 20000

def save_api_call_log_to_file(api_call_log=api_call_log, file_path="/Users/mathiasmilsostephensen/Documents/qms_ai_api/api_call_log.txt"):
    try:
        # Calculate the total tokens used
        total_prompt_tokens = 0
        total_completion_tokens = 0
        total_tokens = 0

        for key in api_call_log:
            for entry in api_call_log[key]:
                total_prompt_tokens += entry.get("prompt_tokens", 0)
                total_completion_tokens += entry.get("completion_tokens", 0)
                total_tokens += entry.get("total_tokens", 0)

        # Create the summary line
        summary_line = f"Total Prompt Tokens: {total_prompt_tokens}, Total Completion Tokens: {total_completion_tokens}, Total Tokens: {total_tokens}\n"

        # Convert the api_call_log dictionary to a JSON formatted string
        log_as_string = json.dumps(api_call_log, indent=4, default=str)  # Using default=str to handle datetime serialization

        # Open the file in write mode and save the log string to the file
        with open(file_path, 'w') as file:
            file.write(summary_line)  # Write the summary line at the top
            file.write(log_as_string)  # Write the JSON log below

        print(f"API call log successfully saved to {file_path}")

    except Exception as e:
        print(f"An error occurred while saving the API call log: {e}")

async def get_estimated_token_usage_in_last_60_seconds():
    current_time = datetime.now(timezone.utc)
    one_minute_ago = current_time - timedelta(seconds=60)
    
    # Filter the recent API calls to get only those made in the last 60 seconds
    recent_calls_in_last_60_seconds = [call for call in recent_api_calls if call >= one_minute_ago]
    
    # Calculate estimated token usage
    estimated_token_usage = len(recent_calls_in_last_60_seconds) * estimated_tokens_per_call
    
    # Update the recent_api_calls list to remove old calls
    recent_api_calls[:] = recent_calls_in_last_60_seconds

    return estimated_token_usage

async def create_assistant_with_file_search(name, instructions, model):
    # Check if name exceeds 256 characters and truncate if necessary
    if len(name) > 256:
        name = name[:256]

    assistant = await client.beta.assistants.create(
        name=name,
        instructions=instructions,
        model=model,
        tools=[{"type": "file_search"}],
        temperature=0.2
    )

    return assistant
    
async def upload_files_and_add_to_vector_store(name, file_paths):
    # Check if name exceeds 256 characters and truncate if necessary
    if len(name) > 256:
        name = name[:256]

    vector_store = await client.beta.vector_stores.create(name=name)

    # Open files in binary mode and create file streams
    file_streams = [open(path, "rb") for path in file_paths]

    # Upload files to the vector store and poll for completion
    await client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )

    # Close the file streams to release resources
    for file_stream in file_streams:
        file_stream.close()

    return vector_store

async def update_assistant_to_use_vector_store(assistant, vector_store):
    assistant = await client.beta.assistants.update(
        assistant_id=assistant.id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
    )

    return assistant

async def create_thread(instruction):
    # Check the length of the instruction
    if len(instruction) > 256000:
        # Truncate the instruction to the first 250,000 characters
        instruction = instruction[:250000]

    # Create a thread with the (potentially truncated) instruction
    thread = await client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": instruction,
            }
        ]
    )

    return thread

async def create_run_and_get_output(thread, assistant, description):
    processed_data = {"message": "", "citations": []}
    retry_count = 0
    max_retry_count = 10
    token_threshold = 150000  # Example threshold for tokens used in the last 60 seconds
    request_threshold = 30   # Example threshold for requests in the last 60 seconds

    while retry_count < max_retry_count:
        try:
            # Calculate estimated token usage for the last 60 seconds
            estimated_token_usage = await get_estimated_token_usage_in_last_60_seconds()

            # If thresholds are exceeded, wait for a random period between 1 and 3 minutes
            if estimated_token_usage > token_threshold:
                wait_time = random.uniform(60, 180)  # Random wait between 1 and 3 minutes
                print(f"Exceeded threshold. Waiting for {wait_time:.2f} seconds...")
                await asyncio.sleep(wait_time)

            # Record the current time for the API call
            recent_api_calls.append(datetime.now(timezone.utc))

            # Proceed with creating the run
            run = await client.beta.threads.runs.create_and_poll(
                thread_id=thread.id, assistant_id=assistant.id
            )

            # Check if run usage is available and log it
            if hasattr(run, 'usage') and run.usage is not None:
                prompt_tokens = run.usage.prompt_tokens
                completion_tokens = run.usage.completion_tokens
                total_tokens = run.usage.total_tokens

                # Log actual usage data
                api_call_log["create_run_and_get_output"].append({
                    "timestamp": datetime.now(timezone.utc),  # Add timezone-aware timestamp here
                    "description": description,
                    "prompt_tokens": prompt_tokens,
                    "completion_tokens": completion_tokens,
                    "total_tokens": total_tokens
                })
                
                # Print the total tokens used across all runs
                total_tokens_used = sum(entry.get("total_tokens", 0) for entry in api_call_log["create_run_and_get_output"])
                print(f"Total tokens used so far: {total_tokens_used}")

            if run.status == 'completed':
                messages = await client.beta.threads.messages.list(thread_id=thread.id)
                
                if messages.data:
                    first_message = messages.data[0]
                    
                    if first_message.content and first_message.content[0].text:  # type:ignore
                        message_content = first_message.content[0].text  # type:ignore
                        annotations = message_content.annotations
                        citations = []

                        for index, annotation in enumerate(annotations):
                            message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
                            
                            file_citation = getattr(annotation, "file_citation", None)
                            if file_citation is not None:
                                cited_file = await client.files.retrieve(file_citation.file_id)
                                citations.append(f"[{index}] {cited_file.filename}")

                        processed_data = {
                            "message": message_content.value,
                            "citations": citations
                        }

                break
            else:
                if run.last_error and run.last_error.code == 'rate_limit_exceeded':
                    retry_count += 1
                    if retry_count < max_retry_count:
                        wait_time = 60
                        await asyncio.sleep(wait_time)
                    else:
                        print(f"Maximum retries reached. Exiting after {retry_count} attempts.")
                        break
                else:
                    break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    # Parse the message content as JSON
    json_content = {}
    try:
        # Check if the output message has the expected format
        if "message" in processed_data and processed_data["message"]:
            # Extract the JSON-like content
            json_string = processed_data["message"]
            
            # Ensure it starts and ends correctly for JSON format
            if json_string.startswith("```json") and json_string.endswith("```"):
                json_string = json_string.strip("```json").strip("```").strip()
                
                # Attempt to load the JSON content
                json_content = json.loads(json_string)
                decoding_results["success"] += 1
            else:
                decoding_results["failures"] += 1
                decoding_results["failures_details"].append({
                    "error": "Invalid JSON format",
                    "raw_output": processed_data["message"]
                })
        else:
            decoding_results["failures"] += 1
            decoding_results["failures_details"].append({
                "error": "Empty or no output message",
                "raw_output": processed_data["message"]
            })
    except json.JSONDecodeError as e:
        decoding_results["failures"] += 1
        decoding_results["failures_details"].append({
            "error": str(e),
            "raw_output": processed_data["message"]
        })
        json_content = {}
    except Exception as e:
        decoding_results["failures"] += 1
        decoding_results["failures_details"].append({
            "error": str(e),
            "raw_output": processed_data["message"]
        })
        json_content = {}

    # Return both the raw message and the JSON content
    return {"raw_output": processed_data["message"], "json_content": json_content}


def log_decoding_issues(decoding_results, file_path="decoding_issues.txt"):
    try:
        with open(file_path, 'a') as log_file:
            # Log the summary of decoding results
            log_file.write(f"Successful Decodings: {decoding_results['success']}\n")
            log_file.write(f"Failed Decodings: {decoding_results['failures']}\n")

            # Log details of each failed decoding attempt
            for failure in decoding_results["failures_details"]:
                log_file.write(f"Error: {failure['error']}\n")
                log_file.write(f"Raw Output: {failure['raw_output']}\n\n")

        print(f"Decoding issues logged to {file_path}")
    except Exception as e:
        print(f"An error occurred while logging decoding issues: {e}")


async def add_message_to_thread(thread, content):
    message = await client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=content
    )

    return message

# Example usage
# asyncio.run(main_function())
