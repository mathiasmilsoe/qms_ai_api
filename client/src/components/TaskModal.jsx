import React, { useState, useRef } from "react";
import { Modal, List, Typography, Button } from "antd";
import { CheckCircleOutlined, CloseCircleOutlined, UndoOutlined } from "@ant-design/icons";
import useStore from "../store";
import PropTypes from "prop-types";
import { updateTaskStatus } from "../api";
import SuggestionModal from "./SuggestionModal";

const { Text } = Typography;

const TaskModal = ({ isVisible, onClose, sectionId = null, requirementIndex = null }) => {
    const reportData = useStore((state) => state.reportData);
    const userId = useStore((state) => state.userId);
    const [loadingButtons, setLoadingButtons] = useState({});
    const contentRef = useRef();

    const [suggestionModalVisible, setSuggestionModalVisible] = useState(false);
    const [currentTask, setCurrentTask] = useState(null);
    const [suggestionIsOpening, setSuggestionIsOpening] = useState(false)

    const openSuggestionModal = (task) => {
        setSuggestionIsOpening(true)
        setCurrentTask(task);
        setSuggestionModalVisible(true);
        setSuggestionIsOpening(false)
    };

    const closeSuggestionModal = () => {
        setSuggestionModalVisible(false);
        setCurrentTask(null);
    };

    const handleTaskUpdate = async (sectionId, requirementIndex, subRequirementIndex, taskTitle, status) => {
        const buttonKey = `${sectionId}-${requirementIndex}-${subRequirementIndex}-${taskTitle}-${status}`;
        setLoadingButtons((prev) => ({ ...prev, [buttonKey]: true }));
        try {
            await updateTaskStatus(userId, sectionId, requirementIndex, subRequirementIndex, taskTitle, status);
        } finally {
            setLoadingButtons((prev) => ({ ...prev, [buttonKey]: false }));
        }
    };

    const sortedTasks = (tasks) => {
        return [
            ...tasks.filter(task => !task.user_input || task.user_input === "open" || task.user_input === ""),
            ...tasks.filter(task => task.user_input === "done"),
            ...tasks.filter(task => task.user_input === "not_relevant")
        ];
    };

    const formatRequirement = (text) => {
        return text
            .replace(/_/g, ' ')
            .replace(/\w\S*/g, (w) => w.replace(/^\w/, (c) => c.toUpperCase()));
    };

    const filteredSections = sectionId ? reportData.filter(section => section.id === sectionId) : reportData;

    return (
        <Modal
            title={null}
            open={isVisible}
            onOk={onClose}
            onCancel={onClose}
            width="80%"
            footer={null}
        >
            <div ref={contentRef}>
                {filteredSections.map((section, sectionIndex) => (
                    <div key={sectionIndex}>
                        <h2>{formatRequirement(section.id)}</h2>
                        {section.data.requirements.map((requirement, reqIndex) => {
                            if (requirementIndex !== null && reqIndex !== requirementIndex) {
                                return null;
                            }
                            return (
                                <div key={reqIndex}>
                                    <SuggestionModal
                                        isVisible={suggestionModalVisible}
                                        onClose={closeSuggestionModal}
                                        task={currentTask}
                                    />
                                    {requirement?.sub_requirements?.map((subReq, subReqIndex) => (
                                        <div key={subReqIndex}>
                                            {Array.isArray(subReq.tasks_list) && subReq.tasks_list.length > 0 && (
                                                <List
                                                    header={<div className="fw7">{formatRequirement(subReq.description)}</div>}
                                                    dataSource={sortedTasks(subReq.tasks_list)}
                                                    renderItem={(task, taskIndex) => (
                                                        <List.Item
                                                            actions={[
                                                                task.user_input === "open" || task.user_input === "" ? (
                                                                    <>

                                                                        <Button
                                                                            key="done"
                                                                            className="green mr3"
                                                                            icon={<CheckCircleOutlined />}
                                                                            loading={loadingButtons[`${section.id}-${reqIndex}-${subReqIndex}-${task.title}-done`]}
                                                                            onClick={() => handleTaskUpdate(section.id, reqIndex, subReqIndex, task.title, "done")}
                                                                        >
                                                                            Done
                                                                        </Button>
                                                                        <Button
                                                                            key="notRelevant"
                                                                            className="red mr3"
                                                                            icon={<CloseCircleOutlined />}
                                                                            loading={loadingButtons[`${section.id}-${reqIndex}-${subReqIndex}-${task.title}-not_relevant`]}
                                                                            onClick={() => handleTaskUpdate(section.id, reqIndex, subReqIndex, task.title, "not_relevant")}
                                                                        >
                                                                            Not Relevant
                                                                        </Button>

                                                                        <Button
                                                                            key="suggestion"
                                                                            className="blue "
                                                                            onClick={() => openSuggestionModal(task)}
                                                                            loading={suggestionIsOpening}
                                                                        >
                                                                            Suggestion
                                                                        </Button>
                                                                    </>
                                                                ) : (
                                                                    <Button
                                                                        key="reopen"
                                                                        onClick={() => handleTaskUpdate(section.id, reqIndex, subReqIndex, task.title, "open")}
                                                                        icon={<UndoOutlined />}
                                                                        loading={loadingButtons[`${section.id}-${reqIndex}-${subReqIndex}-${task.title}-open`]}
                                                                    >
                                                                        Re-open
                                                                    </Button>
                                                                )
                                                            ]}
                                                        >
                                                            <List.Item.Meta
                                                                className="pl4"
                                                                title={
                                                                    task.user_input === "not_relevant" ? (
                                                                        <Text style={{ fontWeight: 'lighter', textDecoration: 'line-through' }}>{task.title}</Text>
                                                                    ) : task.user_input === "done" ? (
                                                                        <div style={{ display: 'flex', alignItems: 'center' }}>
                                                                            <CheckCircleOutlined style={{ color: 'green', marginRight: 5 }} />
                                                                            <Text style={{ color: 'green', fontWeight: 'normal' }}>{task.title}</Text>
                                                                        </div>
                                                                    ) : (
                                                                        task.title
                                                                    )
                                                                }
                                                                description={
                                                                    task.user_input === "open" || task.user_input === "" ? task.description : ""
                                                                }
                                                            />
                                                        </List.Item>
                                                    )}
                                                />
                                            )}
                                        </div>
                                    ))}
                                </div>
                            );
                        })}
                    </div>
                ))}
            </div>
        </Modal>
    );
};

TaskModal.propTypes = {
    isVisible: PropTypes.bool.isRequired,
    onClose: PropTypes.func.isRequired,
    sectionId: PropTypes.string,
    requirementIndex: PropTypes.number,
};

export default TaskModal;
