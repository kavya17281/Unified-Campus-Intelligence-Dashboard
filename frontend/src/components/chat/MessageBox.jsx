export default function MessageBox({ message }) {

    return (
        <div>
            <b>{message.sender}</b>
            <small>{message.time}</small>
            <p>{message.message}</p>
        </div>
    );
}