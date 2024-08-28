# # import pyperclip

# # Define the base prompt
# base_prompt = """ You are a seasoned regulatory consultant and digital auditor specializing in medical device regulations, specifically the Medical Device Regulation (MDR) (EU) 2017/745. Your task is to meticulously assess the provided technical documentation for the ParagitPX medical device. Your role is to act as a devil's advocate, rigorously identifying gaps, non-conformities, potential risks, and any areas of non-compliance with MDR and other relevant regulatory standards.

# Compliance Rating: Rate the compliance of the requirement using the following scale:

# Compliant (C)
# Partially Compliant (PC)
# Non-Compliant (NC)
# Not Applicable (NA)

# Documentation Completeness: Determine if all required documentation is present and accurately reflects the requirement.

# Accuracy of Information: Verify that the information aligns with the exact wording of the MDR.

# Clarity and Organization: Assess whether the information is presented clearly and logically.

# Traceability: Confirm that the requirement can be traced back to specific sections of the MDR.

# Examples and Evidence: Provide relevant examples from the MDR and the technical documentation to support your assessment.

# Non-Conformities: Identify specific non-conformities by referencing the wording from the MDR. Highlight any discrepancies and frame potential non-conformities as follow-up questions that may require further investigation.

# Regulatory Alignment: Ensure all assessments are aligned with specific articles, annexes, and requirements of the MDR (EU) 2017/745, and any other applicable standards, such as ISO 13485, ISO 14971, or IEC 62304.
# Concrete and Precise Feedback: Provide detailed, concrete feedback that references specific sections of the documentation and relates directly to the relevant regulatory clauses or standards.
# Gap and Risk Identification: Identify any missing elements, ambiguities, or weaknesses in the documentation that could lead to non-compliance or rejection by regulatory bodies.
# Actionable Recommendations: Offer precise, actionable recommendations for addressing each identified issue or gap, rooted in regulatory requirements.
# No Assumptions: Do not assume compliance; critically evaluate each component, ensuring no gaps are overlooked.
# Uncertainties: When identifying potential issues, include any areas of uncertainty or ambiguity that might indicate possible non-conformities. These uncertainties should prompt follow-up questions or further investigation, such as the absence of specific materials, unclear test results, incomplete risk assessments, or missing validation data. Where relevant, provide examples of what might be missing or require clarification to ensure full compliance.
# Multiple examples: when stating that e.g. the documentation lacks risks, contraindications, indications or anything else, use several examples of things that might have been omitted from the documentation
# **Specific Requirement:**

# IMPORTANT! When writing feedback, be very careful to always consider what the intended purpose of the device is so that we never suggest anything that is outside the scope of the device. 

# report_object = {
#   "requirements": [
#     {
#       "requirement": "General Device Information",
#       "reference": "MDR Annex II, Section 1.1(a)[1]",
#       "description": "This requirement involves providing essential information about the medical device, including the product or trade name, any alternative identifiers, a general description of the device and its intended purpose, as well as identifying the intended users and any necessary training for safe use.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           # "description": "Clearly state the product or trade name as it will appear on the market.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include any alternative names or identifiers used in marketing or distribution.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide a concise general description of the device, including its intended purpose.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Identify the intended users (e.g., healthcare professionals, patients) and any specific training required for use.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Unique Device Identification (UDI)",
#       "reference": "MDR Annex II, Section 1.1(b)[2]",
#       "description": "This requirement ensures the assignment and documentation of the Basic UDI-DI in compliance with MDR standards, including the format, structure, issuing agency, and any additional identifiers that support traceability.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Assign the Basic UDI-DI in accordance with the requirements of Part C of Annex VI.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide the format and structure of the Basic UDI-DI.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include the issuing agency for the UDI and any relevant registration numbers.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "If applicable, provide a clear identification by means of product code, catalogue number, or other unambiguous references that allow traceability.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Intended Use and Patient Population",
#       "reference": "MDR Annex II, Section 1.1(c)[3]",
#       "description": "This requirement mandates a comprehensive description of the device's intended use, the specific medical conditions it addresses, the patient population, indications for use, contraindications, and any warnings or precautions necessary for safe and effective use.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Describe the specific medical conditions the device is intended to diagnose, treat, or monitor.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Define the patient selection criteria, including age, gender, and health status.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "List indications for use, detailing the specific scenarios where the device is applicable.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Clearly outline contraindications for use, including any conditions or situations where the device should not be used.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide detailed warnings and precautions related to the device's use.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Principles of Operation",
#       "reference": "MDR Annex II, Section 1.1(d)[4]",
#       "description": "This requirement involves explaining the scientific principles that underlie the device's operation, its mode of action, and the provision of supporting scientific evidence or studies.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Explain the scientific principles underlying the device's operation.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Describe the mode of action, including how the device interacts with the body or performs its intended function.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide any necessary scientific evidence or studies that demonstrate the principles of operation.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Qualification Rationale",
#       "reference": "MDR Annex II, Section 1.1(e)[5]",
#       "description": "This requirement ensures a clear rationale for why the product qualifies as a medical device, referencing relevant MDR definitions and any applicable historical context or previous classifications.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Provide a detailed explanation of why the product qualifies as a medical device.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Reference applicable definitions from the MDR that support the qualification.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include any relevant historical context or previous classifications.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Risk Classification",
#       "reference": "MDR Annex II, Section 1.1(f)[6]",
#       "description": "This requirement involves stating the risk class of the device, justifying the classification based on specific rules from Annex VIII, and providing a summary of the risk assessment process and its outcomes.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "State the risk class of the device (Class I, IIa, IIb, III).",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Justify the classification rule(s) applied, referencing the specific rules from Annex VIII.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide a summary of the risk assessment process and outcomes.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Novel Features",
#       "reference": "MDR Annex II, Section 1.1(g)[7]",
#       "description": "This requirement focuses on identifying any novel features of the device that distinguish it from existing products, explaining how these features enhance performance or safety, and providing supporting studies or data.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Identify any novel features of the device that differentiate it from existing products.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide a detailed explanation of how these novel features enhance performance or safety.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include any relevant studies or data supporting the benefits of these novel features.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Accessories and Combinations",
#       "reference": "MDR Annex II, Section 1.1(h)[8]",
#       "description": "This requirement involves listing all accessories intended for use with the device, describing other products that may be used in combination, and providing instructions or guidelines for their use.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "List all accessories intended for use with the device, including their intended purpose.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Describe other devices or products that are not classified as devices but are intended to be used in combination with the device.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide any necessary instructions or guidelines for the use of accessories in conjunction with the device.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Configurations and Variants",
#       "reference": "MDR Annex II, Section 1.1(i)[9]",
#       "description": "This requirement ensures the documentation of all configurations and variants of the device, describing differences in functionality, design, or intended use, and including relevant documentation or specifications.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Provide a complete list of all configurations and variants of the device.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Describe the differences in functionality, design, or intended use among the variants.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include any relevant documentation or specifications for each variant.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Functional Elements",
#       "reference": "MDR Annex II, Section 1.1(j)[10]",
#       "description": "This requirement involves providing a detailed description of the key functional elements of the device, including parts and components, software functionality, and the formulation and composition of materials used. It also includes the provision of labelled pictorial representations to illustrate these elements.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Provide a detailed description of key functional elements, including parts and components.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include information on software components, if applicable, detailing their functionality and interaction with hardware.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Describe the formulation and composition of materials used in the device.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include labelled pictorial representations (e.g., diagrams, photographs, and drawings) to illustrate key functional elements.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Raw Materials",
#       "reference": "MDR Annex II, Section 1.1(k)[11]",
#       "description": "This requirement focuses on listing all raw materials used in the device, particularly those in direct or indirect contact with the human body, and providing details on sourcing, quality control, and relevant safety data or biocompatibility assessments.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "List all raw materials used in the device, specifying those that come into direct or indirect contact with the human body.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide details on the sourcing and quality control of raw materials.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include any relevant safety data sheets (SDS) or biocompatibility assessments.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Technical Specifications",
#       "reference": "MDR Annex II, Section 1.1(l)[12]",
#       "description": "This requirement involves providing detailed technical specifications of the device, including dimensions, weight, performance attributes, operational limits, environmental conditions for use, and the testing methods used to validate these specifications.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Provide detailed technical specifications, including dimensions, weight, and performance attributes.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include information on the device's operational limits and environmental conditions for use.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Describe any testing methods used to validate technical specifications.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Previous Generations",
#       "reference": "MDR Annex II, Section 1.2(a)[13]",
#       "description": "This requirement ensures the documentation of previous generations of the device, including any significant changes made, performance data or clinical outcomes, and any lessons learned that informed the current design.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Provide a detailed overview of previous generations of the device, including any significant changes made.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Include performance data or clinical outcomes from previous generations.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Discuss any lessons learned from previous generations that informed the current design.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     },
#     {
#       "requirement": "Similar Devices",
#       "reference": "MDR Annex II, Section 1.2(b)[14]",
#       "description": "This requirement involves identifying similar devices available on the Union or international markets, providing a comparative analysis of features, specifications, and intended use, and discussing any regulatory approvals or market performance of these similar devices.",
#       "relevant_documents": [],
#       "sub_requirements": [
#         {
#           "description": "Identify similar devices available on the Union or international markets.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Provide a comparative analysis of features, specifications, and intended use.",
#           "compliance_grade": "",
#           "non_conformities": []
#         },
#         {
#           "description": "Discuss any regulatory approvals or market performance of similar devices.",
#           "compliance_grade": "",
#           "non_conformities": []
#         }
#       ]
#     }
#   ]
# }




# IMPORTANT Your response should strictly be the object above filled in with information from the document. Do not omit any keys

# Confidential
# © 2024 Paragit Solutions ApS
# Status: Published
# Version: 4.0
# Date: 2024-04-05
# Project: QMS
# Authors: Mathias Stephensen (MAST)
# PX Instructions For Use
# Confidential
# © 2024 Paragit Solutions ApS
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 3 of 23
# © 2024 Paragit Solutions ApS
# Contents
# MANUFACTURER CONTACT DETAILS ...............................................................................................................5
# INTRODUCTION...............................................................................................................................................5
# INTENDED USE OF PRODUCT ...........................................................................................................................5
# INTENDED USE.........................................................................................................................................................5
# INDICATIONS FOR USE................................................................................................................................................5
# INTENDED USERS AND PATIENT POPULATION.................................................................................................................5
# CLINICAL BENEFIT .....................................................................................................................................................5
# CONTRAINDICATIONS ................................................................................................................................................6
# LIMITATIONS ...........................................................................................................................................................6
# WARNINGS .............................................................................................................................................................6
# POTENTIAL SIDE EFFECTS ...........................................................................................................................................7
# SAFETY ...................................................................................................................................................................7
# PARAGITPX SYSTEM COMPONENTS ..............................................................................................................................7
# REGULATORY INFORMATION .......................................................................................................................................8
# LIFETIME OF PRODUCT REUSABILITY, AND FREQUENCY OF USE ............................................................................................8
# SYMBOLS ........................................................................................................................................................8
# SAFETY WARNINGS AND CAUTIONS..............................................................................................................................9
# OTHER SYMBOLS ......................................................................................................................................................9
# INSTRUCTIONS FOR USE ................................................................................................................................11
# BEFORE USING THE DEVICE .......................................................................................................................................11
# WEARING THE DEVICE .............................................................................................................................................11
# HOW TO USE THE DEVICE .........................................................................................................................................11
# CLEANING AND CLEANING PRECAUTIONS......................................................................................................13
# THE OPERATION, STORAGE AND TRANSPORT CONDITIONS...........................................................................13
# INSTALLING, CALIBRATING OR SERVICING .....................................................................................................13
# MAINTENANCE AND DISPOSAL......................................................................................................................14
# MAINTENANCE ......................................................................................................................................................14
# DISPOSAL..............................................................................................................................................................14
# TECHNICAL DATA SHEET ................................................................................................................................15
# WARRANTY ...................................................................................................................................................21
# REVISION HISTORY ........................................................................................................................................22
# ATTACHED FILES............................................................................................................................................22
# ACCEPTANCE TASKS ......................................................................................................................................22
# SIGNATURES TASKS .......................................................................................................................................23
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 4 of 23
# © 2024 Paragit Solutions ApS
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 5 of 23
# © 2024 Paragit Solutions ApS
# Manufacturer contact details
# Legal manufacturer name: Paragit Neurotech ApS
# Manufacturer Address: Grundtvigsvej 6a, 1864 Frederiksberg, Denmark
# Manufacture E-mail: contact@paragit.com
# Manufacture Phone:+45 50939178
# Technical assistance contact/Email: contact@paragit.com
# Reporting Adverse effects contact/Email: stephensen@paragit.com
# Table 1: Manufacturer contract details
# Introduction
# Commercial product name: ParagitPX
# Medical device family name: ParagitPX
# Model number: ParagitPX
# Table 2: Introduction device information
# Intended Use of Product
# Intended Use
# ParagitPX is designed to collect signals for the investigation of processes related to muscle activity
# and movement (Electromyography - EMG, Movement - IMU, and skin impedance). It serves as a tool
# for athletes, sport enthusiasts, healthcare professionals and lay users to obtain objective and
# quantitative data on muscle activation, movement patterns, and impedance for research purposes
# only.
# Indications for use
# ParagitPX is indicated for use in any adult population not excluded by the contraindications to collect
# data that fosters an understanding of movement and muscle activation.
# Intended Users and Patient Population
# ParagitPX is intended for use by athletes, sports enthusiasts, healthcare professionals, and lay users
# for studying muscle activity and movement. ParagitPX is used by the adult population and it applies
# to a broad range of users interested in understanding muscle function and movement dynamics.
# Clinical benefit
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 6 of 23
# © 2024 Paragit Solutions ApS
# Objective Data Acquisition: Provides precise and objective data on muscle activation and
# movement, aiding in the understanding of muscle function and movement - research purposes only.
# Contraindications
# • Not to be used by individuals allergic to materials in contact with the skin, such as polyester,
# nylon, and silicon.
# • Not suitable for individuals with a history of severe skin irritation, open wounds, or lesions in
# the area of device placement.
# • Not intended for use by individuals who cannot tolerate pressure or mild compression on
# the skin, non-cooperating individuals, or those incapable of self-dressing without caregiver
# support.
# • The device has not been tested in pregnant or breastfeeding women; therefore, its use is
# contraindicated in these groups.
# • The device has not been tested in users with pacemakers; therefore, its use is
# contraindicated in these groups.
# Limitations
# • The device is not intended to support, suggest, or directly diagnose or monitor any disease.
# The system is solely intended to be used for research purposes related to muscle activation
# and movement.
# Warnings
# • Clean the skin before putting the sleeve or one of the two adapters on.
# • Take off immediately in case of rash, irritation, swelling or similar.
# • The device should not be used while taking a shower or exposing it to water in any other
# way.
# • The device must not be connected to a worn while also connected to a power source or
# computer.
# • The device should not be placed near any external electromagnetic fields during use.
# • Use and store the product in accordance with conditions outlined in the Instructions for Use
# (Avoid exposing the device to direct sunlight or extreme heat sources, temperature and
# humidity as these conditions can negatively impact the performance and lifespan of the
# device).
# • The device shall not be opened by the user and the battery is not intended to be replaced by
# the user.
# • The main plug of the power supply (charger) is considered as a disconnecting device. During
# charging, do not position the device in such a way that it is difficult to operate the charger.
# • Keep the AC adapter away from infants, toddlers and children.
# • Use of this equipment adjacent to or stacked with other equipment should be avoided
# because it could result in improper operation. If such use is necessary, this equipment and
# the other equipment should be observed to verify that they are operating normally.
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 7 of 23
# © 2024 Paragit Solutions ApS
# • Use of accessories, transducers and cables other than those specified or provided by this IFU
# could result in increased electromagnetic emissions or decreased electromagnetic immunity
# of this equipment and result in improper operation.
# • Portable RF communications equipment (including peripherals such as antenna cables and
# external antennas) should be used no closer than 30 cm (12 inches) to any part of the
# ParagitPX product, including cables specified by this IFU. Otherwise, degradation of the
# performance of this equipment could result.
# • The device should not be connected to a high frequency (HF) surgical equipment and to an
# Electromyography or Evoked response equipment.
# • The device should not be used close to a shortwave or microwave therapy equipment.
# Cases that customers can expect if Paragit PX performance is lost or degraded due to
# electromagnetic disturbance:
# • INA circuit inside PRU does not detect electromyography within acceptable SNR range.
# • IMU does not record acceleration or angular rate.
# • PRU does not record a minimum of 24h.
# • PRU does not transmit data through physical cable attachment.
# • PRU does not emit driver frequencies for evaluation of skin/electrode performance.
# Potential Side Effects
# • The most common side effect is mild skin irritation or redness, expected to resolve after
# removing the device.
# • In rare cases, allergic reactions to materials used in the device may occur. Immediate
# medical attention should be sought if signs of an allergic reaction appear.
# • If discomfort or uncomfortable pressure is experienced in the area where the device is
# placed, users shall remove the device.
# Safety
# Device does not emit hazardous, or potentially hazardous levels of radiation. The device does not
# contain or incorporate medicinal substances, including human blood or plasma derivatives, or
# tissues or cells, or their derivatives, of human origin, or tissues or cells of animal origin, or their
# derivatives. Paragit Sleeve (PS) is considered a type of BF applied part.
# ParagitPX system components
# The ParagitPX consists of the following 4 key components. Each of the key components are
# described below and depicted in a picture.
# • Paragit Recording Unit (PRU): Equipped with sensors for electromyography, movement, and
# impedance. Housed in a small PA2200 Nylon casing containing the electronics.
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 8 of 23
# © 2024 Paragit Solutions ApS
# • Paragit Sleeve (PS): A non-intrusive, textile-based sleeve with EMG sensors. Designed for
# wearability on upper or lower limbs, made of breathable, stretchable, and washable fabric.
# Available in various sizes and equipped with conductive yarn and polymer.
# • Paragit Electrode Adapter (PEA): A 3D printed adapter for connecting the PRU to electrodes
# with a set distance.
# • Paragit Flex Adapter (PFA): A 3D printed PA2200 adapter for flexible connection of the PRU
# to wired electrodes.
# PRU PS PEA PFA
# In addition to the key components above, the PRU can be charged with a Medical USB-C charger
# which is provided and delivered by Paragit Neurotech, and a small transportation pouch is included
# in the package.
# Regulatory information
# If any user/operator faces a serious incident while operating the ParagitPX, the device user/operator
# shall immediately report the incident to:
# • Paragit Neurotech ApS (contact information available at the beginning of this manual)
# • The Competent Authority of the country where the user/operator resides.
# Lifetime of product reusability, and frequency of use
# The various components of the solution have the following product lifetimes and reusability
# specifications:
# • The PRU, the charger, the PFA, and the PEA have product lifetimes of 3 years. Following
# outlined cleaning guidelines, these two components can be reused across patients.
# • The PS can be reused for up to 3 months or 16 recordings of 24 hours each. The PS should
# not be reused across patients as this can lead to loosened electrodes and degraded
# performance.
# The intended frequency of use is 1-4 cycles of 24 hours per month, but this should be customized by
# the clinician and/or researcher to fit the needs of the individual patient or trial.
# Symbols
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 9 of 23
# © 2024 Paragit Solutions ApS
# Safety Warnings and Cautions
# Indicate Warnings and Cautions are necessary when operating the device or that the
# current situation needs operator awareness or operator action to avoid undesirable
# consequences. Refers to all Warnings and Cautions which are described in this IFU.
# Table 3: Safety Warnings and Cautions symbols
# Other Symbols
# Medical device
# manufacturer
# Indicates the medical
# device manufacturer, as
# defined in EU
# Regulation MDR (EU)
# 2017/745.
# Medical Device
# Indicates the item is a
# medical device
# Company logo
# Serial number
# Indicates the
# manufacturer’s serial
# number so that a specific
# medical device can be
# identified.
# Catalogue number
# Symbol related to
# restriction of the use of
# certain hazardous
# substances in electrical
# and electronic equipment.
# Date of manufacture
# Indicates the date when
# the medical device was
# manufactured.
# “Follow instructions for
# use”
# Batch code
# Indicates the
# manufacturer's batch
# code so that the batch
# or lot can be identified.
# Operator's manual;
# operating instructions
# Indicates the need for the
# user to consult the
# instruction for use
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 10 of 23
# © 2024 Paragit Solutions ApS
# Caution
# Indicates the need for
# the user to consult the
# instructions for use for
# important cautionary
# information such as
# warnings and
# precautions that
# cannot, for a variety of
# reasons, be presented
# on the medical device
# itself.
# Temperature limit
# CE marked product Humidity limitation
# The WEEE symbol,
# indicating separate
# collection for WEEEWaste
# of electrical and
# electronic equipment,
# consists of the crossedout
# wheeled bin, as
# shown below. The
# symbol must be printed
# visibly, legibly and
# indelibly. The symbol is
# required per the Article
# 11(2) of the WEEE
# Directive.
# UDI sign
# Keep dry symbol,
# indicating that the
# transport package shall
# be kept away from rain
# and in dry conditions
# Do not use if package is
# damaged
# symbol, indicating that
# the device must not be
# used if the package
# holding the device is
# damaged, for example on
# packaging of medical
# devices.
# Single user multiple use
# symbol, indicating a
# medical device that may
# be used multiple times
# IP 22
# Water ingress protection
# rating 22.
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 11 of 23
# © 2024 Paragit Solutions ApS
# (multiple procedures)
# on a single user
# Type BF applied part.
# These are Applied Parts
# that make direct
# electrical contact with
# the user, except not
# directly to the heart.
# Direct current
# Atmospheric pressure
# range
# Table 4: Other symbols
# Instructions For Use
# Before using the device
# • Make sure that all units are delivered.
# • Prior to wearing the sleeve, the intended area should be cleaned
# • Connect the PRU to the PS, PEA, or PFA.
# Wearing the device
# • Place the device on the intended area. For sleeves, the white “X” should be placed in the
# elbow bend (forearm) and right under the knee bend (calf). For adapters, the electrodes are
# placed on the intended muscles.
# • If wearing the PS, the fit should be firm but not so tight that the user experiences any
# discomfort.
# How to use the device
# Get the current status of the PRU
# Click the button once to get the current status of the device:
# State LED & vibration Indication Description
# Ready for use Green light. Device is ready for use
# Ongoing sampling Short duration (1 second) blue light Sampling is currently ongoing
# Critical storage
# Long duration (3 seconds) red light and
# 2 vibrations
# Critical storage - please wipe the
# device
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 12 of 23
# © 2024 Paragit Solutions ApS
# Critical battery
# Long duration (3 seconds) red light and
# 3 vibrations
# Critical battery - please charge the
# device
# Critical Error
# Long duration (3 seconds) red light
# without vibrations
# A critical error has occurred and the
# device may not be in a working
# state. Please email bugreports@
# paragit.com
# Start recording: To start data collection, confirm that the device is ready to use and then hold the
# button and wait for two vibrations before releasing the button.
# Stop recording: To stop the recording, confirm that sampling is currently ongoing, then hold the
# button and wait for two vibrations before releasing the button.
# Log current time: To log the current time, confirm the device sampling, then hold the button and
# wait for 1 vibration before releasing the button.
# State LED & vibration Indication Description
# Sample Mode
# started
# Long duration (3 seconds) blue light
# Indicates that the device has
# started sampling data.
# Sample Mode
# Stopped
# Long duration (3 seconds) purple light
# Device has stopped sampling and is
# saving data
# Save Medtime Short duration (1 second) purple light
# Device is logging time of
# medication
# Other light indications:
# State LED & vibration Indication Description
# Charging Mode Orange light Device is charging
# Extracting the data
# To extract the data, connect the device to a USB-C port on a Windows. The device will appear as a
# USB Drive and the data can be extracted. While the PRU is connected to the computer, the device
# can be wiped by holding the button and waiting for 2 vibrations.
# Wiping and resetting the device
# Reset the device: To reset the device, hold the button and wait for 3 vibrations. Use with caution, as
# this may cause data loss.
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 13 of 23
# © 2024 Paragit Solutions ApS
# Reset and wipe the device Reset and wipe the device by holding the button and waiting for 4
# vibrations before releasing the button. Use with caution, as this can cause data loss.
# State LED & vibration Indication Description
# Wiping device White light
# Device is being wiped and all data
# will be deleted.
# Table 5: LED indications
# Cleaning and cleaning precautions
# To ensure the proper functioning and longevity of the ParagitPX device, as well as to maintain
# hygiene and prevent cross-contamination between users, it is crucial to follow the cleaning and
# cleaning precautions outlined below:
# • Prior to wearing the sleeve, the user’s skin should be cleaned and dried using the
# disinfection/alcohol wipes provided in the transportation bag.
# • The PRU must be cleaned thoroughly before sharing across users. To clean the PRU, use a
# 70% Isopropyl and thoroughly wipe the PRU for at least 30 seconds on all surfaces.
# The operation, storage and transport conditions
# To ensure the proper functioning and longevity of the ParagitPX device, it is important to adhere to
# the appropriate operation, storage, and transport conditions outlined below:
# • Operation Temperature: ParagitPX device within a temperature range of 2°C to 25°C to
# ensure optimal performance and prevent damage to the device components.
# • Operation Humidity: Maintain a relative humidity level of 25% to 85% to prevent
# condensation or excessive dryness, which could adversely affect the device's performance
# and lifespan.
# • Operation atmospheric pressure: from 700 hPa to 1060 hPa.
# • Storage, and transport conditions: -25°C to 75°C, 5°C to 35°C at a relative humidity up to
# 85% non-condensing, >35°C to 70°C at water vapour pressure up to 50 hPa.
# • Avoid exposing the device to direct sunlight or extreme heat sources, as these conditions
# can negatively impact the performance and lifespan of the device.
# • Handle the device with care during transport to avoid drops, impacts, or rough handling that
# could damage the device or its components.
# By following these operation, storage, and transport conditions, the ParagitPX device can be
# maintained in optimal condition, ensuring accurate data collection and a long lifespan.
# Installing, calibrating or servicing
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 14 of 23
# © 2024 Paragit Solutions ApS
# To ensure the proper functioning and longevity of the ParagitPX device, it is crucial to follow the
# appropriate procedures for installing, calibrating, and servicing the device as outlined below:
# Installing and calibrating:
# • Carefully unpack the ParagitPX device and its components from the packaging, and inspect
# them for any visible damage or defects. If any damage is present, contact the manufacturer
# for further assistance.
# • Assemble the device by attaching the PRU to the Paragit Sleeve or adapter depending on the
# use case, following the instructions provided in the Instruction for Use.
# • Ensure that the device is fully charged before use. Connect the PRU to the charger using the
# provided cable, and charge the unit until the indicator light confirms that the device is ready
# for use.
# • Once worn and turned on, the Paragit Sleeve will automatically calibrate itself to the user’s
# skin properties.
# Servicing:
# • If there is a need for service of ParagitPX device (when there is a breakdown or there is a
# need to replace some parts) please contact technical assistance. The user is not allowed to
# change or modify the parts of ParagitPX.
# Maintenance and disposal
# Maintenance
# Proper maintenance of the ParagitPX device is essential to ensure its optimal performance, accuracy,
# and longevity. Adhere to the maintenance guidelines outlined below to keep the device in good
# working condition:
# • Cleaning: Clean the device and its components regularly, following the cleaning and cleaning
# precautions outlined in the IFU.
# • Software Updates: It is not necessary to update either the PRU, unless specifically instructed
# to do so by Paragit Staff.
# • Storage and Transport: Store and transport the device following the appropriate storage and
# transport conditions outlined in this IFU.
# • Safety and performance: respect all safety, warnings and precautions information described
# in section warnings and precautions of this IFU.
# Disposal
# Proper disposal of the ParagitPX device and its components is crucial to protect the environment and
# comply with local regulations and guidelines. Follow the disposal instructions outlined below to
# ensure responsible disposal practices:
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 15 of 23
# © 2024 Paragit Solutions ApS
# • Paragit Sleeve Disposal: After using the Paragit Sleeve for its full lifecycle, it should be
# recycled by returning it to either the healthcare institution or Paragit.
# • Electronic Waste Disposal: At the end of the device's useful life or when it is no longer
# functional, do not dispose of the device or its electronic components, such as the PRU,
# battery, and charger, in regular household waste. Electronic waste should be disposed of
# according to local regulations and guidelines, which may include recycling programs or
# designated collection sites.
# • Accessory Disposal: Dispose of any non-electronic accessories, such as cables or carrying
# cases, in accordance with local waste disposal regulations.
# Technical data sheet
# General Specs
# Capacity 300mAh
# Charging Current Limited to 150mA
# Running Time
# 24h recording session on a
# full charge
# Standby Mode 125 days
# PRU Integrated Battery
# (DNK-LP402535)
# Data sheet PRU PRU-B DNK-LP402535
# Data Storage Continuous Logging
# Able to store data for 8 days
# continuous logging
# Data Transfer Connection to PC or Mac USB-C
# PRU Weight 40 grams
# PRU Sleeve (Type BF applied
# part)
# Replacement Lifetime
# Up to 3 months of usage or
# 16 times recording at 24
# hours each (whatever
# happens first)
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 16 of 23
# © 2024 Paragit Solutions ApS
# PRU Casing Manufacturing Process SLS PA2200 3D Printing
# Mounting Connector Attachment/detachment
# Mechanical stress of
# adapter on PS or PEA can
# withstand at least 100
# cycles
# Charger
# Manufacturer Horizon Digital Plus
# Model name HDP05-MD05010U
# Input:
# 100-240 Vac 50/60Hz 0.15
# A
# Output: 5 Vdc / 1 A / 5 W
# Charger
# Certifications IEC60950 and IEC60601
# Safety Specs
# Battery Over-charge protection Yes
# Battery Over-discharge protection Yes
# Battery Over-current protection Yes
# PRU
# Cable connection while
# usage
# Not Possible
# NTC Operating temperatures 0-45 degrees celcius
# Electromyography (muscle activity)
# Sampling rate
# Up to 2kHz @ 16-bit
# resolution (1-60mV input
# differential EMG voltage)
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 17 of 23
# © 2024 Paragit Solutions ApS
# Automatic Gain Selection 1x..32x gain amplification
# CMRR for the INA 100dB
# Measure Skin/Electrode
# Impedance Carrier
# Frequency
# 825Hz and 925Hz (+- 1.5Hz
# @ 1mV)
# PRU - PCB
# Architecture
# Arm Cortex-M33 with
# TrustZone and hardware
# security
# Maximum Clock Speed 160 MHz
# Flash Memory 2 MB
# SRAM 786 KB
# Voltage Range 1.7 V to 3.6 V
# Operating Temperature
# Range
# -40°C to 85°C
# I/Os Up to 136
# Communication Interfaces USB-C
# ADC 14-bit, up to 2.5 Msps
# DAC 12-bit, up to 1 Msps
# Timers 16-bit and 32-bit
# STMicroelectronics
# STM32U575RITx
# DMA Channels Up to 16
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 18 of 23
# © 2024 Paragit Solutions ApS
# Security Features
# AES, PKA, RNG, CRC, and
# TRNG
# ROHS Compliant
# PRU - IMU
# Smart FIFO Up to 9 kbytes
# Full Scale
# ±4/±8/±16/±32 g,
# ±125/±250/±500/±1000/±20
# 00 dps
# LSM6DSO32XTR
# Analog Supply Voltage 1.71 V to 3.6 V
# PRU - EMG Sensor
# Low Offset Voltage 25 μV (Maximum), G ≥ 100
# Low Drift 0.1 μV/°C, G ≥ 100
# Low Noise 50 nV/√Hz, G ≥ 100
# High CMRR 100 dB (Minimum), G ≥ 10
# Low Input Bias Current 200 pA (Maximum)
# Supply Range 1.8 V to 5.5 V
# Input Voltage (V–) +0.1 V to (V+) –0.1 V
# Output Range (V–) +0.05 V to (V+) –0.05 V
# INA333
# Low Quiescent Current 50
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 19 of 23
# © 2024 Paragit Solutions ApS
# Textile components
# Type of contact
# (Direct/indirect )
# Description
# Textile base Direct
# 86 % Polyamide 14 %
# Elastane
# Products do not contain
# latex or natural rubber or
# pose any harmful human
# impact
# associated with its intended
# use.
# Products do not contain
# human or animal tissue or
# extracts, prohibited azo dye
# pigments, medical
# substances or phthalates.
# The products are in
# compliance with REACH.
# No chemicals added during
# treatment/finishing.
# Products may contain
# softening and
# antistatic agents up to 1.5
# %.
# The products are covered by
# Oeko-Tex Standard 100,
# class II
# Data sheet: PS nonconductive
# base textile
# ElectroSkin GECKO 2.0 Direct ElectroSkin electrodes are
# built with a biocompatible
# silicone surface with optimal
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 20 of 23
# © 2024 Paragit Solutions ApS
# skin-electrode impedance
# which enables the highest
# signal quality.
# Has passed the following:
#  ISO 10993-5:2009
# (cytotoxicity)
#  ISO 10993-10:2021
# (skin sensitization)
#  ISO 10993-23:2021 (
# skin irritation)
# Insulation Patch Direct
# Adhesive patch to attach
# the electrodes to the textile
# base. Has passed the
# following:
#  ISO 10993-5:2009
# (cytotoxicity)
#  ISO 10993-10:2021
# (skin sensitization)
#  ISO 10993-23:2021 (
# skin irritation)
# Phantom Tape X Indirect
# Conductive tape to connect
# the electrodes to the
# PRU. Has passed the
# following:
#  ISO 10993-5:2009
# (cytotoxicity)
#  ISO 10993-10:2021
# (skin sensitization)
#  ISO 10993-23:2021 (
# skin irritation)
# 3D SLS PA2200; casing, PFA and PEA
# Nylon PA12 Quality polyamide 12
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 21 of 23
# © 2024 Paragit Solutions ApS
# Moisture Absorption Minimal
# Chemical Resistance
# Highly resistant to
# hydrocarbons, alkalis, fats,
# oils, fuel, ethers, ester and
# ketones
# Impact Strength
# Exceptional, even at low
# temperatures
# Melting Temperature 178 ºC
# Heat Deflection
# Temperature
# 50 ºC
# Service Temperatures
# without high mechanical
# load
# - long term: -50 to +80 ºC, -
# short term (max): +140 ºC
# Flammability according to
# UL94 (3mm / 6mm thick)
# HB
# Casing dimensions
# 11.92mm x 83.64mm x
# 31.35mm
# Table 6: Technical data sheet
# Note: The emission is tested according to the standard CISPR11 (EN 55011) Class B, Group I. As for
# immunity: ESD tests (Electrostatic discharge +- 8 kV contact, +- 2,+-4,+-8,+-15 kV air discharged),
# Radiated immunity 80 MHz-2.7 GHz 10 V/m, Magnetic field immunity 50, 60 Hz - 30 A/m.
# Warranty
# Warranty period is covered by a two-year from the day of purchase.
# Date of purchase: _____________
# The limited warranty does not cover:
# • Defects or damage resulting from improper usage, maintenance or storage not included in
# this manual;
# • Storing or shipping items not included with the original product inside the original product
# packaging;
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 22 of 23
# © 2024 Paragit Solutions ApS
# • Defects or damage resulting from unauthorized disassembly, alteration, or maintenance;
# • Damage caused by force majeure such as fire, flood and lightning, etc.
# • The product has exceeded the valid period of the warranty.
# Revision History
# The table below presents the major changes and tasks for this document.
# Version Date Change/Action Author
# 1.0 2024-02-05 Initial Document Mathias Stephensen (MAST)
# 1.1 2024-02-05 Ready Mathias Stephensen (MAST)
# 1.2 2024-02-06 Update Nikola Stojanovic (NIST)
# 1.3 2024-02-06 Update Nikola Stojanovic (NIST)
# 1.3 2024-02-06 TSK-72 Reviewed Nikola Stojanovic (NIST)
# 1.4 2024-02-09 Changed context Mathias Stephensen (MAST)
# 1.5 2024-02-09 Update Mathias Stephensen (MAST)
# 2.0 2024-02-09 Publish Mathias Stephensen (MAST)
# 2.0 2024-03-19 TSK-71 Reviewed Mauricio Carlos Henrich (MAHE)
# 2.1 2024-04-05 Update Nikola Stojanovic (NIST)
# 2.2 2024-04-05 Ready Nikola Stojanovic (NIST)
# 3.0 2024-04-05 Publish Nikola Stojanovic (NIST)
# 3.1 2024-04-05 Update Mathias Stephensen (MAST)
# 3.2 2024-04-05 Update Mathias Stephensen (MAST)
# 3.3 2024-04-05 Ready Mathias Stephensen (MAST)
# 3.3 2024-04-05 TSK-1015 Reviewed Mauricio Carlos Henrich (MAHE)
# 3.3 2024-04-05 TSK-1016 Reviewed Nikola Stojanovic (NIST)
# 4.0 2024-04-05 Publish Nikola Stojanovic (NIST)
# Attached Files
# The table below list the list of files which are attached to this document at the moment of export.
# File Name Upload Date Size SHA256
# Acceptance Tasks
# The table below list the accomplished Acceptance tasks for this document.
# PX Instructions For Use
# Version: 4.0 Status: Published
# Date: 2024-04-05 Confidential Page 23 of 23
# © 2024 Paragit Solutions ApS
# Completion Date Version Completed by Method Description
# Signatures Tasks
# The table below presents the accomplished Signature tasks for this document.
# Completion Date Version Completed by Method Description

# """

# pyperclip.copy(base_prompt)