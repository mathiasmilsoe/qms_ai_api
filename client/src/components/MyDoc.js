// src/components/MyDoc.js

import React, { useState, useEffect } from 'react';
import { Document, Page, Text, View, StyleSheet, Svg, Path, Link } from '@react-pdf/renderer';

// Define styles for the PDF
const styles = StyleSheet.create({
    page: {
        flexDirection: 'column',
        paddingTop: 60, // Ensure content does not overlap with header
        paddingBottom: 40, // Ensure content does not overlap with footer
        paddingHorizontal: 20,
        position: 'relative', // To allow absolute positioning of header/footer
    },
    header: {
        position: 'absolute',
        top: 10,
        left: 20,
        right: 20,
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        paddingBottom: '10px',
        borderBottom: '1px solid #e0e0e0',
    },
    reportId: {
        fontSize: 9,
        color: 'grey',
        textAlign: 'center',
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    date: {
        fontSize: 9,
        color: 'grey',
        textAlign: 'right',
    },
    footer: {
        position: 'absolute',
        bottom: 10,
        left: 20,
        right: 20,
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between', // Space between text and page number
        fontSize: 9,
        color: 'grey',
        alignItems: 'center', // Align items vertically center
    },
    footerTextLeft: {
        width: 400, // Allow the text to take up available space
    },
    footerTextRight: {
        width: 100, // Fixed width for the page number to avoid overlap
        textAlign: 'right', // Align text to the right
    },
    content: {
        marginTop: 5,
        marginBottom: 5,
        marginLeft: 5,
        marginRight: 5
    },
    section: {
        marginBottom: 10,
    },
    text: {
        fontSize: 12,
    },
    logo: {
        width: 50, // Adjust the size as needed
        height: 'auto',
    },
    svg: {
        width: 100, // Adjust the size as needed        
        height: 'auto',
    },
    section: {
        marginBottom: 10,
    },
    sectionHeader: {
        fontSize: 16,
        fontWeight: 'bold',
    },
    sectionContainer: {
        paddingBottom: 10,  // Add padding to the section container        
        marginBottom: 20,
        borderBottom: '1px solid #e0e0e0'
    },
    requirementHeader: {
        fontSize: 12,
        fontWeight: 'extraBold',
        marginBottom: 10,
    },
    requirementDescription: {
        fontSize: 10,
        marginBottom: 15,
        lineHeight: 1.5
    },
    tocHeader: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    tocItem: {
        fontSize: 12,
        marginBottom: 10,
        color: 'black',
        textDecoration: 'none',
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    tocSection: {
        fontSize: 12,
        fontWeight: 'bold',
    },
    tocRequirement: {
        fontSize: 10,
        color: 'grey',
    },
    label: { marginLeft: 10, padding: '2px 4px', borderRadius: 3, fontSize: 10, fontWeight: 'bold', alignSelf: 'flex-start', },
    labelNC: { color: '#D8000C', backgroundColor: '#FFD2D2' },
    labelPC: { color: '#9F6000', backgroundColor: '#FEEFB3' },
    labelC: { color: '#4F8A10', backgroundColor: '#DFF2BF' },
    requirementHeaderContainer: { display: 'flex', flexDirection: 'row', justifyContent: 'flex-start', alignItems: 'center', marginBottom: 10, },
    boldText: { fontWeight: 'bold', },
    checkedDocumentsContainer: { backgroundColor: '#e0f3ff', borderColor: '#0074cc', borderWidth: 1, borderRadius: 3, padding: 5 },
    checkedDocumentsText: { color: '#0074cc', fontWeight: 'bold', marginBottom: 5, fontSize: 10 },
    checkedDocumentsList: { marginLeft: 10, },
    checkedDocumentsItem: { color: '#0074cc', fontSize: 10, marginBottom: 2, },
    nonConformitiesContainer: {
        backgroundColor: '#ffe0e0', // Light red background
        borderColor: '#cc0000', // Red border
        borderWidth: 1,
        borderRadius: 3,
        padding: 5,
        marginTop: 10,
    },
    nonConformitiesText: {
        color: '#cc0000', // Red text
        fontWeight: 'bold',
        marginBottom: 5,
        fontSize: 10
    },
    nonConformitiesList: {
        marginLeft: 10,
    },
    nonConformitiesItem: {
        color: '#cc0000', // Red text
        fontSize: 10,
        marginBottom: 2,
    },

    taskListContainer: {
        backgroundColor: '#e0ffe0', // Light green background
        borderColor: '#007f00', // Green border
        borderWidth: 1,
        borderRadius: 3,
        padding: 5,
        marginTop: 10,
        marginBottom: 10,
    },
    taskListText: {
        color: '#007f00', // Green text
        fontWeight: 'bold',
        marginBottom: 5,
        fontSize: 10,
    },
    taskList: {
        marginLeft: 10,
    },
    taskItem: {
        marginBottom: 5,
    },
    taskTitle: {
        color: '#007f00', // Green text
        fontWeight: 'bold',
        fontSize: 10,
    },
    taskDescription: {
        color: '#007f00', // Green text
        fontSize: 10,
        marginLeft: 10,
    },
    reportAbstractSection: {
        marginBottom: 10,
        paddingBottom: 10,
        borderBottom: '1px solid #e0e0e0',
    },
    highlightedNonConformitiesSection: {
        marginBottom: 10,
        paddingBottom: 10,
        borderBottom: '1px solid #e0e0e0',
    },
    highlightedNonConformitiesList: {
        marginLeft: 10,
        marginBottom: 5,
        fontSize: 10,
    },
    highlightedNonConformitiesItem: {
        marginBottom: 2,
        fontSize: 10,
        lineHeight: 1.5
    },
});


const MyDoc = ({ reportData, reportAbstract, userId, reportId, currentDate }) => {

    const [pageIndexes, setPageIndexes] = useState({});

    const updatePageIndexes = (id, pageNumber) => {
        setPageIndexes(prevState => {
            if (prevState[id] !== pageNumber) {
                return { ...prevState, [id]: pageNumber };
            }
            return prevState;
        });
    };

    const getPageNumber = (id, pageNumber) => {
        updatePageIndexes(id, pageNumber);
        return pageIndexes[id] ? pageIndexes[id] : pageNumber;
    };


    const formatSectionId = (id) => {
        return id
            .replace(/_/g, ' ') // Replace underscores with spaces
            .split(' ') // Split the string into words
            .map(word => word.charAt(0).toUpperCase() + word.slice(1)) // Capitalize each word
            .join(' '); // Join the words back together
    };

    const getLabelStyle = (overallCompliance) => {
        if (overallCompliance.includes('NC')) return styles.labelNC;
        if (overallCompliance.includes('PC')) return styles.labelPC;
        return styles.labelC;
    };

    useEffect(() => {
        // Log updated pageIndexes to verify
        console.log('Page indexes updated:', pageIndexes);
    }, [pageIndexes]);

    const getUniqueCheckedDocuments = (requirement) => {

        const checkedDocumentsSet = new Set();
        requirement?.sub_requirements?.forEach(subRequirement => {
            subRequirement?.checked_documents?.forEach(doc => checkedDocumentsSet.add(doc));
        });
        console.log("assasaas", Array.from(checkedDocumentsSet))
        return Array.from(checkedDocumentsSet); // Return as an array
    };

    const getAllNonConformities = (requirement) => {
        let nonConformities = [];
        requirement?.sub_requirements?.forEach(subRequirement => {
            if (subRequirement?.non_conformities) {
                nonConformities = nonConformities.concat(subRequirement.non_conformities);
            }
        });
        return nonConformities;
    };

    const getAllTasks = (requirement) => {
        let tasks = [];
        requirement?.sub_requirements?.forEach(subRequirement => {
            if (subRequirement?.tasks_list) {
                tasks = tasks.concat(subRequirement.tasks_list);
            }
        });
        return tasks;
    };

    return (
        <Document>
            <Page size="A4" style={styles.page} wrap>
                {/* Header */}
                <View fixed style={styles.header}>
                    {/* Add your SVG here */}
                    <Text style={styles.reportId}>Report ID: {reportId}</Text>
                    <Text style={styles.date}>{currentDate}</Text>
                </View>

                {/* Table of Contents */}
                <View style={styles.content}>
                    <Text style={styles.tocHeader}>Table of Contents</Text>
                    <Link src="#report-abstract" style={styles.tocItem}>
                        <Text style={styles.tocSection}>Report Abstract</Text>
                        <Text style={styles.tocSection}>
                            {pageIndexes['report-abstract'] || ''}
                        </Text>
                    </Link>
                    {reportData.map((section, sectionIndex) => (
                        <View key={section.id}>
                            <Link src={`#${section.id}`} style={styles.tocItem}>
                                <Text style={styles.tocSection}>{formatSectionId(section.id)}</Text>
                                <Text style={styles.tocSection}>
                                    {pageIndexes[section.id] || ''}
                                </Text>
                            </Link>
                            {section.data.requirements.map((requirement, reqIndex) => (
                                <Link key={reqIndex} src={`#${section.id}_req${reqIndex}`} style={styles.tocItem}>
                                    <Text style={styles.tocRequirement}>{requirement.requirement}</Text>
                                    <Text style={styles.tocRequirement}>
                                        {pageIndexes[`${section.id}_req${reqIndex}`] || ''}
                                    </Text>
                                </Link>
                            ))}
                        </View>
                    ))}
                </View>

                {/* Footer */}
                <View fixed style={styles.footer}>
                    <Text style={styles.footerTextLeft}>
                        The report is automatically generated with Large Language Models and can contain errors. We recommend double-checking important information.
                    </Text>
                    <Text style={styles.footerTextRight} render={({ pageNumber, totalPages }) => `Page ${pageNumber} of ${totalPages}`} />
                </View>
            </Page>

            {/* Page 2 and onward: Report Content */}
            <Page size="A4" style={styles.page} wrap>
                {/* Header */}
                <View fixed style={styles.header}>
                    {/* Add your SVG here */}
                    <Text style={styles.reportId}>Report ID: {reportId}</Text>
                    <Text style={styles.date}>{currentDate}</Text>
                </View>

                {/* Report Abstract */}
                <View style={styles.reportAbstractSection}>
                    <View style={styles.sectionContainer}>
                        <Text style={styles.sectionHeader}>Report Abstract</Text>
                    </View>
                    <Text style={styles.requirementDescription}>{reportAbstract.report_abstract.report_abstract}</Text>
                    <Text
                        fixed
                        style={{ display: 'none' }}
                        render={({ pageNumber }) => updatePageIndexes('report-abstract', pageNumber)}
                    />
                </View>

                {/* Report Content */}
                {reportData.map((section) => (
                    <View key={section.id} style={styles.section}>
                        <View style={styles.sectionContainer}>
                            <Text id={section.id} style={styles.sectionHeader}>{formatSectionId(section.id)}</Text>
                        </View>
                        {section.data.requirements.map((requirement, reqIndex) => (
                            <View key={reqIndex} style={styles.section}>
                                <View style={styles.requirementHeaderContainer}>
                                    <Text id={`${section.id}_req${reqIndex}`} style={styles.requirementHeader}>
                                        {requirement.requirement}
                                    </Text>
                                    <Text style={[styles.label, getLabelStyle(requirement.overall_compliance_grade)]}>
                                        {requirement.overall_compliance_grade}
                                    </Text>
                                </View>

                                {/* Requirement description and assessment */}
                                <Text style={styles.requirementDescription}>
                                    <Text style={styles.boldText}>Description of requirement:</Text> {requirement.description}
                                </Text>
                                <Text style={styles.requirementDescription}>
                                    <Text style={styles.boldText}>Overall assessment:</Text> {requirement.short_compliance_explanation}
                                </Text>

                                {/* Checked Documents from sub-requirements */}
                                <View style={styles.checkedDocumentsContainer}>
                                    <Text style={styles.checkedDocumentsText}>The following documents were checked:</Text>
                                    <View style={styles.checkedDocumentsList}>
                                        {getUniqueCheckedDocuments(requirement).map((document, index) => (
                                            <Text key={index} style={styles.checkedDocumentsItem}>• {document.path}</Text>
                                        ))}
                                    </View>
                                </View>

                                {/* Non-Conformities */}
                                {getAllNonConformities(requirement).length > 0 && (
                                    <View style={styles.nonConformitiesContainer}>
                                        <Text style={styles.nonConformitiesText}>The following sources of possible non-conformities were identified</Text>
                                        <View style={styles.nonConformitiesList}>
                                            {getAllNonConformities(requirement).map((nonConformity, index) => (
                                                <Text>
                                                    <Text key={index} style={styles.nonConformitiesText}>• {nonConformity.title}</Text>
                                                    <Text key={index} style={styles.nonConformitiesItem}> {nonConformity.description}</Text>
                                                </Text>
                                            ))}
                                        </View>
                                    </View>
                                )}

                                {/* Suggested Tasks */}
                                {getAllTasks(requirement).length > 0 && (
                                    <View style={styles.taskListContainer}>
                                        <Text style={styles.taskListText}>
                                            Based on the possible non-conformities, the following tasks are suggested:
                                        </Text>
                                        <View style={styles.taskList}>
                                            {getAllTasks(requirement).map((task, index) => (
                                                <View key={index} style={styles.taskItem}>
                                                    <Text style={styles.taskTitle}>• {task.title}</Text>
                                                    <Text style={styles.taskDescription}>{task.short_description}</Text>
                                                </View>
                                            ))}
                                        </View>
                                    </View>
                                )}

                                {/* Sub Requirements */}
                                {requirement?.sub_requirements && requirement?.sub_requirements.length > 0 && (
                                    <View style={styles.section}>
                                        <Text style={styles.requirementHeader}>Detailed Sub Requirement Analysis</Text>
                                        {requirement?.sub_requirements?.map((subRequirement, subReqIndex) => (
                                            <View key={subReqIndex} style={styles.section}>
                                                <View style={styles.requirementHeaderContainer}>
                                                    <Text>
                                                        {subRequirement.description}
                                                    </Text>
                                                    {/* <Text style={[styles.label, getLabelStyle(subRequirement.compliance_grade)]}>
                                                        {subRequirement.compliance_grade}
                                                    </Text> */}
                                                </View>
                                                {/* <Text style={styles.requirementDescription}>
                                                    {subRequirement.detailed_compliance_explanation}
                                                </Text> */}
                                            </View>
                                        ))}
                                    </View>
                                )}
                            </View>
                        ))}
                    </View>
                ))}

                {/* Footer */}
                <View fixed style={styles.footer}>
                    <Text style={styles.footerTextLeft}>
                        The report is automatically generated with Large Language Models and can contain errors. We recommend double-checking important information.
                    </Text>
                    <Text style={styles.footerTextRight} render={({ pageNumber, totalPages }) => `Page ${pageNumber} of ${totalPages}`} />
                </View>
            </Page>
        </Document>
    );
};

export default MyDoc;
