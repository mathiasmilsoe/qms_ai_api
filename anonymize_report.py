import os
import json
import asyncio
import time
from create_assistant_with_files import create_assistant_with_file_search, create_thread, create_run_and_get_output
from spinner import spinner_loader
from base_variables import model

# Set your directories
input_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output"
output_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/anonymized"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Function to call OpenAI API for a single requirement
async def call_openai_api(requirement_data):
    instruction = f"""
    You are tasked with anonymizing the following JSON content. IMPORTANT: keep the exact same format, keys, structure, and details in the answers,
    but replace any descriptions, product details, company information, document prefixes, and findings with descriptions and findings for an imaginary medical device.
    Ensure the output has no identifiable information related to the original product or company. 
    The length of the JSON format must remain the same for demonstration purposes. 
    IMPORTANT: Only return the JSON object and nothing else.

    It is critical that you replace everything so that none of "ParagitPX" "PRU" "PFA" PEA" "PS" "Sleeve" "Research" or "Muscle activity and movement" is ever mentioned.
    instead re-write to a imaginary medical device for treating bladder infections.

    {json.dumps(requirement_data)}
    """

    assistant = await create_assistant_with_file_search('anonymization_assistant', instruction, model)
    thread = await create_thread(instruction)
    output = await create_run_and_get_output(thread, assistant, f"Anonymize JSON content")

    return output['json_content']

# Function to process a single file
async def process_file(file_path):
    # Load the JSON data from the file
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Extract requirements
    requirements = json_data.get("requirements", [])

    # Process all requirements concurrently
    anonymized_requirements = await asyncio.gather(
        *[call_openai_api(requirement) for requirement in requirements]
    )

    # Replace the old requirements with anonymized ones
    json_data["requirements"] = anonymized_requirements
    
    # Save the anonymized file with the same name in the 'anonymized' folder
    output_path = os.path.join(output_directory, os.path.basename(file_path))
    with open(output_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

# Function to loop through all files and process them asynchronously
async def process_all_files():
    files = [f for f in os.listdir(input_directory) if f.endswith('.json')]

    for file_name in files:
        file_path = os.path.join(input_directory, file_name)
        
        # Start the spinner for each file
        loader_text = f"Processing file: {file_name}"
        stop_spinner_event, spinner_thread = spinner_loader(loader_text)
        
        try:
            # Process the file (anonymization)
            await process_file(file_path)
        finally:
            # Stop the spinner when done
            stop_spinner_event.set()
            spinner_thread.join()

if __name__ == "__main__":
    start_time = time.time()
    print("Starting file anonymization...")

    # Run the async loop to process all files
    asyncio.run(process_all_files())

    elapsed_time = time.time() - start_time
    print(f"Completed anonymization in {elapsed_time:.2f} seconds.")
