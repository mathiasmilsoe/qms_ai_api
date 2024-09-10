// src/components/NotFoundPage.js
import React from "react";
import { Result } from "antd";

const NotFoundPage = () => (
    <Result
        status="404"
        title="No Report ID Provided"
        subTitle="Please check the URL and try again."
    />
);

export default NotFoundPage;
