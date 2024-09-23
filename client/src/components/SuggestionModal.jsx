import React, { useEffect } from "react";
import { Modal, Button, Typography, message } from "antd";
import { CopyOutlined } from "@ant-design/icons";
import ReactMarkdown from "react-markdown";
import rehypeRaw from "rehype-raw"; // Import rehype-raw to allow raw HTML
import PropTypes from "prop-types";
import useStore from "../store";
import { analytics } from "../firebase"
import { logEvent } from "firebase/analytics";

const { Text } = Typography;

const SuggestionModal = ({ isVisible, onClose, task }) => {
    const userId = useStore((state) => state.userId);

    useEffect(() => {
        if (isVisible && task.suggestion) {
            logEvent(analytics, 'suggestion_rendered', {
                task: task.title,
                user_id: userId,
            });
        }
    }, [isVisible, task, userId]);

    if (!task) return null;

    // Function to copy suggestion to clipboard and show message
    const copySuggestionToClipboard = () => {
        if (task.suggestion) {
            navigator.clipboard.writeText(task.suggestion)
                .then(() => {
                    logEvent(analytics, 'suggestion_copied', {
                        task: task,
                        user_id: userId,
                    });
                    message.success('The suggestion has been copied to your clipboard.');
                })
                .catch(() => {
                    message.error('There was an issue copying the suggestion. Please try again.');
                });
        }
    };

    // Highlight [["description of blank field"]] as <mark>[description]</mark>
    const renderSuggestion = (suggestion) => {
        if (!suggestion) {
            return "No suggestion for this task";
        }
        return suggestion.replace(
            /\[\[\s*(.*?)\s*\]\]/g,
            '<mark>$1</mark>'
        );
    };

    return (
        <Modal
            title={`Implementation Suggestion: ${task.title}`}
            open={isVisible}
            onCancel={onClose}
            footer={null}
            width={"50%"}
        >
            <div>
                <ReactMarkdown
                    rehypePlugins={[rehypeRaw]} // Enable raw HTML
                    components={{
                        // Optional: Customize the <mark> element if needed
                        mark: ({ node, ...props }) => (
                            <span style={{ backgroundColor: "yellow", padding: "0.2em", borderRadius: "3px" }}>
                                {props.children}
                            </span>
                        ),
                    }}
                >
                    {renderSuggestion(task.suggestion)}
                </ReactMarkdown>
                <Button
                    icon={<CopyOutlined />}
                    onClick={copySuggestionToClipboard}
                    disabled={!task.suggestion}
                    style={{ marginTop: 16 }}
                >
                    Copy Suggestion
                </Button>
                <div style={{ marginTop: 24 }}>
                    <h4>Relevant Documents:</h4>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                        {task.associated_documents && task.associated_documents.length > 0 ? (
                            task.associated_documents.map((doc, index) => (
                                <Text
                                    key={index}
                                    className="bg-washed-blue br2 mb1 ba b-blue blue pa2"
                                >
                                    {doc.short_name}
                                </Text>
                            ))
                        ) : (
                            <Text>No associated documents</Text>
                        )}
                    </div>
                </div>
            </div>
        </Modal>
    );
};

SuggestionModal.propTypes = {
    isVisible: PropTypes.bool.isRequired,
    onClose: PropTypes.func.isRequired,
    task: PropTypes.shape({
        title: PropTypes.string,
        suggestion: PropTypes.string,
        associated_documents: PropTypes.arrayOf(
            PropTypes.shape({
                short_name: PropTypes.string,
                path: PropTypes.string,
            })
        ),
    }),
};

export default SuggestionModal;
