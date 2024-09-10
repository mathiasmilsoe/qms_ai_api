import json

data = {
    "requirements": [
        {
            "requirement": "Labeling Requirements",
            "reference": "MDR Annex I, Chapter III, Section 23.2",
            "description": "This requirement involves providing complete and accurate labels for the medical device in the languages accepted in the Member States where the device is marketed.",
            "overall_compliance_grade": "PC",
            "detailed_compliance_explanation": "The assessment of the labeling requirements for the ParagitPX medical device reveals a mixed compliance status. The following summarizes the findings across all sub-requirements:\n\n1. **Product Name or Trade Name**: Compliant (C) - The label clearly includes the product name 'ParagitPX', consistent with marketing and documentation.\n\n2. **Intended Purpose**: Partly Compliant (PC) - While the intended purpose is mentioned, it lacks specificity regarding medical applications and user scenarios, which could lead to misuse.\n\n3. **Manufacturer's Name and Address**: Compliant (C) - The manufacturer's details are accurately stated in the EU Declaration of Conformity.\n\n4. **Batch Number or Serial Number**: Partly Compliant (PC) - The label verification evidence does not confirm the presence of a batch or serial number, which is essential for traceability.\n\n5. **Date of Manufacture**: Non-Compliant (NC) - The date of manufacture is missing from the label, which is a critical requirement under the MDR.\n\n6. **Expiry Date**: Non-Compliant (NC) - There is no mention of an expiry date or a statement indicating that there is none, which is required for user safety.\n\n7. **Warnings and Precautions**: Partly Compliant (PC) - Some warnings are present, but they do not comprehensively cover all necessary precautions, particularly regarding contraindications.\n\n8. **Symbols and Safety Information**: Non-Compliant (NC) - The documentation does not demonstrate compliance with ISO 15223-1, as it references obsolete standards and draft documents.\n\n9. **Language Requirements**: Partly Compliant (PC) - While labels are present, there is no explicit evidence confirming translations in all necessary languages for the Member States.\n\nOverall, the labeling documentation for the ParagitPX medical device is partly compliant due to significant gaps in critical areas such as the date of manufacture, expiry date, and compliance with current standards for symbols and safety information.",
            "sub_requirements": [
                {
                    "description": "Ensure the label includes the product name or trade name.",
                    "compliance_grade": "C",
                    "detailed_compliance_explanation": "The label for the ParagitPX medical device clearly includes the product name 'ParagitPX', which is consistent with the name used in marketing and documentation. The validation evidence confirms that all elements of the label are present, readable, and meet the necessary requirements.",
                    "non_conformities": [],
                    "assessment_criteria": "Check if the product name or trade name is present and clear on the label. It should be consistent with the name used in marketing and documentation.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "./PX Annex 06 - Product Verification and Validation/PXS System/PXS Validation/PX LVA240425 Label Validation Evidence v2.0 (Published).pdf",
                        "./PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement  v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "./PX Annex 06 - Product Verification and Validation/PXS System/PXS Validation/PX LVA240425 Label Validation Evidence v2.0 (Published).pdf",
                            "short_name": "PX LVA240425 Label Validation Evidence v2.0 (Published)"
                        },
                        {
                            "path": "./PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement  v2.1 (Draft).pdf",
                            "short_name": "PX S-ST022 The ParagitPX labels"
                        }
                    ],
                    "tasks_list": []
                },
                {
                    "description": "Include the intended purpose of the device.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The intended purpose of the ParagitPX device is described in the document 'PX Intended Purpose v4.0 (Published)'. However, while the document outlines the device's safety features and intended use, it lacks specificity in detailing the exact medical applications and user scenarios, which could lead to potential misuse. For example, it states that the device is intended for external use only but does not specify the conditions or types of patients for whom it is intended. This vagueness could result in improper use or misunderstanding by healthcare providers or patients.",
                    "non_conformities": [
                        {
                            "title": "Lack of Specificity in Intended Use",
                            "description": "The document does not provide a detailed description of the intended medical applications or user scenarios for the device, which is essential to prevent misuse.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf",
                                    "short_name": "PX Intended Purpose v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Verify if the intended purpose of the device is described on the label. It should be specific enough to avoid misuse.",
                    "relevant_documents": [
                        "PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf",
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf",
                            "short_name": "PX Intended Purpose v4.0"
                        },
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Enhance Clarity of Intended Use",
                            "description": "Revise the documentation to include a more detailed description of the intended medical applications and specific user scenarios for the ParagitPX device to ensure clarity and prevent misuse.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf",
                                    "short_name": "PX Intended Purpose v4.0"
                                },
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Provide the manufacturer's name and address.",
                    "compliance_grade": "C",
                    "detailed_compliance_explanation": "The manufacturer's name and address are clearly stated in the EU Declaration of Conformity. The document specifies 'Paragit Neurotech, Grundtvigsvej 6a, 1864 Frederiksberg, Denmark', which is accurate and consistent with official records. This meets the requirements set forth in the MDR.",
                    "non_conformities": [],
                    "assessment_criteria": "Ensure the manufacturer's name and address are clearly stated on the label. This information must be accurate and consistent with official records.",
                    "relevant_documents": [
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "PX Annex 08 - EU Declaration of Conformity/PX EU Declaration of Conformity v2.0 (Published).pdf",
                        "PX Annex 10 - Existing Approvals and Certificates/PX GS1 Company prefix Certificate v2.0 (Published)/PX GS1 Company prefix Certificate v2.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "PX Annex 08 - EU Declaration of Conformity/PX EU Declaration of Conformity v2.0 (Published).pdf",
                            "short_name": "PX EU Declaration of Conformity v2.0 (Published)"
                        },
                        {
                            "path": "PX Annex 10 - Existing Approvals and Certificates/PX GS1 Company prefix Certificate v2.0 (Published)/PX GS1 Company prefix Certificate v2.0 (Published).pdf",
                            "short_name": "PX GS1 Company prefix Certificate v2.0 (Published)"
                        }
                    ],
                    "tasks_list": []
                },
                {
                    "description": "Include batch number or serial number for traceability.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The label verification evidence indicates that the label contents are credible and compliant with standard requirements. However, it does not explicitly confirm the presence of a batch number or serial number on the label, which is essential for traceability as per MDR requirements. The absence of these identifiers could hinder the ability to trace the device back through the manufacturing process, which is a critical aspect of device safety and regulatory compliance.",
                    "non_conformities": [
                        {
                            "title": "Missing Batch Number or Serial Number",
                            "description": "The label does not include a batch number or serial number, which is required for traceability under MDR.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Check if a batch number or serial number is present on the label for traceability. It should allow the device to be traced back through the manufacturing process.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "./PX Annex 10 - Existing Approvals and Certificates/PX GS1 Company prefix Certificate v2.0 (Published)/PX GS1 Company prefix Certificate v2.0 (Published).pdf",
                        "./PX Annex 06 - Product Verification and Validation/PXS System/PX Design Verification/PX LVE240424 Label Verification Evidence v2.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "./PX Annex 10 - Existing Approvals and Certificates/PX GS1 Company prefix Certificate v2.0 (Published)/PX GS1 Company prefix Certificate v2.0 (Published).pdf",
                            "short_name": "PX GS1 Company prefix Certificate v2.0 (Published)"
                        },
                        {
                            "path": "./PX Annex 06 - Product Verification and Validation/PXS System/PX Design Verification/PX LVE240424 Label Verification Evidence v2.0 (Published).pdf",
                            "short_name": "PX LVE240424 Label Verification Evidence v2.0 (Published)"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Add Batch Number or Serial Number to Label",
                            "description": "Update the product label to include a batch number or serial number to ensure traceability as required by MDR.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "State the date of manufacture.",
                    "compliance_grade": "NC",
                    "detailed_compliance_explanation": "The technical documentation does not include the date of manufacture on the product label. According to the MDR, the date of manufacture must be clearly stated in an unambiguous and standardized format. This omission could lead to difficulties in traceability and accountability, especially in the event of a product recall or adverse event reporting.",
                    "non_conformities": [
                        {
                            "title": "Missing Date of Manufacture",
                            "description": "The product label does not specify the date of manufacture, which is a requirement under the MDR.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Verify that the date of manufacture is included on the label. The date should be in a format that is unambiguous and standardized.",
                    "relevant_documents": [
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "PX Annex 08 - EU Declaration of Conformity v2.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "PX Annex 08 - EU Declaration of Conformity v2.0 (Published).pdf",
                            "short_name": "EU Declaration of Conformity v2.0"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Add Date of Manufacture to Product Label",
                            "description": "Revise the product label to include the date of manufacture in a clear and standardized format as per MDR requirements.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Provide the expiry date or a statement indicating no expiry date if applicable.",
                    "compliance_grade": "NC",
                    "detailed_compliance_explanation": "The reviewed documents do not contain any information regarding the expiry date of the Paragit PX medical device. Specifically, the 'PX Instructions For Use v4.0' and 'PX Product Label v2.1 (Draft)' lack any mention of an expiry date or a statement indicating that there is no expiry date. This is a critical non-compliance as per the MDR requirements, which mandate that such information must be clearly provided to ensure user safety and proper usage of the device.",
                    "non_conformities": [
                        {
                            "title": "Missing Expiry Date Information",
                            "description": "The documents do not provide an expiry date or a statement indicating that there is no expiry date for the Paragit PX medical device, which is a requirement under the MDR.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                },
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Ensure the expiry date is included, or a statement indicating that there is no expiry date if applicable. The date should be clear and in an accepted format.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "./PX Annex 08 - EU Declaration of Conformity/PX EU Declaration of Conformity v2.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "./PX Annex 08 - EU Declaration of Conformity/PX EU Declaration of Conformity v2.0 (Published).pdf",
                            "short_name": "PX EU Declaration of Conformity v2.0"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Add Expiry Date Information",
                            "description": "Revise the 'PX Instructions For Use' and 'PX Product Label' documents to include the expiry date of the Paragit PX medical device or a statement indicating that there is no expiry date. Ensure that the information is clear and in an accepted format.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                },
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Include necessary warnings and precautions.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The documentation reviewed includes the PX Product Label and Instructions for Use, which contain some warnings and precautions. However, they lack comprehensive coverage of all necessary warnings that should be conspicuous and clear. For instance, the label does not adequately address potential risks associated with improper use or specific contraindications that may arise during the use of the device. This partial compliance indicates that while some warnings are present, they do not fully meet the requirements set forth in the MDR.",
                    "non_conformities": [
                        {
                            "title": "Insufficient Warnings on Product Label",
                            "description": "The product label does not include all necessary warnings and precautions, particularly regarding contraindications and potential misuse of the device.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ]
                        },
                        {
                            "title": "Lack of Clarity in Instructions for Use",
                            "description": "The Instructions for Use do not clearly articulate the necessary precautions that users must take to ensure safe operation of the device.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0 (Published)"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Check if all necessary warnings and precautions are included on the label. They should be conspicuous and clear.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0 (Published)"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0 (Published)"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Revise Product Label",
                            "description": "Update the product label to include all necessary warnings and precautions, ensuring they are clear and conspicuous to users.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ],
                            "user_input": ""
                        },
                        {
                            "title": "Enhance Instructions for Use",
                            "description": "Revise the Instructions for Use to include detailed precautions and warnings related to the safe operation of the device.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0 (Published)"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Verify that symbols and safety information are correctly used and internationally recognized.",
                    "compliance_grade": "NC",
                    "detailed_compliance_explanation": "The documentation provided does not adequately demonstrate compliance with ISO 15223-1, which is essential for ensuring that symbols and safety information are correctly used and internationally recognized. Specifically, the document 'PX S-ST019 The system shall comply with ISO 15223-1-2021 v3.0 (Obsolete)' is marked as obsolete, indicating that it may not reflect the current standards required for compliance. Furthermore, the document 'PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement v2.1 (Draft)' is still in draft form and has not been finalized, which raises concerns about its validity and applicability. Without adherence to the latest standards, there is a significant risk that the symbols and safety information may not be understood correctly by users, potentially leading to misuse or safety issues.",
                    "non_conformities": [
                        {
                            "title": "Obsolete Standard Compliance",
                            "description": "The document PX S-ST019 is based on an obsolete version of ISO 15223-1, which may not meet current regulatory requirements for symbols and safety information.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST019 The system shall comply with ISO 15223-1-2021 v3.0 (Obsolete).pdf",
                                    "short_name": "PX S-ST019"
                                }
                            ]
                        },
                        {
                            "title": "Draft Labeling Standards",
                            "description": "The document PX S-ST022 is a draft and has not been finalized, which raises concerns about its applicability and compliance with the required standards.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement v2.1 (Draft).pdf",
                                    "short_name": "PX S-ST022"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Ensure that symbols and safety information are appropriately used and are clearly understood. Symbols should comply with ISO 15223-1.",
                    "relevant_documents": [
                        "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST019 The system shall comply with ISO 15223-1-2021 v3.0 (Obsolete).pdf",
                        "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement  v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST019 The system shall comply with ISO 15223-1-2021 v3.0 (Obsolete).pdf",
                            "short_name": "PX S-ST019"
                        },
                        {
                            "path": "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement v2.1 (Draft).pdf",
                            "short_name": "PX S-ST022"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Update Compliance Documentation",
                            "description": "Revise the compliance documentation to ensure that it references the most current version of ISO 15223-1 and reflects the applicable standards for symbols and safety information.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST019 The system shall comply with ISO 15223-1-2021 v3.0 (Obsolete).pdf",
                                    "short_name": "PX S-ST019"
                                }
                            ],
                            "user_input": ""
                        },
                        {
                            "title": "Finalize Labeling Standards",
                            "description": "Complete the draft document PX S-ST022 and ensure that it adheres to the finalized standards for labeling and safety information.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 03 - Design And Manufacturing Information/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement v2.1 (Draft).pdf",
                                    "short_name": "PX S-ST022"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Ensure the labels are provided in the languages accepted in the Member States where the device is marketed.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The assessment of the documentation indicates that while the labels are present and readable, there is no explicit evidence provided that confirms the availability of translations in all necessary languages for the Member States where the device is marketed. The label validation evidence does not specify the languages included, which raises concerns about compliance with the MDR requirements for multilingual labeling. Therefore, the compliance status is partly compliant due to potential missing translations.",
                    "non_conformities": [
                        {
                            "title": "Missing Language Translations",
                            "description": "The documentation does not confirm that the labels are available in all necessary languages required by the Member States where the device is marketed. This could lead to non-compliance with MDR requirements regarding user information accessibility.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                },
                                {
                                    "path": "./PX Annex 06 - Product Verification and Validation/PXS System/PXS Validation/PX LVA240425 Label Validation Evidence v2.0 (Published).pdf",
                                    "short_name": "PX LVA240425 Label Validation Evidence v2.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Verify if labels are available in all necessary languages. If labels are available in the required languages, it is compliant. If some translations are missing or incorrect, it is partly compliant. If no translations are provided, it is non-compliant.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "./PX Annex 06 - Product Verification and Validation/PXS System/PXS Validation/PX LVA240425 Label Validation Evidence v2.0 (Published).pdf",
                        "./PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement  v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "./PX Annex 06 - Product Verification and Validation/PXS System/PXS Validation/PX LVA240425 Label Validation Evidence v2.0 (Published).pdf",
                            "short_name": "PX LVA240425 Label Validation Evidence v2.0"
                        },
                        {
                            "path": "./PX Annex 03 - Design And Manufacturing Information/PX Design & Development Input/PXS System Design & Development Input/PXS Design Input /PXS Standards/PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement  v2.1 (Draft).pdf",
                            "short_name": "PX S-ST022 The ParagitPX labels shall adhere to the standards outlined in this requirement v2.1 (Draft)"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Verify Language Translations",
                            "description": "Conduct a review of the product labels to ensure that translations are provided in all necessary languages as required by the Member States where the device is marketed. Document the languages included and ensure compliance with MDR requirements.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ],
                            "user_input": ""
                        },
                        {
                            "title": "Update Label Validation Evidence",
                            "description": "Revise the label validation evidence to explicitly state the languages in which the labels are provided. Ensure that this information is clear and accessible for compliance verification.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 06 - Product Verification and Validation/PXS System/PXS Validation/PX LVA240425 Label Validation Evidence v2.0 (Published).pdf",
                                    "short_name": "PX LVA240425 Label Validation Evidence v2.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                }
            ]
        },
        {
            "requirement": "Instructions for Use (IFU) Requirements",
            "reference": "MDR Annex I, Chapter III, Section 23.4 and 23.4(h)",
            "description": "This requirement mandates comprehensive instructions for use of the device, ensuring user safety and effective usage.",
            "overall_compliance_grade": "PC",
            "detailed_compliance_explanation": "The overall compliance grade for the Instructions for Use (IFU) requirements is partly compliant (PC). This assessment is based on the evaluation of several sub-requirements:\n\n1. **Detailed Instructions for Safe and Effective Use**: The documentation provides essential information but lacks clarity in certain areas, particularly regarding the reuse of the Paragit Sleeve (PS). This gap in detail could lead to misunderstandings, resulting in a partly compliant status.\n\n2. **Coverage of Hazards and Precautionary Measures**: While safety warnings are included, not all potential hazards are addressed, such as environmental factors and user errors. This incomplete coverage also results in a partly compliant grade.\n\n3. **Instructions in Required Languages**: The instructions are available in English, but there is no confirmation of translations into all necessary languages for the Member States. This uncertainty leads to a partly compliant status.\n\n4. **Illustrations or Diagrams**: Some illustrations are present, but they lack sufficient detail and clarity, which may hinder user understanding. Therefore, this sub-requirement is also graded as partly compliant.\n\n5. **Detailed Information on Installation, Use, and Maintenance**: The documentation provides a general overview but lacks comprehensive step-by-step instructions, resulting in a partly compliant grade.\n\n6. **Troubleshooting Information**: This is a significant gap, as no troubleshooting information is provided, leading to a non-compliant status for this sub-requirement.\n\n7. **Contact Information for Technical Support**: This requirement is fully met, as accurate and accessible contact information is provided, resulting in a compliant grade.\n\nIn summary, the documentation meets some requirements adequately but falls short in critical areas, particularly in troubleshooting and detailed instructions, leading to an overall classification of partly compliant.",
            "sub_requirements": [
                {
                    "description": "Include detailed instructions for the safe and effective use of the device.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The 'PX Instructions For Use v4.0' document provides a comprehensive overview of the device's components, intended use, safety warnings, and cautions. However, while it includes essential information, some instructions could be clearer or more detailed. For instance, the document mentions that the Paragit Sleeve (PS) should not be reused across patients but does not elaborate on the cleaning procedures or specific risks associated with improper reuse. This lack of detail may lead to misunderstandings or misuse, thus making the compliance partly compliant rather than fully compliant.",
                    "non_conformities": [
                        {
                            "title": "Insufficient Reuse Instructions",
                            "description": "The instructions do not provide detailed cleaning procedures or risks associated with the reuse of the Paragit Sleeve (PS), which could lead to improper use and potential patient safety issues.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Check if detailed instructions for safe and effective use are included. If instructions are comprehensive and clear, it is compliant. If instructions are vague or incomplete, it is partly compliant. If no instructions are provided, it is non-compliant.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Enhance Reuse Instructions",
                            "description": "Provide detailed cleaning procedures and associated risks for the Paragit Sleeve (PS) to ensure safe reuse and prevent potential patient safety issues.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Ensure the instructions cover all potential hazards and precautionary measures.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The 'PX Instructions For Use v4.0' document includes a section on safety warnings and cautions, indicating necessary precautions when operating the device. However, while some hazards are addressed, not all potential hazards are comprehensively covered. For instance, specific environmental conditions or user errors that could lead to device malfunction are not mentioned. This partial coverage results in a partly compliant status.",
                    "non_conformities": [
                        {
                            "title": "Incomplete Hazard Coverage",
                            "description": "The instructions do not address all potential hazards associated with the device, such as environmental factors that may affect performance and user errors that could lead to misuse.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Verify that all potential hazards and precautionary measures are addressed in the instructions. If hazards and precautions are comprehensively covered, it is compliant. If some hazards or precautions are missing or unclear, it is partly compliant. If no hazards or precautions are provided, it is non-compliant.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Enhance Hazard Coverage in Instructions",
                            "description": "Review and update the 'PX Instructions For Use' to include all potential hazards, including environmental factors and user errors that could lead to device malfunction. Ensure that all precautionary measures are clearly articulated.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Provide instructions in the languages accepted in the Member States where the device is marketed.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The documentation contains instructions for use in English, but it is unclear if translations into all required languages for the Member States are provided. The 'PX Instructions For Use v4.0' document includes symbols and safety warnings but does not specify if translations are available for other languages. The 'PX Packaging Instruction v3.0' and 'PX Product Label v2.1' documents also do not confirm the presence of translations in the necessary languages. Therefore, the compliance status is partly compliant due to the lack of clarity regarding language availability.",
                    "non_conformities": [
                        {
                            "title": "Missing Translations",
                            "description": "The instructions for use do not specify if they are available in all necessary languages for the Member States where the device is marketed. This could lead to user confusion and improper use of the device.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                },
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                                    "short_name": "PX Packaging Instruction v3.0"
                                },
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Ensure that instructions for use are available in all necessary languages. If instructions are available in the required languages, it is compliant. If some translations are missing or incorrect, it is partly compliant. If no translations are provided, it is non-compliant.",
                    "relevant_documents": [
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        },
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Provide Translations",
                            "description": "Ensure that the instructions for use and all relevant documentation are translated into all necessary languages accepted in the Member States where the device is marketed. This includes verifying the accuracy and clarity of translations to prevent misuse of the device.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                },
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                                    "short_name": "PX Packaging Instruction v3.0"
                                },
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Include illustrations or diagrams to aid understanding if necessary.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The technical documentation includes some illustrations and diagrams, particularly in the 'Device Description and Specification' section of the STED document. However, while these illustrations are present, they may not be sufficiently detailed or clear for all users to fully understand the device's components and functionality. For instance, the diagrams depicting the key components of the ParagitPX are mentioned but not elaborated upon in terms of clarity and comprehensiveness. Therefore, the documentation is partly compliant as it provides some visual aids but lacks the necessary detail to ensure full understanding.",
                    "non_conformities": [
                        {
                            "title": "Insufficient Clarity of Illustrations",
                            "description": "The illustrations provided in the documentation do not adequately convey the necessary details about the device's components and their functions. This could lead to misunderstandings about the device's operation and safety features.",
                            "associated_documents": [
                                {
                                    "path": "./PX Summary of Technical Documentation (STED) v2.0 (Published).pdf",
                                    "short_name": "PX STED"
                                },
                                {
                                    "path": "./PX Annex 01 - Device Description and Specification/PX Product Classification v4.0 (Published).pdf",
                                    "short_name": "PX Product Classification"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Check if illustrations or diagrams are provided to aid understanding when necessary. If illustrations are comprehensive and clear, it is compliant. If illustrations are vague or unclear, it is partly compliant. If no illustrations are provided when needed, it is non-compliant.",
                    "relevant_documents": [
                        "./PX Summary of Technical Documentation (STED) v2.0 (Published).pdf",
                        "./PX Annex 01 - Device Description and Specification/PX Product Classification v4.0 (Published).pdf",
                        "./PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf",
                        "./PX Annex 04 - General Safety And Performance Requirements/PX 2024-04-01 List of Applicable Standards and Regulations v2.0 (Published).pdf",
                        "./PX Annex 04 - General Safety And Performance Requirements/PX GSPR Checklist Final v2.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Summary of Technical Documentation (STED) v2.0 (Published).pdf",
                            "short_name": "PX STED"
                        },
                        {
                            "path": "./PX Annex 01 - Device Description and Specification/PX Product Classification v4.0 (Published).pdf",
                            "short_name": "PX Product Classification"
                        },
                        {
                            "path": "./PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf",
                            "short_name": "PX Intended Purpose"
                        },
                        {
                            "path": "./PX Annex 04 - General Safety And Performance Requirements/PX 2024-04-01 List of Applicable Standards and Regulations v2.0 (Published).pdf",
                            "short_name": "PX Applicable Standards"
                        },
                        {
                            "path": "./PX Annex 04 - General Safety And Performance Requirements/PX GSPR Checklist Final v2.0 (Published).pdf",
                            "short_name": "PX GSPR Checklist"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Enhance Clarity of Illustrations",
                            "description": "Revise the existing illustrations and diagrams to ensure they provide clear and comprehensive information about the device's components and their functions. This may include adding labels, annotations, and additional diagrams if necessary.",
                            "associated_documents": [
                                {
                                    "path": "./PX Summary of Technical Documentation (STED) v2.0 (Published).pdf",
                                    "short_name": "PX STED"
                                },
                                {
                                    "path": "./PX Annex 01 - Device Description and Specification/PX Product Classification v4.0 (Published).pdf",
                                    "short_name": "PX Product Classification"
                                }
                            ],
                            "user_input": ""
                        },
                        {
                            "title": "Conduct User Testing for Clarity",
                            "description": "Perform user testing with the revised illustrations to gather feedback on their clarity and effectiveness in conveying the necessary information about the device. Adjust the illustrations based on user feedback.",
                            "associated_documents": [
                                {
                                    "path": "./PX Summary of Technical Documentation (STED) v2.0 (Published).pdf",
                                    "short_name": "PX STED"
                                },
                                {
                                    "path": "./PX Annex 01 - Device Description and Specification/PX Intended Purpose v4.0 (Published).pdf",
                                    "short_name": "PX Intended Purpose"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Provide detailed information on how to install, use, and maintain the device.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The documentation provides a general overview of the installation, usage, and maintenance of the ParagitPX device. However, it lacks comprehensive step-by-step instructions that would ensure users can follow them easily. For example, while the 'PX Instructions For Use v4.0' document outlines safety warnings and cautions, it does not provide detailed procedures for installation or maintenance, which are critical for user safety and device performance. Additionally, the instructions should be more user-friendly, possibly including diagrams or flowcharts to enhance understanding.",
                    "non_conformities": [
                        {
                            "title": "Lack of Detailed Installation Instructions",
                            "description": "The instructions do not provide a clear, step-by-step guide for installing the device, which may lead to improper setup and potential safety risks.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        },
                        {
                            "title": "Insufficient Maintenance Guidelines",
                            "description": "The maintenance section lacks specific procedures and schedules for regular checks and servicing of the device, which could result in decreased performance over time.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Verify that the IFU include detailed steps for installation, use, and maintenance. Instructions should be easy to follow and comprehensive.",
                    "relevant_documents": [
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Develop Comprehensive Installation Instructions",
                            "description": "Create detailed, step-by-step installation instructions for the ParagitPX device, including diagrams and troubleshooting tips to assist users in proper setup.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        },
                        {
                            "title": "Enhance Maintenance Guidelines",
                            "description": "Revise the maintenance section to include specific procedures, schedules, and checklists for regular maintenance of the device to ensure optimal performance.",
                            "associated_documents": [
                                {
                                    "path": "PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Include troubleshooting information for common problems and their solutions.",
                    "compliance_grade": "NC",
                    "detailed_compliance_explanation": "The document does not provide any troubleshooting information for common problems or their solutions. This is a critical gap as it does not meet the requirement for users to have access to practical and effective solutions for issues they may encounter while using the device. Without this information, users may face difficulties in operating the device safely and effectively, potentially leading to misuse or adverse events.",
                    "non_conformities": [
                        {
                            "title": "Lack of Troubleshooting Information",
                            "description": "The document fails to include any troubleshooting information for common problems that users may encounter with the device. This omission is significant as it does not provide users with the necessary guidance to resolve issues effectively, which could lead to improper use or safety risks.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Ensure that troubleshooting information for common issues is present and clear. Solutions should be practical and effective.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Develop Troubleshooting Section",
                            "description": "Create a dedicated section in the Instructions for Use that outlines common problems users may encounter with the device, along with practical and effective solutions for each issue. This section should be clear, concise, and easy to understand to ensure users can quickly find the information they need.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Provide contact information for technical support or customer service.",
                    "compliance_grade": "C",
                    "detailed_compliance_explanation": "The documentation includes accurate and accessible contact information for technical support or customer service. In the 'PX Instructions For Use v4.0', the contact information for Paragit Neurotech ApS is provided clearly at the beginning of the manual, ensuring users can easily reach out for assistance.",
                    "non_conformities": [],
                    "assessment_criteria": "Check if contact information for technical support or customer service is included. The contact details should be accurate and accessible.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1"
                        }
                    ],
                    "tasks_list": []
                }
            ]
        },
        {
            "requirement": "Electronic Instructions for Use (eIFU)",
            "reference": "Regulation (EU) 207/2012",
            "description": "This requirement pertains to providing electronic instructions for use as an alternative to paper instructions, ensuring accessibility and user convenience.",
            "overall_compliance_grade": "PC",
            "detailed_compliance_explanation": "The assessment of the electronic Instructions for Use (eIFU) for the paragitPX medical device reveals several areas of compliance and non-compliance with the MDR requirements. Overall, the eIFU is partly compliant due to the following findings:\n\n1. **Accessibility and User-Friendliness (PC)**: The eIFU is accessible but could be improved in terms of usability. The language used is somewhat technical, which may confuse users. Additionally, there is no direct link or QR code provided in the packaging or product label to access the eIFU, limiting user access.\n\n2. **Availability of Access Information (PC)**: While some information regarding accessing the eIFU is provided, it lacks clarity and comprehensiveness. Users may not have explicit guidance on how to find the eIFU, which is essential for compliance.\n\n3. **User Notification Mechanism (NC)**: There is a significant gap in the documentation regarding mechanisms to inform users about updates to the eIFU. The absence of a defined process for user notifications leads to non-compliance with MDR requirements.\n\n4. **Request System for Paper IFU (NC)**: The documentation does not specify a system for users to request paper versions of the IFU. This is a critical gap as it does not comply with the requirement that the process should be easy and free of charge.\n\n5. **Format Accessibility (PC)**: The eIFU is provided in PDF format, which is generally accessible on various devices. However, there is no mention of compatibility with specific platforms or alternative formats that may enhance accessibility, limiting its compliance.\n\nIn summary, while there are some compliant aspects of the eIFU, the significant non-compliance in user notification mechanisms and the request system for paper IFUs, along with the partly compliant status in accessibility and format, result in an overall compliance grade of 'PC'.",
            "sub_requirements": [
                {
                    "description": "Ensure that eIFU are easily accessible and user-friendly.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The eIFU provided in the 'PX Instructions For Use v4.0' document is accessible and contains necessary information. However, the usability could be improved by simplifying the language and enhancing the layout for better readability. The packaging instructions and product label documents do not provide direct access to the eIFU, which may hinder user accessibility. Therefore, while the eIFU is present, there are areas for improvement in user-friendliness.",
                    "non_conformities": [
                        {
                            "title": "Usability Issues in eIFU",
                            "description": "The language used in the eIFU may be too technical for some users, which could lead to misunderstandings about the device's operation and safety precautions.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        },
                        {
                            "title": "Lack of Direct Access to eIFU",
                            "description": "The packaging instructions and product label do not provide a direct link or QR code to access the eIFU, which may limit user access to important information.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                                    "short_name": "PX Packaging Instruction v3.0"
                                },
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Check if eIFU are accessible and user-friendly. If eIFU are easily accessible and comprehensible, it is compliant. If accessibility or usability issues are present, it is partly compliant. If eIFU are not provided, it is non-compliant.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Simplify Language in eIFU",
                            "description": "Revise the eIFU to use simpler language and clearer instructions to enhance user understanding and accessibility.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        },
                        {
                            "title": "Add Direct Access to eIFU",
                            "description": "Include a QR code or direct link on the packaging and product label that leads to the eIFU for easy access by users.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                                    "short_name": "PX Packaging Instruction v3.0"
                                },
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Verify compliance with requirements for availability, including providing information about accessing eIFU.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The documentation provides some information about accessing the electronic Instructions for Use (eIFU), but it lacks clarity and comprehensiveness. For instance, while the 'PX Instructions For Use' document mentions the need to report serious incidents, it does not explicitly detail how users can access the eIFU or where it can be found. This vagueness leads to a partly compliant status as users may not have clear guidance on accessing necessary information.",
                    "non_conformities": [
                        {
                            "title": "Lack of Clear Access Information for eIFU",
                            "description": "The documentation does not provide explicit instructions on how users can access the electronic Instructions for Use (eIFU). This is critical for user safety and compliance with MDR requirements.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Ensure that users are given clear information on accessing eIFU. If access information is clear and comprehensive, it is compliant. If access information is vague or incomplete, it is partly compliant. If no access information is provided, it is non-compliant.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Enhance eIFU Access Information",
                            "description": "Revise the 'PX Instructions For Use' document to include clear and comprehensive instructions on how users can access the electronic Instructions for Use (eIFU). This should include specific URLs, QR codes, or other means of access to ensure users can easily find the information they need.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Include mechanisms for ensuring that users are aware of updates to the eIFU.",
                    "compliance_grade": "NC",
                    "detailed_compliance_explanation": "The reviewed documents do not provide clear mechanisms for informing users about updates to the electronic Instructions for Use (eIFU). Specifically, the 'PX Instructions For Use v4.0' does not mention any notification system for updates, and the 'PX Product Label v2.1 (Draft)' lacks information on how users will be informed of changes. This absence of a defined process for user notification leads to a non-compliance status as per the MDR requirements.",
                    "non_conformities": [
                        {
                            "title": "Lack of User Notification Mechanism",
                            "description": "The documentation does not specify any mechanisms for notifying users about updates to the eIFU, which is critical for ensuring that users have access to the most current information regarding the device's use and safety.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                },
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Check if mechanisms are in place to inform users about updates to eIFU. If update mechanisms are clear and functional, it is compliant. If update mechanisms are unclear or unreliable, it is partly compliant. If no update mechanisms are provided, it is non-compliant.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                        "./PX Annex 09 - Technical Documentation on Post-market Surveillance/PX PMSP230220-01 PMS Plan v3.0 (Published).pdf",
                        "./PX Annex 09 - Technical Documentation on Post-market Surveillance/PX PMCF240220-01 PMCF Plan v3.0 (Published).pdf",
                        "./PX Annex 08 - EU Declaration of Conformity/PX EU Declaration of Conformity v2.0 (Published).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1 (Draft)"
                        },
                        {
                            "path": "./PX Annex 09 - Technical Documentation on Post-market Surveillance/PX PMSP230220-01 PMS Plan v3.0 (Published).pdf",
                            "short_name": "PX PMSP230220-01 PMS Plan v3.0"
                        },
                        {
                            "path": "./PX Annex 09 - Technical Documentation on Post-market Surveillance/PX PMCF240220-01 PMCF Plan v3.0 (Published).pdf",
                            "short_name": "PX PMCF240220-01 PMCF Plan v3.0"
                        },
                        {
                            "path": "./PX Annex 08 - EU Declaration of Conformity/PX EU Declaration of Conformity v2.0 (Published).pdf",
                            "short_name": "PX EU Declaration of Conformity v2.0"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Establish User Notification Mechanism",
                            "description": "Develop and implement a clear mechanism for notifying users about updates to the eIFU. This could include email notifications, alerts on the manufacturer's website, or updates through a mobile application.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                },
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                                    "short_name": "PX Product Label v2.1 (Draft)"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Provide a system for users to request paper versions of the IFU if needed.",
                    "compliance_grade": "NC",
                    "detailed_compliance_explanation": "The documentation does not provide a clear system or process for users to request paper versions of the Instructions for Use (IFU). While the IFU mentions safety warnings and cautions, it lacks explicit instructions or contact information for users to request paper copies. This is a significant gap as it does not comply with the requirement that the process should be easy and free of charge.",
                    "non_conformities": [
                        {
                            "title": "Lack of Request System for Paper IFU",
                            "description": "The documentation does not specify a system for users to request paper versions of the IFU, which is a requirement under the MDR. This could lead to user confusion and hinder access to necessary information for safe device operation.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Ensure that there is a system in place for users to request paper versions of the IFU. The process should be easy and free of charge.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Establish a Request System for Paper IFU",
                            "description": "Develop and implement a clear and accessible system for users to request paper versions of the Instructions for Use (IFU). This should include contact information, methods of request (e.g., phone, email), and ensure that the process is free of charge.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                },
                {
                    "description": "Ensure that the eIFU are in a format that is accessible on a wide range of devices and platforms.",
                    "compliance_grade": "PC",
                    "detailed_compliance_explanation": "The eIFU provided in the 'PX Instructions For Use v4.0' document is in PDF format, which is generally accessible on various devices such as computers, tablets, and smartphones. However, there is no explicit mention of compatibility with specific platforms or alternative formats that may enhance accessibility, such as HTML or mobile-friendly formats. This limits its compliance as it may not be fully accessible to all users, particularly those relying on assistive technologies.",
                    "non_conformities": [
                        {
                            "title": "Limited Format Accessibility",
                            "description": "The eIFU is only available in PDF format, which may not be compatible with all devices or assistive technologies, potentially hindering access for some users.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ]
                        }
                    ],
                    "assessment_criteria": "Check if the eIFU are provided in formats that are accessible on various devices (e.g., computers, tablets, smartphones) and platforms. If the formats are compatible and readable, it is compliant.",
                    "relevant_documents": [
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                        "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf"
                    ],
                    "checked_documents": [
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                            "short_name": "PX Instructions For Use v4.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Packaging Instruction v3.0 (Published)/PX Packaging Instruction v3.0 (Published).pdf",
                            "short_name": "PX Packaging Instruction v3.0"
                        },
                        {
                            "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Product Label v2.1 (Draft)/PX Product Label v2.1 (Draft).pdf",
                            "short_name": "PX Product Label v2.1"
                        }
                    ],
                    "tasks_list": [
                        {
                            "title": "Provide Alternative Formats for eIFU",
                            "description": "Develop and provide the eIFU in additional formats such as HTML or mobile-friendly versions to ensure compatibility with a wider range of devices and assistive technologies.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        },
                        {
                            "title": "Conduct Accessibility Testing",
                            "description": "Perform accessibility testing of the eIFU on various devices and platforms to ensure compliance with accessibility standards and guidelines.",
                            "associated_documents": [
                                {
                                    "path": "./PX Annex 02 - Information To Be Supplied By The Manufacturer/PX Instructions For Use v4.0 (Published).pdf",
                                    "short_name": "PX Instructions For Use v4.0"
                                }
                            ],
                            "user_input": ""
                        }
                    ]
                }
            ]
        }
    ]
}

def get_unique_documents(data):
    checked_documents_set = set()

    # Function to normalize document paths by removing leading './'
    def normalize_path(doc_path):
        return doc_path.lstrip('./')

    # Iterate through the requirements and sub-requirements
    for requirement in data['requirements']:
        # Check in sub-requirements
        for sub_req in requirement.get('sub_requirements', []):
            checked_docs = sub_req.get('checked_documents', [])
            for doc in checked_docs:
                # Normalize the document path and create a full document object
                normalized_doc = {**doc, 'path': normalize_path(doc['path'])}
                # Add the JSON stringified version to the set to ensure uniqueness
                checked_documents_set.add(json.dumps(normalized_doc, sort_keys=True))
        
        # Check in main requirement
        checked_docs = requirement.get('checked_documents', [])
        for doc in checked_docs:
            normalized_doc = {**doc, 'path': normalize_path(doc['path'])}
            checked_documents_set.add(json.dumps(normalized_doc, sort_keys=True))

    # Convert back to list of dictionaries
    unique_documents = [json.loads(doc) for doc in checked_documents_set]
    
    return unique_documents

# Get the unique checked documents
unique_documents = get_unique_documents(data)

# Print the results
print(f"Number of unique checked documents: {len(unique_documents)}")
print("Unique checked documents:")
for doc in unique_documents:
    print(doc['path'])