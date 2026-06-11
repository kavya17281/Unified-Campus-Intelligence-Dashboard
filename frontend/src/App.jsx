import { useState } from "react";

import InputBox from "./components/chat/InputBox";
import MessageBox from "./components/chat/MessageBox";

import ShowLibrary from "./components/library/ShowLibrary";
import ShowEvents from "./components/events/ShowEvents";
import ShowCafeteria from "./components/cafeteria/ShowCafeteria";
import ShowAcademics from "./components/academics/ShowAcademics";

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

    const [messages, setMessages] =
        useState(messageData);

    const [input, setInput] =
        useState("");

    const [mcpData, setMcpData] =
        useState({
            library: [],
            events: [],
            cafeteria: [],
            academics: []
        });

    async function updateData() {

        const response =
            await fetch("/dashboard-data");

        const data =
            await response.json();

        setMcpData(data);
    }

    return (
        <>
            <InputBox
                input={input}
                setInput={setInput}
                setMessages={setMessages}
            />

            {messages.map(msg => (
                <MessageBox
                    key={msg.id}
                    message={msg}
                />
            ))}

            <button onClick={updateData}>
                Update Data
            </button>

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
        </>
    );
}