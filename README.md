# Intelligence Reports API

A REST API service for managing intelligence reports built with FastAPI.

## Features

- Create, read, and list intelligence reports
- Tag-based filtering and text search
- API key authentication
- SQLite database storage
- Docker containerization
- Professional error handling

## Quick Start

### Local Development

#### 1. Create a virtual environment 

It is best practice to use a **virtual environment** so dependencies are isolated from the system Python.

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

#### 2. Run the server
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Docker

  - [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running  
    (on Windows it requires **WSL2** enabled)


1. Build the image:
```bash
docker build -t intelligence-reports-api .
```

2. Run the container:
```bash
docker run -p 8000:8000 -e API_KEY="Ran's-BE-Project" intelligence-reports-api
```

## API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`

---

## Swagger UI

When you open [http://localhost:8000/docs](http://localhost:8000/docs) in Chrome you see **Swagger UI**, an interactive documentation tool.  

- **Top bar**: API title and version  
- **Authorize button (🔒)**: Click to enter your API key once, so all requests will automatically include it.  
  - Enter: `Ran's-BE-Project`  
  - Press **Authorize** → **Close**  
- **Endpoints list**: Each endpoint (`POST /report`, `GET /reports`, etc.) shows description, parameters, request body, and possible responses.  
- **Try it out**: Lets you send real requests directly from the browser.

---


## Authentication

All endpoints (except `/health`) require an API key passed as a Bearer token in the Authorization header.

Default API key: `Ran's-BE-Project`

Set custom API key using environment variable:
```bash
export API_KEY=Ran's-BE-Project
```

## API Endpoints

### POST /report
Create a new intelligence report.

**Headers:**
```
Authorization: Bearer Ran's-BE-Project
Content-Type: application/json
```

**Request Body:**
```json
{
    "title": "Security Incident Report",
    "content": "Detailed description of the security incident...",
    "tags": ["security", "incident", "urgent"]
}
```

### GET /report/{id}
Fetch a specific report by ID.

**Headers:**
```
Authorization: Bearer Ran's-BE-Project
```

### GET /reports
List all reports with optional filtering.

**Query Parameters:**
- `tag`: Filter by tag (e.g., `?tag=security`)
- `search`: Search in title and content (e.g., `?search=incident`)

**Headers:**
```
Authorization: Bearer Ran's-BE-Project
```

### GET /health
Health check endpoint (no authentication required).

## Testing Examples

### Using curl

1. **Create a report:**
```bash
curl -X POST "http://localhost:8000/report"   -H "Authorization: Bearer Ran's-BE-Project"   -H "Content-Type: application/json"   -d '{
    "title": "Network Breach Investigation",
    "content": "Suspicious network activity detected on server farm alpha. Initial investigation reveals potential unauthorized access attempt.",
    "tags": ["security", "network", "investigation"]
  }'
```

2. **Get all reports:**
```bash
curl -X GET "http://localhost:8000/reports"   -H "Authorization: Bearer Ran's-BE-Project"
```

3. **Filter by tag:**
```bash
curl -X GET "http://localhost:8000/reports?tag=security"   -H "Authorization: Bearer Ran's-BE-Project"
```

4. **Search reports:**
```bash
curl -X GET "http://localhost:8000/reports?search=network"   -H "Authorization: Bearer Ran's-BE-Project"
```

5. **Get specific report:**
```bash
curl -X GET "http://localhost:8000/report/{report-id}"   -H "Authorization: Bearer Ran's-BE-Project"
```

### Using Postman

1. Set up environment variable `API_KEY` = `Ran's-BE-Project`
2. Add Authorization header: `Bearer {{API_KEY}}`
3. Use the endpoints as described above

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

## Database

The application uses SQLite for data persistence. The database file `reports.db` will be created automatically in the project directory.

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `201`: Created
- `401`: Unauthorized (invalid API key)
- `404`: Not Found
- `422`: Validation Error

---

## Running with Docker vs. Local Development

- **Docker**: Runs the application inside an isolated container, independent of your system.  
  - Ensures consistent environment ("works on my machine" problem solved)  
  - Easy to deploy on servers or share with others  
  - Requires Docker Desktop running in the background  

- **Local (venv)**: Runs directly on your own Python environment.  
  - Easier for fast development and debugging (with hot reload)  
  - Depends on your local Python and libraries  
  - Best for coding and testing during development

