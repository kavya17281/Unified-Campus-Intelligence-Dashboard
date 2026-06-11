Prerequisites

Python 3.10+
FastAPI
Uvicorn

Run main server
uvicorn main:app --reload


Run All MCP Services

Open 4 separate terminals.

cd mcp/library_api
uvicorn library_api:app --reload --port 8001

cd mcp/event_api
uvicorn event_api:app --reload --port 8002

cd mcp/cafeteria_api
uvicorn cafeteria_api:app --reload --port 8003

cd mcp/academic_api
uvicorn academic_api:app --reload --port 8004




Library     http://localhost:8001
Events      http://localhost:8002
Cafeteria   http://localhost:8003
Academic    http://localhost:8004


run the frontend
cd frontend
npm run dev

cd frontend
npm run build

http://localhost:5173/