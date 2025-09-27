from fastapi import FastAPI, HTTPException, Depends, Query
from typing import List, Optional
from models import Report, ReportCreate, ReportResponse
from database import db_manager
from auth import verify_api_key

app = FastAPI(
    title="Intelligence Reports API",
    description="A REST API for managing intelligence reports",
    version="1.0.0"
)

@app.post("/report", response_model=ReportResponse, status_code=201)
async def create_report(
    report_data: ReportCreate,
    api_key: str = Depends(verify_api_key)
):
    """
    Create a new intelligence report
    
    Args:
        report_data (ReportCreate): Report data containing:
            - title (str): Report title
            - content (str): Report content/body
            - tags (List[str]): List of tags for categorization
        api_key (str): Valid API key for authentication
    
    Returns:
        ReportResponse: Created report with:
            - id (str): Unique report identifier
            - title (str): Report title
            - content (str): Report content
            - tags (List[str]): Associated tags
            - date (str): Creation timestamp in ISO format
    
    Raises:
        HTTPException: 401 if API key is invalid
        HTTPException: 422 if request data is malformed
    """    
    report = db_manager.create_report(report_data)
    return ReportResponse(
        id=str(report.id),
        title=report.title,
        content=report.content,
        tags=report.tags,
        date=report.date.isoformat()
    )

@app.get("/report/{report_id}", response_model=ReportResponse)
async def get_report(
    report_id: str,
    api_key: str = Depends(verify_api_key)
):
    """Fetch a specific intelligence report by ID"""
    report = db_manager.get_report(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return ReportResponse(
        id=str(report.id),
        title=report.title,
        content=report.content,
        tags=report.tags,
        date=report.date.isoformat()
    )

@app.get("/reports", response_model=List[ReportResponse])
async def get_reports(
    tag: Optional[str] = Query(None, description="Filter reports by tag"),
    search: Optional[str] = Query(None, description="Search in report title and content"),
    api_key: str = Depends(verify_api_key)
):
    """List all intelligence reports with optional filtering"""
    reports = db_manager.get_reports(tag=tag, search=search)
    return [
        ReportResponse(
            id=str(report.id),
            title=report.title,
            content=report.content,
            tags=report.tags,
            date=report.date.isoformat()
        )
        for report in reports
    ]

@app.get("/health")
async def health_check():
    """Health check endpoint (no auth required)"""
    return {"status": "healthy", "service": "Intelligence Reports API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
