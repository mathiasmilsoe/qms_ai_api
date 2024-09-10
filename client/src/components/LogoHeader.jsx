// src/components/LogoHeader.jsx

import React, { useState } from "react";
import { Layout, Button, message } from "antd";
import { CheckCircleOutlined, FilePdfOutlined } from "@ant-design/icons";
import { useNavigate } from "react-router-dom";
import logo from "../logo.svg";
import useStore from "../store";
import MyDoc from './MyDoc';  // Import your PDF document component
import { PDFDownloadLink, pdf } from '@react-pdf/renderer'; // Import pdf for manual PDF generation
import TaskModal from "./TaskModal";

const { Header: AntHeader } = Layout;

const Header = ({ showReportRef }) => {
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
        <AntHeader className="pa3 bg-white br3 mr3 ml3 mt1" style={{ display: "flex", justifyContent: "space-between", alignItems: "center", background: "#fff", padding: "0 20px" }}>
            <img src={logo} alt="Logo" style={{ height: "40px" }} />

            {token ? (
                <div>
                    {/* <Button disabled={isPreparingPdf} icon={<FilePdfOutlined />} onClick={downloadPDF}>
                        Export to PDF
                    </Button> */}
                    {/* <Button className="ml2" icon={<CheckCircleOutlined />} onClick={() => setIsModalVisible(true)} style={{ marginRight: 10 }}>
                        Task list
                    </Button> */}
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
