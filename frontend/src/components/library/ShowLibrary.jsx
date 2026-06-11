import LibraryCard from "./LibraryCard";
import { normalizeToArray }
from "../../utils/normalize";

export default function ShowLibrary({ data }) {

    const list =
        normalizeToArray(data);

    return (
        <div className="overview-section">
            <h3>Library</h3>

            {list.map(item => (
                <LibraryCard
                    key={item.id}
                    item={item}
                />
            ))}
        </div>
    );
}