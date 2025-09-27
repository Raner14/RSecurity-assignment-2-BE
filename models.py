from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import UUID, uuid4

class ReportCreate(BaseModel):
    title: str
    content: str = Field(..., min_length=1)
    tags: List[str] = Field(default_factory=list)

class Report(BaseModel):
    id: UUID
    title: str
    content: str
    tags: List[str]
    date: datetime
    

class ReportResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: List[str]
    date: str
