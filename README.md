# Unified Campus Intelligence Dashboard

## Project Description

Unified Campus Intelligence Dashboard is an AI-powered campus assistant designed to provide students with a single interface for accessing information about campus services. Instead of navigating multiple systems, users can ask questions in natural language and receive accurate responses about library resources, campus events, academics, and cafeteria services.

The system combines specialized AI agents with modular MCP (Model Context Protocol) APIs to retrieve structured information and generate contextual responses.


Remark: This project uses fake data inside APIS.
---

## Features

### AI-Powered Conversational Interface

* Natural language question answering
* Intelligent query routing
* Context-aware responses

### Library Services

* Book search and availability
* Shelf location lookup
* Library information retrieval

### Campus Events

* Event discovery
* Upcoming activities
* Event schedules and details

### Academic Information

* Course-related information
* Academic resources
* Department and campus data

### Cafeteria Services

* Menu information
* Food availability
* Dining-related queries

### Dashboard Overview

* Aggregated campus information
* Unified data access
* Real-time API integration

### Modular Architecture

* Independent MCP services
* Agent-based design
* Scalable backend structure

---

## System Architecture

User Query
↓
Router Agent
↓
Specialized Agent Selection
├── Library Agent
├── Events Agent
├── Academics Agent
└── Cafeteria Agent
↓
MCP APIs
↓
Structured Campus Data
↓
Natural Language Response

---

## Tech Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* Python
* FastAPI

### AI Layer

* Groq LLM
* Agent-based Routing

### APIs

* MCP Architecture
* REST APIs

### Deployment

* Render

---

## Project Structure

```text
project/
├── frontend/
│   ├── src/
│   └── dist/
│
├── backend/
│   ├── agents/
│   ├── router/
│   └── ...
│
├── mcp/
│   ├── library_api/
│   ├── events_api/
│   ├── academics_api/
│   └── cafeteria_api/
│
├── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 4. Build Frontend

```bash
npm run build
```

### 5. Run MCP Services

Start the individual MCP API services.

### 6. Run Main Application

```bash
uvicorn main:app --reload
```

### 7. Open Application

Navigate to:

```text
http://localhost:8000
```

---

## Deployed Demo

Main Application:

[INSERT DEPLOYED DEMO LINK HERE]

MCP Services:

* Library MCP
* Events MCP
* Academics MCP
* Cafeteria MCP

---

## Future Improvements

* User authentication
* Database integration
* Conversation memory
* Real-time notifications
* Additional campus services
* Analytics dashboard

---

## Author

Kavya

Built to explore:

* Agentic AI systems
* MCP architecture
* FastAPI microservices
* AI-assisted campus information systems
* Full-stack application deployment














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




uvicorn mcp.event_api.event_api:app --host 0.0.0.0 --port 10000
pip install -r mcp/event_api/requirements.txt

uvicorn mcp.cafeteria_api.cafeteria_api:app --host 0.0.0.0 --port 10000
pip install -r mcp/cafeteria_api/requirements.txt

uvicorn mcp.academic_api.academic_api:app --host 0.0.0.0 --port 10000
pip install -r mcp/academic_api/requirements.txt