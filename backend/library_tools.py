from backend.mcp.library_api.library_service import (
    get_availability,
    get_author,
    get_summary
)

TOOLS = {
    "get_availability": get_availability,
    "get_author": get_author,
    "get_summary": get_summary
}