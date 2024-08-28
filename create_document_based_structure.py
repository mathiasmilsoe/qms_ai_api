import json
import os
import time
import threading
from collections import defaultdict
from spinner import spinner_loader  # Import the spinner_loader function

def process_and_save_document_based_structure(name):
    # Define paths
    input_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output"
    output_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/document_based_structure"
    input_file_path = os.path.join(input_directory, f"{name}.json")
    output_file_path = os.path.join(output_directory, f"{name}_document_based.json")

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Load the JSON file
    try:
        with open(input_file_path, 'r') as json_file:
            requirements_data = json.load(json_file)
    except FileNotFoundError:
        return
    except json.JSONDecodeError:
        return

    # Create the document-based structure
    document_based_structure = defaultdict(list)
    for requirement in requirements_data["requirements"]:
        for document in requirement["relevant_documents"]:
            requirement_copy = {
                "requirement": requirement["requirement"],
                "reference": requirement["reference"],
                "description": requirement["description"],
                "relevant_documents": requirement["relevant_documents"],
                "overall_compliance_grade": requirement["overall_compliance_grade"],
                "detailed_compliance_explanation": requirement["detailed_compliance_explanation"],
                "required_follow_up_checks": requirement["required_follow_up_checks"],
                "sub_requirements": requirement["sub_requirements"]
            }
            document_based_structure[document].append(requirement_copy)

    # Convert the defaultdict to a regular dictionary before saving
    document_based_structure = dict(document_based_structure)

    # Save the structure to a JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(document_based_structure, json_file, indent=4)

def convert_document_to_requirement_based(requirement_name):
    # Start the timer
    start_time = time.time()
    
    # Start the spinner for converting to requirement-based structure
    stop_spinner_event, spinner_thread = spinner_loader(f"Converting to requirement-based structure for: {requirement_name}")

    try:
        # Define file paths based on the requirement name
        input_path = f"/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/document_based_structure/{requirement_name}_with_relevant_documents_document_based.json"
        output_path = f"/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output/for_consolidation/{requirement_name}_document_asssesments_for_consolidation.json"
        
        # Read the document-based JSON file
        with open(input_path, 'r') as file:
            document_based = json.load(file)

        # Initialize an empty dictionary to store the requirement-based data
        requirement_based = {"requirements": []}
        
        # Dictionary to keep track of requirements we've seen
        requirements_map = {}

        # Iterate over each document in the document-based data
        for document, assessments in document_based.items():
            for assessment in assessments:
                req_name = assessment["requirement"]
                if req_name not in requirements_map:
                    new_req = {
                        "requirement": req_name,
                        "reference": assessment["reference"],
                        "description": assessment["description"],
                        "required_follow_up_checks": [],
                        "checked_documents": [],
                        "overall_compliance_grade": {},
                        "non_conformities": [],
                        "sub_requirements": []
                    }
                    requirements_map[req_name] = new_req
                    requirement_based["requirements"].append(new_req)
                
                req_entry = requirements_map[req_name]
                req_entry["checked_documents"].append(document)
                req_entry["overall_compliance_grade"][document] = assessment["overall_compliance_grade"]
                req_entry["required_follow_up_checks"].append(assessment["required_follow_up_checks"])

                for sub_req in assessment["sub_requirements"]:
                    existing_sub_req = next((sr for sr in req_entry["sub_requirements"] if sr["description"] == sub_req["description"]), None)
                    
                    if existing_sub_req is None:
                        new_sub_req = {
                            "description": sub_req["description"],
                            "compliance_grade": {},
                            "detailed_compliance_explanation": {},
                            "non_conformities": [],
                            "assessment_criteria": sub_req["assessment_criteria"]
                        }
                        req_entry["sub_requirements"].append(new_sub_req)
                    else:
                        new_sub_req = existing_sub_req

                    new_sub_req["compliance_grade"][document] = sub_req["compliance_grade"]
                    new_sub_req["detailed_compliance_explanation"][document] = sub_req["detailed_compliance_explanation"]
                    if sub_req["non_conformities"]:
                        new_sub_req["non_conformities"].extend(sub_req["non_conformities"])

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write the requirement-based JSON file
        with open(output_path, 'w') as outfile:
            json.dump(requirement_based, outfile, indent=4)

    finally:
        # Stop the spinner after the task is completed
        stop_spinner_event.set()
        spinner_thread.join()

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(f"Finished in {elapsed_time:.2f} seconds: Converting to requirement-based structure for {requirement_name}")
