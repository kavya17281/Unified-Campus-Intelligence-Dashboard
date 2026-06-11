import { cardStyle } from "../../utils/cardStyle";

export default function CafeteriaCard({ item }) {

    return (
        <div style={cardStyle}>
            <p><b>{item.name}</b></p>

            <p>Category: {item.category}</p>

            <p>Price: ₹{item.price}</p>

            <p>
                {item.is_veg
                    ? "Vegetarian"
                    : "Non-Vegetarian"}
            </p>

            <p>
                Status: {item.available
                    ? "Available"
                    : "Not Available"}
            </p>
        </div>
    );
}