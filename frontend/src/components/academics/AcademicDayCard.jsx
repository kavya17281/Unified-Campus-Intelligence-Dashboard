export default function AcademicDayCard( {day, sessions} ) {

    return (
        <div
            style={{
                border: "1px solid #ccc",
                padding: "12px",
                marginBottom: "15px",
                borderRadius: "8px"
            }}
        >
            <h4>
                {day.charAt(0).toUpperCase() +
                    day.slice(1)}
            </h4>

            {sessions.map((session, index) => (
                <div
                    key={index}
                    style={{
                        marginBottom: "10px"
                    }}
                >
                    <p><b>{session.subject}</b></p>

                    <p>{session.time}</p>

                    <p>{session.type} | {session.room}</p>
                </div>
            ))}
        </div>
    );
}