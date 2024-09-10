import { create } from 'zustand';
import { persist } from 'zustand/middleware';

const useStore = create(
    persist(
        (set) => ({
            token: null,
            userId: '',
            reportId: '',
            reportData: [],  // Initial state for reportData
            setToken: (token) => set({ token }),
            setUserId: (userId) => set({ userId }),
            setReportId: (reportId) => set({ reportId }),
            setReportData: (reportData) => set({ reportData }),  // Function to set reportData
            signOut: () => {
                set({ token: null, userId: '', reportId: '', reportData: [], reportAbstract: null, activeSection: null, activeRequirement: null });
                localStorage.removeItem('auth-storage'); // Clear persisted data from localStorage
            },
            activeSection: null, // state to store the currently active section    
            setActiveSection: (sectionId) => set({ activeSection: sectionId }),
            activeRequirement: null, // state to store the currently active section    
            setActiveRequirement: (requirement) => set({ activeRequirement: requirement }),
            reportAbstract: null,  // New state for reportAbstract            
            setReportAbstract: (abstract) => set({ reportAbstract: abstract }),
        }),
        {
            name: 'lumidocs-store',
            getStorage: () => localStorage, // Use local storage for persistence
        }
    )
);

export default useStore;
