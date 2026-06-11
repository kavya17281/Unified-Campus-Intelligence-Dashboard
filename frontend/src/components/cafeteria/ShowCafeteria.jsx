import CafeteriaCard from "./CafeteriaCard";
import { normalizeToArray }
from "../../utils/normalize";

export default function ShowCafeteria({
    data
}) {

    const list =
        normalizeToArray(data);

    return (
        <div>
            <h3>Cafeteria</h3>

            {list.map(item => (
                <CafeteriaCard
                    key={item.id}
                    item={item}
                />
            ))}
        </div>
    );
}