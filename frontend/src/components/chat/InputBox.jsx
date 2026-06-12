export default function InputBox( {input, setInput, setMessages, isLoading, setIsLoading} ){

    async function handleSend() {

        if (input.trim() === "")
            return;

        setIsLoading(true);

        try {
            const userMessage = {
                message: input,
                sender: "user",
                time: new Date().toLocaleTimeString(),
                id: crypto.randomUUID()
            };

            setMessages(prev => [...prev, userMessage]);

            const response = await fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message: input})
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

        } finally { setIsLoading(false) }

    }

    return (
        <div className="chat-input-container">
            <div className="chat-input-bar">
            <input
                disabled={isLoading}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                    console.log("Pressed:", e.key);
                    if (e.key === "Enter") {
                        e.preventDefault();
                        handleSend();
                    }
                }}
                placeholder="type your message"
                className="chat-input"
            />

            <button 
                onClick={handleSend} 
                className="send-button"
                disabled={isLoading}
            >
                {isLoading ? "Thinking..." : "Send"}
            </button>
            </div>
        </div>
    );
}