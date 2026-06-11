import EventCard from "./EventCard";
import { normalizeToArray }
from "../../utils/normalize";

export default function ShowEvents({ data }) {

    const list =
        normalizeToArray(data);

    return (
        <div>
            <h3>Events</h3>

            {list.map(item => (
                <EventCard
                    key={item.id}
                    item={item}
                />
            ))}
        </div>
    );
}