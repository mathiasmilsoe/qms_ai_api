import React, { useEffect, forwardRef, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { message, Collapse, Anchor, Tooltip, Affix, Button, Spin } from "antd"; // Import Tooltip
import { collection, getDocs, doc, getDoc } from "firebase/firestore";
import { db } from "../firebase";
import useStore from "../store";
import TaskProgress from '../components/TaskProgress';
import TaskModal from '../components/TaskModal';
import { ToTopOutlined, MenuUnfoldOutlined, ShrinkOutlined } from '@ant-design/icons'; // Import relevant icons
import "../app.css"
import { LoadingOutlined } from '@ant-design/icons';
import { analytics } from "../firebase"
import { logEvent } from "firebase/analytics";


const { Link } = Anchor; // Destructure Link from Anchor


const ShowReportPage = forwardRef(({ expandedSections, setExpandedSections, collapseAllSections, openAllSections, demoReportId }, ref) => {
    const token = useStore((state) => state.token);
    const userId = useStore((state) => state.userId);
    const setReportData = useStore((state) => state.setReportData);
    const reportData = useStore((state) => state.reportData);
    const navigate = useNavigate();
    const setActiveSection = useStore((state) => state.setActiveSection);
    const setActiveRequirement = useStore((state) => state.setActiveRequirement);
    const setReportAbstract = useStore((state) => state.setReportAbstract);
    const reportAbstract = useStore((state) => state.reportAbstract);

    const isDemoReport = !!demoReportId;
    const [loading, setLoading] = useState(true); // Loading state
    const [percent, setPercent] = useState(0);

    const sectionsRef = useRef([]);
    const requirementsRef = useRef([]);
    const tocRef = useRef(null);

    const [isTaskModalVisible, setIsTaskModalVisible] = useState(false);
    const [taskModalSectionId, setTaskModalSectionId] = useState(null);
    const [taskModalRequirementIndex, setTaskModalRequirementIndex] = useState(null);

    const [activeLink, setActiveLink] = useState(null);

    const openTaskModal = (sectionId = null, requirementIndex = null) => {
        setTaskModalSectionId(sectionId);
        setTaskModalRequirementIndex(requirementIndex);
        setIsTaskModalVisible(true);
    };

    useEffect(() => {
        const sectionOrder = [
            "device_description_and_specification",
            "information_supplied_by_manufacturer",
            "general_safety_and_performance_requirements",
            "design_and_manufacturing_information",
            "benefit_risk_analysis_and_risk_management",
            "product_verification_and_validation",
            "post_market_surveillance",
            "clinical_evaluation",
            "documentation_structure_and_accessibility",
            "compliance_with_common_specifications",
            "usability_and_human_factors_engineering",
            "software_lifecycle_processes",
            "cybersecurity_requirements",
            "supply_chain_traceability"
        ];

        let failledFetch = [];

        const fetchReport = async (reportUserId) => {
            try {
                const sectionsRef = collection(db, "reports", reportUserId, "sections");
                const querySnapshot = await getDocs(sectionsRef);
                let sections = querySnapshot.docs.map((doc) => ({
                    id: doc.id,
                    data: doc.data(),
                }));

                // Sort sections based on the predefined sectionOrder array
                sections = sections.sort((a, b) => {
                    return sectionOrder.indexOf(a.id) - sectionOrder.indexOf(b.id);
                });

                if (!sections || sections.length === 0) {
                    failledFetch.push("report");
                } else {
                    logEvent(analytics, 'fetched_report', {
                        user_id: reportUserId,
                    });
                }

                setReportData(sections);
            } catch (error) {
                failledFetch.push("report");
            }
        };

        const fetchReportAbstract = async (reportUserId) => {
            try {
                const abstractRef = collection(db, "report_abstracts", reportUserId, "abstracts");
                const abstractSnapshot = await getDocs(abstractRef);

                // Convert array of abstracts to object with id as key and data as value
                const abstracts = abstractSnapshot.docs.reduce((acc, doc) => {
                    acc[doc.id] = doc.data();
                    return acc;
                }, {});

                if (!abstracts || Object.keys(abstracts).length === 0) {
                    failledFetch.push("abstracts");
                } else {
                    logEvent(analytics, 'fetched_abstracts', {
                        user_id: reportUserId,
                    });
                }

                setReportAbstract(abstracts);
            } catch (error) {
                failledFetch.push("abstracts");
            }
        };

        const showLoader = () => {
            setLoading(true);
            let progress = 0;
            const interval = setInterval(() => {
                progress += 20;
                setPercent(progress);

                if (progress >= 100) {
                    clearInterval(interval);
                }
            }, 100);
        };

        const fetchData = async (reportUserId) => {
            showLoader(); // Start the loader

            await Promise.all([fetchReport(reportUserId), fetchReportAbstract(reportUserId)]);

            if (failledFetch.length > 0) {
                message.error("Failed to fetch report");
                logEvent(analytics, 'report_fetch_failed', {
                    user_id: reportUserId,
                    content_type: failledFetch,
                });
            }

            setLoading(false); // Stop the loader
        };

        if (isDemoReport) {
            fetchData(demoReportId); // Fetch demo report data
        } else {
            if (!token || !userId) {
                message.error("You must sign in first.");
                navigate(`/signin`);
                return;
            }
            fetchData(userId); // Fetch user report data
        }
    }, [token, userId, setReportData, setReportAbstract, navigate]);


    const formatSectionId = (id) => {
        if (id) {
            return id
                .replace(/_/g, ' ')
                .split(' ')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1))
                .join(' ');
        } else {
            return null;
        }
    };

    const getLabelStyle = (overallCompliance) => {
        if (overallCompliance?.includes('NC')) return 'bg-light-red white';
        if (overallCompliance?.includes('PC')) return 'bg-light-yellow black-70';
        return 'bg-light-green dark-green';
    };

    const getSectionNCsAndTasks = (sectionId) => {
        let tasks = [];
        let nonConformities = [];
        let checkedDocuments = new Set();  // Use Set to ensure uniqueness of paths

        const section = reportData.find(section => section.id === sectionId);

        if (!section) {
            return { tasks, nonConformities, checkedDocuments: Array.from(checkedDocuments) };
        }

        const normalizePath = (path) => path.replace(/^\.\//, '');  // Remove leading "./" from path

        section.data.requirements.forEach(requirement => {
            // Collect tasks from the requirement level
            if (requirement.task_list) {
                tasks = tasks.concat(requirement.task_list);
            }

            // Collect non-conformities from the requirement level
            if (requirement.non_conformities) {
                nonConformities = nonConformities.concat(requirement.non_conformities);
            }

            // Collect checked documents from the requirement level based on path
            if (requirement.checked_documents) {
                requirement.checked_documents.forEach(doc => {
                    checkedDocuments.add(normalizePath(doc.path));  // Only check uniqueness on the normalized path
                });
            }

            // Loop through each sub-requirement and collect tasks, non-conformities, and documents
            if (requirement?.sub_requirements) {
                requirement?.sub_requirements?.forEach(subRequirement => {
                    // Collect tasks from the sub-requirement
                    if (subRequirement.tasks_list) {
                        tasks = tasks.concat(subRequirement.tasks_list);
                    }

                    // Collect non-conformities from the sub-requirement
                    if (subRequirement.non_conformities) {
                        nonConformities = nonConformities.concat(subRequirement.non_conformities);
                    }

                    // Collect checked documents from the sub-requirement based on path
                    if (subRequirement.checked_documents) {
                        subRequirement.checked_documents.forEach(doc => {
                            checkedDocuments.add(normalizePath(doc.path));  // Ensure uniqueness on the normalized path
                        });
                    }
                });
            }
        });

        // Convert checkedDocuments set back to an array of strings (paths)
        const uniqueCheckedDocuments = Array.from(checkedDocuments);

        return {
            tasks,
            nonConformities,
            checkedDocuments: uniqueCheckedDocuments
        };
    };

    const getUniqueCheckedDocuments = (requirement) => {
        let checkedDocuments = new Set();  // Use Set to ensure uniqueness

        const normalizePath = (path) => path.replace(/^\.\//, '');  // Remove leading "./" from path

        // Loop through sub-requirements and collect unique checked documents
        requirement?.sub_requirements?.forEach(subRequirement => {
            subRequirement?.checked_documents?.forEach(doc => {
                checkedDocuments.add(normalizePath(doc.path));  // Normalize and add to Set
            });
        });

        // Convert Set back to an array of strings (paths)
        return Array.from(checkedDocuments);
    };

    const handleCollapseChange = (key) => {
        console.log("!!!", key)
        setExpandedSections(key);
    };


    const handleAnchorClick = (e, targetId, parentSectionId = null) => {
        e.preventDefault();  // Prevent the default anchor behavior initially

        // Update state with expanded sections
        setExpandedSections((prevExpandedSections) => {
            const expandedKeys = [...prevExpandedSections];

            // Check if parent section needs expanding
            if (parentSectionId && !expandedKeys.includes(parentSectionId)) {
                expandedKeys.push(parentSectionId);
            }

            // Check if the target section or requirement needs expanding
            if (!expandedKeys.includes(targetId)) {
                expandedKeys.push(targetId);
            }

            return expandedKeys;
        });

        // Set the active link manually
        setActiveLink(`#${targetId}`);

        // Delay to ensure DOM updates and the section expands
        setTimeout(() => {
            // Find the anchor link corresponding to the targetId
            const anchorLink = document.querySelector(`a[href="#${targetId}"]`);
            if (anchorLink) {
                // Simulate a click
                anchorLink.click();
            }
        }, 100); // Adjust the delay as necessary
    };

    useEffect(() => {
        const reportContentElement = document.querySelector('.report-content');

        console.log("reportelement", reportContentElement)

        const observerOptions = {
            root: null, // relative to the viewport
            rootmargin: "0px 0px 400px 0px",
            threshold: 0.1 // adjust this to determine when an element is considered in view
        };

        const observerCallback = (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    setActiveLink(`#${entry.target.id}`);
                }
            });
        };

        const observer = new IntersectionObserver(observerCallback, observerOptions);

        // Observe all sections and requirements
        const allElements = document.querySelectorAll('[id]');
        allElements.forEach(el => observer.observe(el));

        return () => observer.disconnect(); // Clean up the observer on component unmount
    }, [reportData, expandedSections]);

    const scrollToTop = () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });  // Smoothly scrolls to the top
    };

    const getTotalNCs = (requirement) => {
        let totalNCs = 0;

        requirement?.sub_requirements?.forEach(subRequirement => {
            if (subRequirement?.non_conformities) {
                totalNCs += subRequirement.non_conformities.length;
            }
        });

        return totalNCs;
    };

    if (loading) {
        return (
            <Spin spinning={loading} tip={`Loading ${percent}%`} fullscreen />
        );
    }

    return (

        <div ref={ref} className="flex" style={{ display: 'flex', alignItems: 'flex-start' }}>
            {/* Anchor Sidebar */}
            <Affix offsetTop={67}>
                <div className="bg-white br3 pa3 ml2 mt1 hide-scrollbar" style={{ width: '200px', marginRight: '20px', maxHeight: '100vh', overflowY: 'auto' }}>
                    <div className="mb2 flex justify-center">
                        <Tooltip title="Top the top">
                            <Button onClick={scrollToTop} size={"small"} icon={<ToTopOutlined />} />
                        </Tooltip>
                        <Tooltip className="ml3" title="Open all">
                            <Button onClick={openAllSections} size={"small"} icon={<MenuUnfoldOutlined />} />
                        </Tooltip>
                        <Tooltip className="ml3" title="Collapse all">
                            <Button onClick={collapseAllSections} size={"small"} icon={<ShrinkOutlined />} />
                        </Tooltip>
                    </div>
                    <Anchor getCurrentAnchor={() => activeLink} affix={false}>
                        <Tooltip title="Report Abstract" placement="right">
                            <Link
                                className="f7"
                                href="#report-abstract"
                                title={<div onClick={(e) => handleAnchorClick(e, 'report-abstract')}>Report Abstract</div>}
                            />
                        </Tooltip>
                        {reportData.map((section) => (
                            <Tooltip key={section.id} title={formatSectionId(section.id)} placement="right">
                                <Link
                                    className="f7"
                                    href={`#${section.id}`}
                                    title={<div onClick={(e) => handleAnchorClick(e, section.id)}>{formatSectionId(section.id)}</div>}
                                >
                                    {section.data.requirements.map((requirement, index) => (
                                        <Tooltip key={requirement.requirement} title={requirement.requirement} placement="right">
                                            <Link
                                                href={`#${requirement.requirement}`}
                                                title={
                                                    <div onClick={(e) => handleAnchorClick(e, requirement.requirement, section.id)}>
                                                        {requirement.requirement}
                                                    </div>
                                                }
                                            />
                                        </Tooltip>
                                    ))}
                                </Link>
                            </Tooltip>
                        ))}
                    </Anchor>
                </div>
            </Affix>

            {/* Report Content */}
            <div style={{ flexGrow: 1 }}>
                <TaskModal
                    isVisible={isTaskModalVisible}
                    onClose={() => setIsTaskModalVisible(false)}
                    sectionId={taskModalSectionId}
                    requirementIndex={taskModalRequirementIndex}
                />

                <Collapse ghost bordered={false} expandIconPosition="left" defaultActiveKey={[]} activeKey={expandedSections}>
                    <div id="report-abstract" className="bg-white br3 pa3 ml2 mr2 mt1">
                        <span className="f5 b">Report abstract</span>
                        <div className="mb3">
                            <p className="f7 mb3 lh-copy">{reportAbstract?.report_abstract?.report_abstract}</p>
                        </div>
                    </div>

                    <div>
                        <Collapse ghost bordered={false} onChange={handleCollapseChange} expandIconPosition="left" defaultActiveKey={[]} activeKey={expandedSections}>
                            {reportData.map((section, index) => (
                                <Collapse.Panel
                                    header={<div className="flex justify-between">
                                        <span className="f5 b">{formatSectionId(section.id)}</span>
                                        <div className="flex">
                                            <div className="ml4">
                                                <TaskProgress onOpenModal={openTaskModal} sectionId={section.id} />
                                            </div>
                                            <div className="ml4">
                                                <span className={`ml3 dib ph2 pv1 br2 f7 fw5 ${getLabelStyle("NC")}`}>{getSectionNCsAndTasks(section.id).nonConformities.length} potential NCs</span>
                                            </div>
                                            <div className="ml4">
                                                <span className={`ml3 dib ph2 pv1 br2 f7 fw5 bg-washed-blue ba b--blue blue`}>{getSectionNCsAndTasks(section.id).checkedDocuments.length} documents checked</span>
                                            </div>
                                        </div>
                                    </div>}
                                    key={section.id}
                                    id={section.id}
                                    className="bg-white br3 pa3 ml2 mr2 mt3"
                                >
                                    <div className="mb3">
                                        <div className="f7 mb3 lh-copy">{reportAbstract?.[section.id]?.section_abstract}</div>
                                        <Collapse bordered={false} expandIconPosition="left" defaultActiveKey={[]} activeKey={expandedSections} onChange={handleCollapseChange}>
                                            {section.data.requirements.map((requirement, reqIndex) => (
                                                <Collapse.Panel
                                                    header={<div className="flex items-center justify-between">

                                                        <span className="f6 b " style={{ width: "70%" }}>{requirement.requirement}</span>

                                                        <div className="flex " style={{ width: "30%", height: 25 }}>
                                                            <div className="flex justify-center" style={{ width: "25%" }}><span className="mr4 dib ph2 pv1 br2 f7 fw6 bg-light-red white">{getTotalNCs(requirement)}</span></div>
                                                            <div className="flex justify-center" style={{ width: "25%" }}><span className={`mr4 dib ph2 pv1 br2 f7 fw6 ${getLabelStyle(requirement.overall_compliance_grade)}`}>
                                                                {requirement.overall_compliance_grade}
                                                            </span></div>
                                                            <div className="flex justify-center" style={{ maxWidth: "50%" }}><TaskProgress onOpenModal={openTaskModal} sectionId={section.id} requirementIndex={reqIndex} /></div>
                                                        </div>

                                                    </div>}
                                                    key={`${requirement.requirement}`}
                                                    id={`${requirement.requirement}`}
                                                    className="bg-white br2 pa2 "
                                                >
                                                    <div className="mb3">
                                                        <p className="f7 mb3 lh-copy">
                                                            <span className="b">Description of requirement:</span> {requirement.description}
                                                        </p>
                                                        <p className="f7 mb3 lh-copy">
                                                            <span className="b">Overall assessment:</span> {requirement.short_compliance_explanation}
                                                        </p>

                                                        <Collapse ghost className="bg-washed-blue ba b--blue br2 pa2 mb3" expandIconPosition="left" defaultActiveKey={[]} activeKey={expandedSections} onChange={handleCollapseChange}>
                                                            <Collapse.Panel
                                                                header={<span className="dark-blue fw6 mb2 f7">
                                                                    {getUniqueCheckedDocuments(requirement).length} documents were checked
                                                                </span>}
                                                                key={`checked-documents-${reqIndex}`}
                                                            >
                                                                <div className="ml3">
                                                                    {/* List unique checked documents from sub-requirements */}
                                                                    {getUniqueCheckedDocuments(requirement).map((docPath, index) => (
                                                                        <p key={index} className="dark-blue f7 mb1">• {docPath}</p>
                                                                    ))}
                                                                </div>
                                                            </Collapse.Panel>
                                                        </Collapse>

                                                        <Collapse ghost className="bg-washed-red ba b--dark-red br2 pa2 mb3" expandIconPosition="left" defaultActiveKey={[]} activeKey={expandedSections} onChange={handleCollapseChange}>
                                                            <Collapse.Panel
                                                                header={<span className="dark-red fw6 mb2 f7">
                                                                    {requirement?.sub_requirements?.reduce((total, subReq) => total + (subReq?.non_conformities?.length || 0), 0)} Sources of possible non-conformities
                                                                </span>}
                                                                key={`non-conformities-${reqIndex}`}
                                                            >
                                                                <div className="ml3">
                                                                    {/* Non-conformities at the sub-requirement level */}
                                                                    {requirement?.sub_requirements?.map((subRequirement, subReqIndex) => (
                                                                        subRequirement?.non_conformities?.map((nonConformity, index) => (
                                                                            <p key={`${subReqIndex}-${index}`} className="dark-red f7 mb1">
                                                                                <p className="b">• {nonConformity.title}</p> {nonConformity.description}
                                                                            </p>
                                                                        ))
                                                                    ))}
                                                                </div>
                                                            </Collapse.Panel>
                                                        </Collapse>

                                                        <Collapse size="small" expandIconPosition="left" defaultActiveKey={[]} activeKey={expandedSections} onChange={handleCollapseChange} className="mb3">
                                                            {requirement?.sub_requirements?.map((subRequirement, subReqIndex) => (
                                                                <Collapse.Panel
                                                                    header={<div className="flex items-center ">
                                                                        <span className="mr2 f7 gray">
                                                                            <span>{subRequirement.description}</span>
                                                                        </span>
                                                                        <span className={`ml3 dib ph2 pv1 br2 f7 fw5 ${getLabelStyle(subRequirement.compliance_grade)}`}>
                                                                            {subRequirement.compliance_grade}
                                                                        </span>
                                                                    </div>}
                                                                    key={`${requirement.requirement}-sub-${subReqIndex}`}
                                                                    className="bg-white br2 pa2"
                                                                >
                                                                    <div className="ml3">

                                                                        <p className="mr2 f7 mb2">
                                                                            <span className="b">Assessment:</span> {subRequirement?.detailed_compliance_explanation}
                                                                        </p>


                                                                    </div>
                                                                </Collapse.Panel>
                                                            ))}
                                                        </Collapse>
                                                    </div>
                                                </Collapse.Panel>
                                            ))}
                                        </Collapse>
                                    </div>
                                </Collapse.Panel>
                            ))}
                        </Collapse>
                    </div>
                </Collapse>
            </div>

        </div>
    );
});

export default ShowReportPage;
