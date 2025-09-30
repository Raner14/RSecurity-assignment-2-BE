# Intelligence Reports API

A REST API service for managing intelligence reports built with FastAPI.

## Features

- Create, read, and list intelligence reports
- Tag-based filtering and text search
- API key authentication
- SQLite database storage
- Docker containerization

## Quick Start

You can run this project in two ways:

### Option 1: Virtual Environment

**Best for:** Development with hot reload  
**Requirements:** Python 3.10+ installed

1. Create a virtual environment: 


**Windows (PowerShell):**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS / Linux (bash/zsh):**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To exit the virtual environment:
```bash
deactivate
```

2. Run the server
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Option 2: Docker

**Best for:** Production-like environment - runs the same everywhere  
**Requirements:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running (on Windows requires **WSL2**)

**What Docker does:** Creates a mini Linux computer with Python 3.10 and runs your app in complete isolation.


1. Build the image:
```bash
docker build -t intelligence-reports-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 -e API_KEY="Ran's-BE-Project" intelligence-reports-api
```

The API will be available at `http://localhost:8000`

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`

---

### Using Swagger UI

1. Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser
2. Click the **🔒 Authorize** button
3. Enter: `Ran's-BE-Project`
4. Click **Authorize** → **Close**
5. Now you can test all endpoints directly from the browser!

## API Endpoints (Quick Reference)

### Main Endpoints:
- `POST /report` - Create new report
- `GET /report/{id}` - Get specific report  
- `GET /reports` - List all reports (with filtering: `?tag=security&search=incident`)
- `GET /health` - Health check (no auth needed)

### Example Request Body for POST /report:
```json
{
    "title": "Cyber Attack Detection",
    "content": "Suspicious activity detected on network segment 192.168.1.0/24. Multiple failed login attempts from IP 10.0.0.15. Recommend immediate investigation.",
    "tags": ["security", "network", "urgent", "investigation"]
}
```

## Authentication

All endpoints (except `/health`) require API key: `Ran's-BE-Project`

## Project Structure

```
├── main.py          # FastAPI application
├── models.py        # Pydantic data models
├── database.py      # Database layer (SQLite)
├── auth.py          # Authentication middleware
├── requirements.txt # Python dependencies
├── Dockerfile       # Docker configuration
└── README.md        # This file
```

---

## Docker vs. Virtual Environment

- **Docker**: Isolated Linux environment - consistent everywhere, best for deployment
- **Virtual Environment**: Uses your local Python - faster for development with hot reload

