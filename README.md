Prerequisites

Python 3.10+
FastAPI
Uvicorn

Run main server
cd backend
uvicorn main:app --reload


Run All MCP Services

Open 4 separate terminals.

cd backend/mcp/library_api
uvicorn library_api:app --reload --port 8001

cd backend/mcp/event_api
uvicorn event_api:app --reload --port 8002

cd backend/mcp/cafeteria_api
uvicorn cafeteria_api:app --reload --port 8003

cd backend/mcp/academic_api
uvicorn academic_api:app --reload --port 8004




Library     http://localhost:8001
Events      http://localhost:8002
Cafeteria   http://localhost:8003
Academic    http://localhost:8004

