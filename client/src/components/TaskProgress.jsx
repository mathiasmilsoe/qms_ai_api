import React from 'react';
import PropTypes from 'prop-types';
import useStore from '../store';

const TaskProgress = ({ sectionId = null, requirementIndex = null, parentHeight = 'auto', onOpenModal }) => {
    // Fetch the report data from Zustand store
    const reportData = useStore(state => state.reportData);

    let tasks = [];
    if (sectionId) {
        // Find the relevant section and optionally the requirement within that section
        const section = reportData.find(section => section.id === sectionId);

        if (section) {
            if (requirementIndex !== null) {
                const requirement = section.data.requirements[requirementIndex];
                if (requirement) {
                    // Collect tasks from all sub_requirements within the requirement
                    tasks = requirement?.sub_requirements?.flatMap(subReq => subReq.tasks_list || []);
                }
            } else {
                // If no requirementIndex is provided, accumulate all tasks from all requirements
                tasks = section.data.requirements.flatMap(req =>
                    req?.sub_requirements?.flatMap(subReq => subReq.tasks_list || [])
                );
            }
        }
    } else {
        // If no sectionId is provided, accumulate all tasks from all sections
        tasks = reportData.flatMap(section =>
            section.data.requirements.flatMap(req =>
                req?.sub_requirements?.flatMap(subReq => subReq.tasks_list || [])
            )
        );
    }

    // Calculate the number of resolved tasks based on user_input
    const resolvedTasksCount = tasks?.filter(task => task?.user_input === "done" || task?.user_input === "not_relevant").length;
    const totalTasksCount = tasks?.length || 0;

    // Calculate the progress percentage
    const progressPercentage = totalTasksCount > 0 ? (resolvedTasksCount / totalTasksCount) * 100 : 0;

    // Function to handle click event and open the modal
    const handleClick = (e) => {
        e.stopPropagation();  // Stop the click event from bubbling up to parent elements
        onOpenModal(sectionId, requirementIndex);
    };

    return (
        <div className="dim" style={{ height: parentHeight, cursor: 'pointer' }} onClick={handleClick}>
            {/* Progress bar */}
            <div style={{
                width: '100%',
                height: 8,
                backgroundColor: '#e0e0e0',
                borderRadius: '5px',
                overflow: 'hidden'
            }}>
                <div style={{
                    width: `${progressPercentage}%`,
                    height: '100%',
                    backgroundColor: '#4FD1C5',
                    borderRadius: '5px 0 0 5px'
                }}></div>
            </div>
            {/* Label */}
            <p className="f7 mt1" style={{ textAlign: 'center' }}>
                {resolvedTasksCount}/{totalTasksCount} resolved tasks
            </p>
        </div>
    );
};

// PropTypes to ensure correct usage
TaskProgress.propTypes = {
    sectionId: PropTypes.string, // Optional
    requirementIndex: PropTypes.number, // Optional
    parentHeight: PropTypes.string, // Optional prop to control height
    onOpenModal: PropTypes.func.isRequired, // Function to open the modal
};

export default TaskProgress;
