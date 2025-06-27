from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    open = "open"
    investigating = "investigating"
    resolved = "resolved"

class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: str
    status: Optional[StatusEnum] = StatusEnum.open

class IncidentResponse(IncidentCreate):
    id: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True