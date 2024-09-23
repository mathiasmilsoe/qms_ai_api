// src/App.js
import React, { useRef, useState, useEffect } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Layout, Affix, Alert } from "antd"; // Import Alert from Ant Design
import SignInPage from "./pages/SignInPage";
import NotFoundPage from "./pages/NotFoundPage";
import ShowReportPage from "./pages/ShowReportPage";
import Header from "./components/LogoHeader";
import SiderComponent from "./components/Sider";  // Import the new SiderComponent
import 'tachyons';
import useStore from "./store";

const { Content } = Layout;

const formatRequirement = (text) => {
  if (text) {
    return text
      .replace(/[_-]/g, ' ')  // Replace both "_" and "-" with a space
      .replace(/\w\S*/g, (w) => w.replace(/^\w/, (c) => c.toUpperCase()));  // Capitalize each word
  } else {
    return "";
  }
};

const App = () => {
  const showReportRef = useRef(); // Reference for ShowReportPage
  const activeSection = useStore((state) => state.activeSection)
  const activeRequirement = useStore((state) => state.activeRequirement)
  const token = useStore((state) => state.token)
  const reportData = useStore((state) => state.reportData);

  // State to manage which sections are expanded
  const [expandedSections, setExpandedSections] = useState([]);

  // State to control whether to show the browser alert
  const [showBrowserAlert, setShowBrowserAlert] = useState(false);

  // Function to detect if the user is using Chrome
  const detectBrowser = () => {
    const userAgent = navigator.userAgent.toLowerCase();
    if (!userAgent.includes("chrome")) {
      setShowBrowserAlert(true);
    }
  };

  // Run browser detection when the component mounts
  useEffect(() => {
    detectBrowser();
  }, []);

  // Function to open all sections
  const openAllSections = () => {
    const allKeys = [];  // Array to hold all keys that need to be expanded

    reportData.forEach((section) => {
      allKeys.push(section.id); // Add section key

      section.data.requirements.forEach((requirement, reqIndex) => {
        allKeys.push(`${requirement.requirement}`); // Add requirement key
        allKeys.push(`checked-documents-${reqIndex}`); // Add documents key
        allKeys.push(`non-conformities-${reqIndex}`); // Add non-conformities key

        requirement?.sub_requirements?.forEach((subRequirement, subReqIndex) => {
          allKeys.push(`${requirement.requirement}-sub-${subReqIndex}`); // Add sub-requirement key
        });
      });
    });

    setExpandedSections(allKeys); // Set all keys to be expanded
  };

  // Function to collapse all sections
  const collapseAllSections = () => {
    setExpandedSections([]);
  };

  return (
    <Router>
      <Layout style={{ minHeight: "100vh", minWidth: 1200 }}>
        {showBrowserAlert && (
          <Affix offsetTop={0}>
            <Alert
              description="LumiDocs is faster and more stable in Chrome. For the best experience, please switch to Chrome."
              type="warning"
              closable
              onClose={() => setShowBrowserAlert(false)}
              style={{ textAlign: 'center' }}
              className="mr3 ml3 mt1"
            />
          </Affix>
        )}

        {/* Render the Header only on non-signin routes */}
        <Routes>
          <Route path="/signin" element={<SignInPage />} />
          <Route
            path="/show_report"
            element={
              <>
                <Affix offsetTop={0}>
                  <Header showReportRef={showReportRef} isDemo={false} />
                </Affix>
                <ShowReportPage
                  ref={showReportRef}
                  expandedSections={expandedSections}
                  setExpandedSections={setExpandedSections}
                  collapseAllSections={collapseAllSections}
                  openAllSections={openAllSections}
                />
              </>
            }
          />
          <Route
            path="/d"
            element={
              <>
                <Affix offsetTop={0}>
                  <Header showReportRef={showReportRef} isDemo={true} />
                </Affix>
                <ShowReportPage
                  ref={showReportRef}
                  expandedSections={expandedSections}
                  setExpandedSections={setExpandedSections}
                  collapseAllSections={collapseAllSections}
                  openAllSections={openAllSections}
                  demoReportId="49Ymd6vvIqhOZChldJ8GUcAjbcv1"
                />
              </>
            }
          />
          <Route path="/" element={<SignInPage />} />
          <Route path="*" element={<NotFoundPage />} />
        </Routes>
      </Layout>
    </Router>
  );
};

export default App;
