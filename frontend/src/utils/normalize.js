export function normalizeToArray(data) {

    if (!data) return [];

    if (Array.isArray(data))
        return data;

    if (typeof data === "object")
        return Object.values(data).flat();

    return [];
}