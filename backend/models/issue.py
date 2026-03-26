from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class IssueCreate(BaseModel):
    title: str
    description: str
    category: str
    image_url: Optional[str] = None

class IssueUpdate(BaseModel):
    status: str  # "reported" or "resolved"

class IssueOut(BaseModel):
    id: UUID
    title: str
    description: str
    category: str
    image_url: Optional[str] = None
    status: str
    created_at: datetime
