from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
import datetime

from database import get_db
from models import LocationPoint
from config import settings

router = APIRouter(prefix="/location", tags=["location"])
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

class LocationPayload(BaseModel):
    device_id: str
    latitude: float
    longitude: float
    altitude: Optional[float] = None
    accuracy: Optional[float] = None
    speed: Optional[float] = None
    heading: Optional[float] = None
    activity_type: Optional[str] = "stationary"
    battery_level: Optional[float] = None
    is_charging: Optional[bool] = False
    timestamp: Optional[datetime.datetime] = None

class BatchLocationPayload(BaseModel):
    device_id: str
    locations: List[LocationPayload]

@router.post("/update", dependencies=[Depends(verify_api_key)])
async def update_location(payload: LocationPayload, db: AsyncSession = Depends(get_db)):
    loc = LocationPoint(
        device_id=payload.device_id,
        latitude=payload.latitude,
        longitude=payload.longitude,
        altitude=payload.altitude,
        accuracy=payload.accuracy,
        speed=payload.speed,
        heading=payload.heading,
        activity_type=payload.activity_type,
        battery_level=payload.battery_level,
        is_charging=payload.is_charging,
        timestamp=payload.timestamp or datetime.datetime.utcnow()
    )
    db.add(loc)
    await db.commit()
    return {"status": "success", "recorded_at": loc.timestamp}

@router.post("/batch", dependencies=[Depends(verify_api_key)])
async def batch_update_location(payload: BatchLocationPayload, db: AsyncSession = Depends(get_db)):
    count = 0
    for item in payload.locations:
        loc = LocationPoint(
            device_id=payload.device_id,
            latitude=item.latitude,
            longitude=item.longitude,
            altitude=item.altitude,
            accuracy=item.accuracy,
            speed=item.speed,
            heading=item.heading,
            activity_type=item.activity_type,
            battery_level=item.battery_level,
            is_charging=item.is_charging,
            timestamp=item.timestamp or datetime.datetime.utcnow()
        )
        db.add(loc)
        count += 1
    await db.commit()
    return {"status": "success", "inserted_count": count}

@router.get("/latest/{device_id}", dependencies=[Depends(verify_api_key)])
async def get_latest_location(device_id: str, db: AsyncSession = Depends(get_db)):
    stmt = select(LocationPoint).where(LocationPoint.device_id == device_id).order_by(LocationPoint.timestamp.desc()).limit(1)
    result = await db.execute(stmt)
    point = result.scalars().first()
    if not point:
        raise HTTPException(status_code=404, detail="No location recorded for device")
    return {
        "device_id": point.device_id,
        "latitude": point.latitude,
        "longitude": point.longitude,
        "altitude": point.altitude,
        "accuracy": point.accuracy,
        "activity": point.activity_type,
        "battery": point.battery_level,
        "timestamp": point.timestamp
    }
