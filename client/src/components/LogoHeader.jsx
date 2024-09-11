import React, { useState } from "react";
import { Layout, Button, message } from "antd";
import { useNavigate } from "react-router-dom"; // Import useLocation
import logo from "../logo.svg";
import useStore from "../store";
import MyDoc from './MyDoc';  // Import your PDF document component
import { PDFDownloadLink, pdf } from '@react-pdf/renderer'; // Import pdf for manual PDF generation
import TaskModal from "./TaskModal";

const { Header: AntHeader } = Layout;

const Header = ({ showReportRef, isDemo }) => {
    const token = useStore((state) => state.token);
    const signOut = useStore((state) => state.signOut);
    const reportData = useStore((state) => state.reportData);
    const userId = useStore((state) => state.userId); // Get the userId from Zustand
    const reportId = useStore((state) => state.reportId);
    const reportAbstract = useStore((state) => state.reportAbstract);
    const navigate = useNavigate();
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [isPreparingPdf, setIsPreparingPdf] = useState(false);

    const currentDate = new Date().toLocaleString('en-GB', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });

    const handleSignOut = () => {
        signOut();
        navigate("/signin");
    };

    const downloadPDF = async () => {
        setIsPreparingPdf(true);
        await message.loading({ content: "Preparing PDF...", key: "pdf-download" });
        const doc = <MyDoc reportAbstract={reportAbstract} reportData={reportData} userId={userId} reportId={reportId} currentDate={currentDate} />;
        const blob = await pdf(doc).toBlob();
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = "Report.pdf";
        link.click();
        message.success({ content: "PDF downloaded", key: "pdf-download", duration: 2 });
        setIsPreparingPdf(false);
    };

    return (
        <AntHeader className="pa3 bg-white br3 mr2 ml2 mt2 mb2" style={{ display: "flex", justifyContent: "space-between", alignItems: "center", background: "#fff", padding: "0 20px" }}>
            <div style={{ display: "flex", alignItems: "center" }}>
                <img src={logo} alt="Logo" style={{ height: "40px" }} />

                {/* Show the demo message if the user is on /d */}

            </div>
            <div className="w-100 flex justify-center">{isDemo && (
                <span className="blue f5 ml4 b">
                    You are viewing a demo report for a fictional product and company
                </span>
            )}</div>

            {token ? (
                <div>
                    <Button type="primary" onClick={handleSignOut}>
                        Sign Out
                    </Button>
                </div>
            ) : (
                ""
            )}

            {/* Use the TaskModal component */}
            <TaskModal isVisible={isModalVisible} onClose={() => setIsModalVisible(false)} />
        </AntHeader>
    );
};

export default Header;
