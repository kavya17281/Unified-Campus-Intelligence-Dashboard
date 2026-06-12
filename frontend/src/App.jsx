import { useState, useEffect, useRef } from "react";

import InputBox from "./components/chat/InputBox";
import MessageBox from "./components/chat/MessageBox";

import ShowLibrary from "./components/library/ShowLibrary";
import ShowEvents from "./components/events/ShowEvents";
import ShowCafeteria from "./components/cafeteria/ShowCafeteria";
import ShowAcademics from "./components/academics/ShowAcademics";

import "./styles/App.css";
import "./styles/AssistantPanel.css";
import "./styles/OverviewPanel.css";

const messageData = [
    {
        message: "hello",
        sender: "user",
        time: "2200",
        id: crypto.randomUUID()
    },
    {
        message: "hi! how can i help you",
        sender: "robot",
        time: "2201",
        id: crypto.randomUUID()
    }
];

export default function App() {

    const [messages, setMessages] = useState(messageData);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    const chatRef = useRef(null);

    const [mcpData, setMcpData] = useState({
            library: [],
            events: [],
            cafeteria: [],
            academics: []
        });

    async function updateData() {

        const response = await fetch("/dashboard-data");
        const data = await response.json();

        setMcpData(data);
    }


    useEffect(() => {
        chatRef.current?.scrollTo({
            top: chatRef.current.scrollHeight,
            behavior: "smooth"
        });
    }, [messages]);

    useEffect(() => {updateData();}, []);

    return (
        <div className="dashboard-layout">
            <div className="left-panel">
                <div className="assistant-container">

                    <div className="chat-history" ref={chatRef}>
                        <div className="messages">

                        {messages.map(msg => (
                            <MessageBox
                                key={msg.id}
                                message={msg}
                            />
                        ))}
                        </div>
                    </div>

                    <InputBox
                        input={input}
                        setInput={setInput}
                        setMessages={setMessages}
                        isLoading={isLoading}
                        setIsLoading={setIsLoading}
                    />
                </div>
            </div>


            <div className="right-panel">
                <div className="overview-container">

                        <p className="panel-title">Campus Overview</p>

                        <div className="overview-content">

                            <ShowLibrary
                                data={mcpData.library}
                            />

                            <ShowEvents
                                data={mcpData.events}
                            />

                            <ShowCafeteria
                                data={mcpData.cafeteria}
                            />

                            <ShowAcademics
                                data={mcpData.academics}
                            />
                        </div>
                </div>

            </div>

        </div>
    );
}