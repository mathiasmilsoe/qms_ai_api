import os
import json
from create_assistant_with_files import create_thread, create_run_and_get_output
import asyncio
from base_variables import selected_requirement_categories
from spinner import spinner_loader  # Import spinner logic

async def create_abstracts(mdr_expert, base_path="/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output", 
                           abstracts_path="/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/abstracts"):
    """ 
    This function creates abstracts for each individual requirement category and then creates a consolidated abstract for the entire report.
    """
    
    # Step 1: Create abstracts for each individual requirement category
    category_abstracts = {}

    for requirement_category in selected_requirement_categories:
        print(f"Processing requirement category: {requirement_category}")

        # Start the spinner for this category
        loader_text = f"Processing abstract for category: {requirement_category}"
        stop_spinner_event, spinner_thread = spinner_loader(loader_text)

        try:
            # Correct the path for input file
            input_file = os.path.join(base_path, f"{requirement_category}.json")
            if not os.path.isfile(input_file):
                print(f"File not found: {input_file}")
                continue
            
            with open(input_file, 'r') as json_file:
                json_content = json.load(json_file)
            
            # Create instruction for each requirement category
            instruction = f"""
            Below you will find an object containing a detailed assessment of a technical documentation package against MDR for the category '{requirement_category}'.
            Based on the information provided in the object and your knowledge of the MDR, your task is to write an abstract 
            and extract the most important information from the report. The user will have access to the report, but the abstract will be the first thing they see.
            Focus on the aspects that are most critical to the manufactures compliance and write as a single cohesive short and precise text without bullets or numbering each requirement/subrequirement. 

            IMPORTANT only return the json object, and no additional text

            {{
                "section_abstract": string # a detailed abstract highlighting the findings of the report focusing on the aspects that are most critical to the manufacturer
            }}

            {json.dumps(json_content, indent=2)}
            """

            # Create thread and run the instruction
            thread = await create_thread(instruction)
            output = await create_run_and_get_output(thread, mdr_expert, instruction)
            category_abstracts[requirement_category] = output["json_content"]

            # try:
            #     # Check if the output message has the expected format
            #     if output and "message" in output and output["message"]:
            #         json_string = output["message"].strip("```json").strip("```").strip()
            #         # Attempt to load the JSON content
            #         category_abstract = json.loads(json_string)
            #         category_abstracts[requirement_category] = category_abstract
            #     else:
            #         print(f"No valid output message received or it is empty for category {requirement_category}.")
            # except json.JSONDecodeError as e:
            #     print(f"Failed to decode JSON for category {requirement_category}: {e}")
            # except Exception as e:
            #     print(f"An unexpected error occurred for category {requirement_category}: {e}")
        finally:
            # Stop the spinner after processing the category
            stop_spinner_event.set()
            spinner_thread.join()

    # Save individual abstracts
    abstracts_file_path = os.path.join(abstracts_path, "individual_abstracts.json")
    with open(abstracts_file_path, 'w') as json_file:
        json.dump(category_abstracts, json_file)
    print(f"Individual abstracts saved at {abstracts_file_path}")

    # Step 2: Create a consolidated abstract for the report
    print("Creating consolidated abstract for the report...")

    # Start spinner for consolidated abstract
    loader_text = "Processing consolidated abstract for the report"
    stop_spinner_event, spinner_thread = spinner_loader(loader_text)

    try:
        consolidated_instruction = f"""
        Below you will find abstracts for each requirement category based on the detailed assessment of a technical documentation package against MDR.
        Your task is to consolidate these abstracts into a comprehensive abstract for the entire report, highlighting the overall findings and aspects most critical to the manufacturer.
        Do not include any non-conformities in the abstract.

        IMPORTANT only return the json object, and no additional text

        {{
            "report_abstract": string # a detailed abstract highlighting the overall findings of the report focusing on the aspects that are most critical to the manufacturer
        }}

        {json.dumps(category_abstracts, indent=2)}
        """

        # Create thread and run the instruction for consolidated abstract
        thread = await create_thread(consolidated_instruction)
        output = await create_run_and_get_output(thread, mdr_expert, consolidated_instruction)
        consolidated_abstract = output['json_content']

        # try:
        #     # Check if the output message has the expected format
        #     if output and "message" in output and output["message"]:
        #         json_string = output["message"].strip("```json").strip("```").strip()
        #         # Attempt to load the JSON content
        #         consolidated_abstract = json.loads(json_string)
        #     else:
        #         print(f"No valid output message received or it is empty for consolidated abstract.")
        #         consolidated_abstract = {}
        # except json.JSONDecodeError as e:
        #     print(f"Failed to decode JSON for consolidated abstract: {e}")
        #     consolidated_abstract = {}
        # except Exception as e:
        #     print(f"An unexpected error occurred for consolidated abstract: {e}")
        #     consolidated_abstract = {}
        
    finally:
        # Stop spinner after processing the consolidated abstract
        stop_spinner_event.set()
        spinner_thread.join()

    # Save the consolidated abstract
    consolidated_file_path = os.path.join(abstracts_path, "report_abstract.json")
    with open(consolidated_file_path, 'w') as json_file:
        json.dump(consolidated_abstract, json_file)
    print(f"Consolidated abstract saved at {consolidated_file_path}")

    return "OK"

# Example usage
# asyncio.run(create_abstracts(mdr_expert))
