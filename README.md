# Unified Campus Intelligence Dashboard

## Project Description

Unified Campus Intelligence Dashboard is an AI-powered campus assistant designed to provide students with a single interface for accessing information about campus services. Instead of navigating multiple systems, users can ask questions in natural language and receive accurate responses about library resources, campus events, academics, and cafeteria services.

The system combines specialized AI agents with modular MCP (Model Context Protocol) APIs to retrieve structured information and generate contextual responses.


Remark:
This project uses fake data inside APIS.
The page first gathers all data from API's to display on the right panel.
But each time a command is sent the assistant, it calls the API to fetch the desired data.
---

## Features

### AI-Powered Conversational Interface

* Natural language question answering
* Intelligent query routing
* Fetches data from the API's

### Library Services

* Book search and availability
* Shelf location lookup
* Library information retrieval

### Campus Events

* Event discovery
* Upcoming activities
* Event schedules and details

### Academic Information

* Course-schedule information
* Exam schedule
* Cancelled and postponed classes included

### Cafeteria Services

* Menu information
* Food availability
* Cost related information

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
│   └── public/
│
├── backend/
│   ├── agents/
│   ├── router/
│   └── shared/
│   └── tools/
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
git clone https://github.com/kavya17281/Unified-Campus-Intelligence-Dashboard.git
cd Unified-Campus-Intelligence-Dashboard
```

You would need to make a .env file inside backend folder with
GROQ_API_KEY="<YOUR_API_KEY>"

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

Open 4 new terminals, and in each terminal
```bash
uvicorn mcp.library_api.library_api:app --reload --port 8001
```

```bash
uvicorn mcp.event_api.event_api:app --reload --port 8002
```

```bash
uvicorn mcp.cafeteria_api.cafeteria_api:app --reload --port 8003
```

```bash
uvicorn mcp.academic_api.academic_api:app --reload --port 8004
```

also in backend/config.py comment all hosted links and use the local server links

### 6. Run Main Application

In a new terminal

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

Remark:
The application might take some time to start.
Wait until the Campus Overview is filled with data.
---

## Future Improvements

* User authentication
* Database integration
* Conversation memory
* Additional campus services
* Analytics dashboard
* Calender for academics data

---

## Author

Kavya

Built to explore:

* Agentic AI systems
* MCP architecture
* FastAPI microservices
* AI-assisted campus information systems
* Full-stack application deployment
