// src/components/SiderComponent.js
import React from 'react';
import { Layout, Menu } from 'antd';
import { ToTopOutlined, MenuUnfoldOutlined, ShrinkOutlined } from '@ant-design/icons'; // Import relevant icons

const { Sider } = Layout;

const SiderComponent = ({ onOpenAll, onCollapseAll }) => {

    // Function to scroll to the top
    const scrollToTop = () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    const collapseAll = () => {
        onCollapseAll()
        scrollToTop()
    }

    return (
        <Sider
            collapsed
            style={{
                background: '#fff', // Set background to white
                borderRadius: '10px', // Add soft corners with a radius of 10px
                overflow: 'hidden', // Ensure content fits within rounded corners
                marginLeft: 15,
                marginTop: 15,
                height: "100%"
            }}
        >
            <Menu theme="light" mode="inline" selectedKeys={[]}>
                <Menu.Item key="1" icon={<ToTopOutlined />} onClick={scrollToTop}>
                    To the top
                </Menu.Item>
                <Menu.Item key="2" onClick={onOpenAll} icon={<MenuUnfoldOutlined />} >
                    Open all
                </Menu.Item>
                <Menu.Item key="3" onClick={collapseAll} icon={<ShrinkOutlined />}>
                    Collapse all
                </Menu.Item>
                {/* Add more menu items as needed */}
            </Menu>
        </Sider>
    );
};

export default SiderComponent;
