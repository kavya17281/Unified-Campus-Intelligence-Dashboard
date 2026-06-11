import { cardStyle } from "../../utils/cardStyle";

export default function LibraryCard({ item }) {

    return (
        <div className="overview-card">
            <p><b>{item.title}</b></p>

            <p>Author: {item.author}</p>

            <p>Category: {item.category}</p>

            <p>{item.summary}</p>

            <p>
                Copies: {item.copies}
                {" | "}
                Shelf: {item.shelf}
            </p>
        </div>
    );
}