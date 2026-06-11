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

        const botMessage = {
            message: data.response,
            sender: "robot",
            time: new Date().toLocaleTimeString(),
            id: crypto.randomUUID()
        };

        setMessages(prev => [...prev, botMessage]);

        setInput("");
    }

    return (
        <>
            <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="type your message"
            />

            <button onClick={handleSend}>
                Send
            </button>
        </>
    );
}