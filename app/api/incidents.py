from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, database
from app.schemas import incident as incident_schema
from app.core.security import get_current_user, is_admin
from uuid import uuid4
from typing import List, Optional

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("/", response_model=incident_schema.IncidentResponse)
def create_incident(
    incident: incident_schema.IncidentCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    new_incident = models.Incident(
        id=str(uuid4()),
        title=incident.title,
        description=incident.description,
        severity=incident.severity,
        status=incident.status,
        owner_id=current_user.id,
    )
    db.add(new_incident)
    db.commit()
    db.refresh(new_incident)
    return new_incident

@router.get("/", response_model=List[incident_schema.IncidentResponse])
def list_incidents(
    severity: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    query = db.query(models.Incident)
    if severity:
        query = query.filter(models.Incident.severity == severity)
    if status:
        query = query.filter(models.Incident.status == status)
    return query.limit(limit).all()

@router.delete("/{incident_id}", status_code=204)
def delete_incident(
    incident_id: str,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can delete incidents")
    incident = db.query(models.Incident).filter(models.Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    db.delete(incident)
    db.commit()