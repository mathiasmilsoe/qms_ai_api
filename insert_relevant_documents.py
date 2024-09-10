import asyncio
import json
import os
import time
from base_variables import base_instruction, list_of_files, output_directory
from create_assistant_with_files import create_thread, create_run_and_get_output
from report_category_sections.device_description_and_specification import device_description_and_specification
from report_category_sections.information_supplied_by_manufacturer import information_supplied_by_manufacturer
from report_category_sections.design_and_manufacturing_information import design_and_manufacturing_information
from report_category_sections.general_safety_and_performance_requirements import general_safety_and_performance_requirements
from report_category_sections.benefit_risk_analysis_and_risk_management import benefit_risk_analysis_and_risk_management
from report_category_sections.product_verification_and_validation import product_verification_and_validation
from report_category_sections.post_market_surveillance import post_market_surveillance
from report_category_sections.clinical_evaluation import clinical_evaluation
from report_category_sections.documentation_structure_and_accessibility import documentation_structure_and_accessibility
from report_category_sections.compliance_with_common_specifications import compliance_with_common_specifications
from report_category_sections.usability_and_human_factors_engineering import usability_and_human_factors_engineering
from report_category_sections.software_lifecycle_processes import software_lifecycle_processes
from report_category_sections.cybersecurity_requirements import cybersecurity_requirements
from report_category_sections.supply_chain_traceability import supply_chain_traceability
from spinner import spinner_loader  # Import the spinner_loader function from spinner.py

async def insert_relevant_documents_for_sub_requirement(sub_requirement, requirement_category, mdr_expert):
    instruction = f"""
    Please use the file list provided below to add all the documents that are relevant to check the compliance of the individual requirements. IMPORTANT if a requirement relies on specific evidences or similar, use the traceability matrix or the STED document to find all the relevant evidences that must be inspected. It is critical that where relevant we identify both plans, protocols, and evidences for inspection. Please rather add a document too much than one too little. Please fill in your response in this object
    
    {sub_requirement}

    The available files are listed below. IMPORTANT, strictly add the names of the files as they appear in the list and no other text. IMPORTANT only return the JSON format (Strict formatting with double quates "" for strings) and nothing else.
    {list_of_files}
    """
    thread_add_relevant_documents = await create_thread(f"{base_instruction}. {instruction}")

    output = await create_run_and_get_output(thread_add_relevant_documents, mdr_expert, f"insert relevant documents {requirement_category} - {sub_requirement['description']}")
    output_json = output['json_content']

    sub_requirement.update(output_json)

async def insert_relevant_documents(requirement_category, mdr_expert):
    start_time = time.time()
    
    requirement_objects = {
        "device_description_and_specification": device_description_and_specification,
        "information_supplied_by_manufacturer": information_supplied_by_manufacturer,
        "design_and_manufacturing_information": design_and_manufacturing_information,
        "general_safety_and_performance_requirements": general_safety_and_performance_requirements,
        "benefit_risk_analysis_and_risk_management": benefit_risk_analysis_and_risk_management,
        "product_verification_and_validation": product_verification_and_validation,
        "post_market_surveillance": post_market_surveillance,
        "clinical_evaluation": clinical_evaluation,
        "documentation_structure_and_accessibility": documentation_structure_and_accessibility,
        "compliance_with_common_specifications": compliance_with_common_specifications,
        "usability_and_human_factors_engineering": usability_and_human_factors_engineering,
        "software_lifecycle_processes": software_lifecycle_processes,
        "cybersecurity_requirements": cybersecurity_requirements,
        "supply_chain_traceability": supply_chain_traceability
    }

    requirement_object = requirement_objects[requirement_category]
    
    loader_text = f"Inserting relevant documents for {requirement_category}"
    stop_spinner_event, spinner_thread = spinner_loader(loader_text)

    try:
        tasks = []
        for requirement in requirement_object["requirements"]:
            for sub_requirement in requirement["sub_requirements"]:
                tasks.append(insert_relevant_documents_for_sub_requirement(sub_requirement, requirement_category, mdr_expert))
        await asyncio.gather(*tasks)

        output_filename = f"{requirement_category}.json"

        os.makedirs(output_directory, exist_ok=True)

        output_filepath = os.path.join(output_directory, output_filename)

        with open(output_filepath, 'w') as json_file:
            json.dump(requirement_object, json_file, indent=4)

    finally:
        stop_spinner_event.set()
        spinner_thread.join()

        elapsed_time = time.time() - start_time
        print(f"Completed in {elapsed_time:.2f} seconds: {loader_text}")

async def main(mdr_expert, selected_requirement_categories):

    tasks = []
    for requirement in selected_requirement_categories:
        await insert_relevant_documents(requirement, mdr_expert)

    # await asyncio.gather(*tasks)