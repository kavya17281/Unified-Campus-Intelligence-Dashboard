import AcademicDayCard from "./AcademicDayCard";

export default function ShowAcademics( {data} ) {

    if (!data)
        return null;

    return (
        <div className="overview-section">
            <h3>Academics</h3>

            {Object.entries(data).map(
                ([day, sessions]) => (
                    <AcademicDayCard
                        key={day}
                        day={day}
                        sessions={sessions}
                    />
                )
            )}
        </div>
    );
}