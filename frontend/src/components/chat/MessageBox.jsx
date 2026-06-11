export default function MessageBox({ message }) {

    if (message.sender === "user") {
        return (
            <div className="user-message">
                <div className="message-header">
                    <b>{message.sender}</b>

                    <small className="message-time">
                        {message.time}
                    </small>
                </div>
                <p>{message.message}</p>
            </div>
        );
    }

    return (
        <div className="bot-message">
            <div className="message-header">
                <b>{message.sender}</b>

                <small className="message-time">
                    {message.time}
                </small>
            </div>
            <p>{message.message}</p>
        </div>
    );
}