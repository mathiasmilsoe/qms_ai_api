from openai import OpenAI
client = OpenAI()

model = "gpt-4o-mini" #"gpt-4o-mini" #"gpt-4o"

vector_store_expiry_days = 1

number_of_documents_per_requirement = 5

product_name ="paragitPX"

base_instruction = f""" 
You are a seasoned regulatory consultant and digital auditor with extensive 
expertise in medical device regulations, specifically the Medical Device 
Regulation (MDR) (EU) 2017/745. Your primary responsibility is to conduct 
a thorough and critical assessment of the technical documentation provided 
for the {product_name} medical device. Your approach should be that of a 
devil's advocate, rigorously identifying and documenting any gaps, 
non-conformities, potential risks, and areas of non-compliance 
with the MDR and any other relevant regulatory standards.
"""

mdr_path = "/Users/mathiasmilsostephensen/Downloads/CELEX_32017R0745_EN_TXT.pdf"

output_directory = "/Users/mathiasmilsostephensen/Documents/qms_ai_api/prompt_output"

technical_file_directory = "/Users/mathiasmilsostephensen/Library/CloudStorage/GoogleDrive-mathias.stephensen@gmail.com/Mit drev/AI-QMS/Paragit documentation/documents/paragitPX"

compliance_criteria = """
Compliant (C): The requirement is fully met with documented evidence.
Partly Compliant (PC): The requirement is partially met; some aspects are compliant while others need improvement.
Non-Compliant (NC): The requirement is not met at all.
Non-Applicable (NA): The requirement does not apply to the specific device or situation.
"""


list_of_files = '''
['./PX Summary of Technical Documentation (STED) v2.0 (Published).pdf', 'PX Annex 07 - Pre-Clinical and Clinical data/PX 2024-03 Clinical Evaluation Report v6.0 (Published).pdf', 'PX Annex 07 - Pre-Clinical and Clinical data/PX 2024-03 Literature Search Protocol v4.0 (Published).zip', 'PX Annex 07 - Pre-Clinical and Clinical data/PX CER author CV v3.0 (Published).zip', 'PX Annex 07 - Pre-Clinical and Clinical data/PX 2024-04 Election of Clinical Evaluation Report Author v2.0 (Published).pdf', 'PX Annex 07 - Pre-Clinical and Clinical data/PX 2024-03 Clinical Evaluation Plan v3.0 (Published).pdf', 'PX Annex 07 - Pre-Clinical and Clinical data/PX Signed Documents v2.0 (Published).pdf', 'PX Annex 07 - Pre-Clinical and Clinical data/PX 2024-04 Declaration of interests v4.0 (Published).pdf', 'PX Annex 07 - Pre-Clinical and Clinical data/PX Signed Documents/PX Declaration of interest (signed) v2.0 (Published).zip', 'PX Annex 07 - Pre-Clinical and Clinical data/PX Signed Documents/PX Clinical Evaluation Plan (signed) v2.0 (Published).zip', 'PX Annex 07 - Pre-Clinical and Clinical data/PX Signed Documents/PX Clinical Evaluation Report (signed) v2.0 (Published).zip', 'PX Annex 07 - Pre-Clinical and Clinical data/PX Signed Documents/PX Literature Search Protocol (signed) v2.0 (Published).zip', 'PX Annex 01 - Device Description and Specification/PX Product Classification v4.0 (Published).pdf', 'PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf', 'PX Annex 10 - Existing Approvals and Certificates/PX GS1 Company prefix Certificate v2.0 (Published).zip', 'PX Annex 10 - Existing Approvals and Certificates/PX GS1 Company prefix Certificate v2.0 (Published)/PX GS1 Company prefix Certificate v2.0 (Published).pdf', 'PX Annex 05 - Benefit-Risk Analysis and Risk Management/PX Risk Management Plan v1.8 (Obsolete).pdf', 'PX Annex 05 - Benefit-Risk Analysis and Risk Management/PX 2024-04-01 Risk Management Plan v3.0 (Published).pdf', 'PX Annex 05 - Benefit-Risk Analysis and Risk Management/PX Risk Management Report v1.3 (Obsolete).pdf', 'PX Annex 05 - Benefit-Risk Analysis and Risk Management/PX 2024-04-01 Risk Management Report v3.0 (Published).pdf', 'PX Annex 05 - Benefit-Risk Analysis and Risk Management/PX 2024-04-01 Risk Analysis (product) v4.0 (Published)/PX 2024-04-01 Risk Analysis (product) v4.0 (Published).pdf', 'PX Annex 05 - Benefit-Risk Analysis and Risk Management/PX Risk Analysis v1.5 (Obsolete)/PX Risk Analysis v1.5 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX PR231228-01 Project Review v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Software v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX PR240401-01 Project Review v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design Output v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX PR240425-01 Project Review v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Product Configuration v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Versions v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX IEC62304CLP231122-01-IEC 62304 Checklist - Paragit v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Quality Plan v1.5 (Draft).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX System Requirements List v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input v1.2 (Draft).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS User needs v1.5 (Draft).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input  v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Operational Requirements v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Regulatory Requirements v1.3 (Draft).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR005 The system shall have overheating protection to ensure that the operations shut down if the PCB or battery temperature exceeds 45 degrees v1.2 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR008 The system shall contain instructions for how to wash any washable parts v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR006 The system shall have over-discharge protection v1.2 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR002 The ParagitPX system must exclusively store personal data in an encrypted format v1.3 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR010 The system shall be designed to ensure secure and error-free integration of all electrical components. v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR011 The ParagitPX system shall incorporate security measures to restrict code updates to authorized personnel only v1.4 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR003 The system battery powering the operations shall be ISO certified v3.2 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PXS S-SR001 The Paragit PX system shall have soft edges with a radius of at least 2mm on all hard surfaces potentially in contact with skin- to avoid injury v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR007 The system shall be designed to comply with all applicable safety and reliability standards for electrical systems to ensure protection against electrical faults- including over-current- short circuits- and thermal runaway.  v4.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR009 The system shall be designed to ensure safe and reliable maintenance through controlled service procedures v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Safety Requirements/PX S-SR004 The system shall be designed to manage power efficiently and safely v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR007 The system shall allow the user to see when a recording was started and ended v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR001 The system shall measure bio-potential signals accurately in ranges that at least capture [0Hz - 500 Hz] v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR002 The system shall quantify impedance changes of at least 100 ohm in order to estimate the amount of accumulated sweat between the electrodes v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR003 The system shall measure 3D acceleration accurately in ranges typical for human movement during daily activity v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR006 The system shall be designed to ensure compatibility and interoperability with standard external computing devices for data management purposes. v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR008 The system shall allow the user to see when a recording was ended down to at least the second (UTC time) v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR009 The system shall provide the user with the exact (--- 0.5 Hz) sample rate that was used during a recording v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR005 The ParagitPX System shall be able to recharge from 0% to 100% via USB-C in a maximum of 6 hours v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Functional Requirements/PX S-FR004 The system shall measure 3D rotation accurately in ranges typical for human movement during daily activity v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PX S-PHR008 The ParagitPX System shall be designed for optimal usability- ensuring that all user interface components are easily accessible and distinguishable by touch. v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PX S-PHR009 The ParagitPX system shall be able to withstand appropriate transportation v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PXS S-PHR003 The ParagitPX system shall adhere to the weight budget outlined in this requirement v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PX S-PHR007 The Paragit PX system shall be operable using low amounts of force- allowing easy use for users with movement disorders v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PX S-PHR005 The ParagitPX system shall be collapsible  to a maximum width of 5cm v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PXS S-PHR004 The ParagitPX system shall adhere to the size budget outlined in this requirement v5.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PXS S-PHR001 The ParagitPX system shall be wearable for at least 95% of users v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Physical Requirements/PXS S-PHR006 The system must be designed to be universally wearable- accommodating placement on any part of the body. v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST007 The system shall comply with IP22- as confirmed by accredited centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST006 The system shall comply with EN 60529-1991 - A1-2000 - A2-2013- as confirmed by accredited centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST014 The system shall comply with ISO 62366-1-2015-A1-2020 v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST010 The system shall comply with IEC 60601-1-6- as confirmed by accredited test centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST005 The system shall comply with EN 60068-2-27-2009- as confirmed by accredited test centre  v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PXS S-ST003 CHEMICAL CHARACTERIZATION System materials in touch with the skin- shall be made of biocompatible material in accordance with ISO10993-18  v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST021 The system shall comply with IEC 60601-1-2- as confirmed by accredited test centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST018 The system shall comply with DS-EN 61340-5-1-2016 v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST020 The system shall comply with IEC 62133 v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST004 The system shall comply with EN 60068-2-64-2008- as confirmed by accredited test centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST012 The system shall comply with IEC 62304-2006-A1-2015 v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement  v2.1 (Draft).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST008 The system shall comply with IEC 60601-2-40- as confirmed by accredited test centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST019 The system shall comply with ISO 15223-1-2021 v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PXS S-ST001 CYTOTOXICITY System materials in touch with the skin- shall be made of biocompatible materials in accordance with ISO10993-5  v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST016 The system shall comply with DS-EN ISO 20417-2021 v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST011 The system shall comply with IEC 60601-1-11- as confirmed by accredited test centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST017 The system shall comply with IEC 60529-1989-AMD2-2013-COR1-2019 v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST013 The system shall comply with 14971-2019-A11-2021  v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PXS S-ST002 IRRITATION System materials in touch with the skin- shall be made of biocompatible materials in accordance with ISO10993-23 v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST015 The system shall comply with IEC-TR 62366-2-2016-AMD1-2020 v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST009 The system shall comply with IEC 60601-1- as confirmed by accredited test centre v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Operational Requirements/PX S-OR001 The ParagitPX system should be able to withstand disinfection with 70% isopropyl without any degradation in performance v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Operational Requirements/PX S-OR003 The ParagitPX system should store all data offline- locally on the device v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Operational Requirements/PX S-OR004 The ParagitPX system shall be able to withstand appropriate cleaning during its lifetime without performance degradation v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Operational Requirements/PX S-OR005 The ParagitPX system shall be active only when it is disconnected from the charger v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Operational Requirements/PX S-OR002 The ParagitPX System shall be constructed such that only the components in contact with the skin must be able to withstand a minimum of 10 wash cycles at 30 degrees Celsius with less than 5% degradation EMG signal nzUArukG v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PX S-PR006 The system shall be able to store at least 48 hours of data v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PX S-PR008 The system shall be designed to ensure consistent operational performance and reliability over a minimum service life of three years under normal usage conditions v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PXS S-PR003 The system shall measure 3D rotation accurately in ranges typical for human movement during daily activity v3.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PXS S-PR005- The ParagitPX system shall be able actively collect data over a minimum of 24 hours continuously  v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PX S-PR009 The system shall be designed to operate effectively without reliance on single-use consumables or additional materials beyond initial setup v4.0 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PX S-PR010 The system shall be durable enough to withstand connection life cycles through the lifetime  v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PXS S-PR007 The system shall allow the collection of sensitive EMG (-30 dB) without adjusting manual settings v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Performance Requirements/PX S-PR011 The system shall measure bio-potential signals accurately in ranges typical for human movement during daily activity [0Hz - 500 Hz] v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements/PXS S-UR001 The ParagitPX system shall only provide user feedback when prompted by the user v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements/PX S-UR005 The ParagitPX system shall have features to communicate status and errors to the user v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements/PX S-UR006 The ParagitPX system shall be able to provide feedback on current status within 0.5 seconds v1.4 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements/PX S-UR007 The system shall be capable of accurately logging events with precision to the second v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements/PX S-UR002 The system shall have the means to be turned on-off v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements/PX S-UR004 The ParagitPX system shall have haptic feedback of at least 0.00196newtons of force v4.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Usability Requirements/PX S-UR003 The ParagitPX system shall compromise one button for turning the device off v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS User needs/PX Clinicians User Needs v1.1 (Obsolete).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Design Output/PXS Design Output v1.1 (Draft).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Software/PX 2024-04-03 Software Architecture v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Software/PX 2024-04-03 Software Maintenance Plan v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Software/PX 2024-04-03 Software Configuration Record v2.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Software/PX SDP231228 Software Development Plan v3.0 (Published).pdf', 'PX Annex 03 - Design And Manufacturing Information/PX Versions/PXS 1.0.0 v2.0 (Published).pdf', 'PX Annex 09 - Technical Documentation on Post-market Surveillance/PX PMSP230220-01 PMS Plan v3.0 (Published).pdf', 'PX Annex 09 - Technical Documentation on Post-market Surveillance/PX PMCF240220-01 PMCF Plan v3.0 (Published).pdf', 'PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf', 'PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf', 'PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf', 'PX Annex 08 - EU Declaration of Conformity/PX EU Declaration of Conformity v2.0 (Published).pdf', 'PX Annex 04 - General Safety And Performance Requirements/PX 2024-04-01 List of Applicable Standards and Regulations v2.0 (Published).pdf', 'PX Annex 04 - General Safety And Performance Requirements/PX GSPR Checklist Final v2.0 (Published).pdf']
'''