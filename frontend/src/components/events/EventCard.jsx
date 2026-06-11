import { cardStyle } from "../../utils/cardStyle";

export default function EventCard({ item }) {

    return (
        <div style={cardStyle}>
            <p><b>{item.title}</b></p>

            <p>{item.date} | {item.start_time} - {item.end_time}</p>

            <p>{item.venue} | {item.category}</p>

            <p>{item.description}</p>

            <p>Club: {item.club}</p>

            {item.refreshments && (
                <p>Refreshments: {item.refreshments}</p>
            )}

            <p>
                {item.registration_required
                    ? "Registration Required"
                    : "Open Entry"}
            </p>
        </div>
    );
}