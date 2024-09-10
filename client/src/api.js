// src/api.js
import { db } from "./firebase";
import { doc, updateDoc, getDoc } from "firebase/firestore";
import useAuthStore from "./store";

// Function to update task status in Firestore
export const updateTaskStatus = async (userId, sectionId, requirementIndex, subRequirementIndex, taskTitle, status) => {
    try {
        const docRef = doc(db, "reports", userId, "sections", sectionId);

        // Fetch the current document to get all existing data
        const docSnap = await getDoc(docRef);
        if (!docSnap.exists()) {
            console.error("No such document!");
            return;
        }

        // Clone the current data to avoid modifying the original directly
        const currentData = { ...docSnap.data() };

        // Find the specific requirement and sub-requirement to update the task
        const requirement = currentData.requirements[requirementIndex];
        const subRequirement = requirement.sub_requirements[subRequirementIndex];

        if (!subRequirement) {
            console.error("Sub-requirement not found!");
            return;
        }

        // Find the task within the sub-requirement's task_list
        const task = subRequirement.tasks_list.find(t => t.title === taskTitle);

        if (!task) {
            console.error("Task not found!");
            return;
        }

        // Update the task status
        task.user_input = status;

        // Update Firestore with the new task status while preserving other data
        await updateDoc(docRef, {
            requirements: currentData.requirements  // This preserves the full structure of `requirements` and `sub_requirements`
        });

        // Update the Zustand store with the new task status
        useAuthStore.setState((state) => ({
            reportData: state.reportData.map(sec =>
                sec.id === sectionId
                    ? {
                        ...sec,
                        data: {
                            ...sec.data,
                            requirements: currentData.requirements
                        }
                    }
                    : sec
            )
        }));

    } catch (error) {
        console.error("Error updating task status:", error);
    }
};
