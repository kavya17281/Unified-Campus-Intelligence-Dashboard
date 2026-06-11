export default function InputBox( {input, setInput, setMessages} ){

    async function handleSend() {

        if (input.trim() === "")
            return;

        const userMessage = {
            message: input,
            sender: "user",
            time: new Date().toLocaleTimeString(),
            id: crypto.randomUUID()
        };

        setMessages(prev => [...prev, userMessage]);

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: input
            })
        });

        const data = await response.json();

        const assistantMessage = {
            message: data.response,
            sender: "assistant",
            time: new Date().toLocaleTimeString(),
            id: crypto.randomUUID()
        };

        setMessages(prev => [...prev, assistantMessage]);

        setInput("");
    }

    return (
        <div className="chat-input-container">
            <div className="chat-input-bar">
            <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="type your message"
                className="chat-input"
            />

            <button onClick={handleSend} className="send-button">
                Send
            </button>
            </div>
        </div>
    );
}