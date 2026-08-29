import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, Text
from database import Base

class LocationPoint(Base):
    __tablename__ = "location_points"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude = Column(Float, nullable=True)
    accuracy = Column(Float, nullable=True)
    speed = Column(Float, nullable=True)
    heading = Column(Float, nullable=True)
    activity_type = Column(String, nullable=True)  # stationary, walking, running, automotive, cycling
    battery_level = Column(Float, nullable=True)
    is_charging = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, index=True)

class Geofence(Base):
    __tablename__ = "geofences"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    radius_meters = Column(Float, default=100.0)
    description = Column(Text, nullable=True)
    notify_on_entry = Column(Boolean, default=True)
    notify_on_exit = Column(Boolean, default=True)
