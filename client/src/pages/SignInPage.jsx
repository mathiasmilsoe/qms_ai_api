// src/components/SignInPage.js
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Input, Button, message, Typography } from "antd";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";
import useStore from "../store";
import { analytics } from "../firebase";
import { logEvent } from "firebase/analytics";

const { Title, Text } = Typography;

const SignInPage = () => {
    const [reportId, setReportId] = useState("");
    const [password, setPassword] = useState("");
    const setToken = useStore((state) => state.setToken);
    const setUserId = useStore((state) => state.setUserId); // Access the setUserId method from Zustand store
    const setStoreReportId = useStore((state) => state.setReportId);
    const navigate = useNavigate();
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        // Check if the event has already been logged in this session
        if (!sessionStorage.getItem('sign_in_page_loaded')) {
            logEvent(analytics, 'sign_in_page_loaded');
            sessionStorage.setItem('sign_in_page_loaded', 'true');
        }
    }, []);

    const handleSignIn = async () => {
        if (!reportId) {
            message.error("Please enter a report ID.");
            return;
        }

        setIsLoading(true);
        const email = `${reportId}@lumidocs.web.app`;
        try {
            const userCredential = await signInWithEmailAndPassword(auth, email, password);
            const token = await userCredential.user.getIdToken();
            setToken(token);
            setUserId(userCredential.user.uid); // Store the user's UUID in Zustand
            setStoreReportId(reportId);
            logEvent(analytics, 'sign_in_completed', {
                user_id: reportId,
            });
            message.success("Successfully signed in!");
            navigate(`/show_report`);
        } catch (error) {
            logEvent(analytics, 'sign_in_failed', {
                report_id: reportId,
            });
            message.error("Password does not match report ID.");
        }
        setIsLoading(false);
    };

    return (
        <div className="mw6 h6 center mt5 pl5 pr5 pb5 pt3 tc bg-white br3">
            <Title level={2} className="mb3">Sign in</Title>
            <Text type="secondary" className="mb4 db">Enter the report ID and password to sign in and view the report</Text>

            <Input
                placeholder="Report ID"
                value={reportId}
                onChange={(e) => setReportId(e.target.value)}
                className="mb3"
            />
            <Input.Password
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mb3"
            />
            <Button type="primary" onClick={handleSignIn} className="w-100" loading={isLoading}>
                Sign In
            </Button>
        </div>
    );
};

export default SignInPage;
