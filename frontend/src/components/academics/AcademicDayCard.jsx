export default function AcademicDayCard( {day, sessions} ) {

    return (
        <div className="overview-card">

            <h3>
                {day.charAt(0).toUpperCase() +
                    day.slice(1)}
            </h3>

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