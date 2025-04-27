from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Planet(Base):
    __tablename__ = "planets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    size = Column(Float)
    distance_from_sun = Column(Float)

    satellites = relationship("Satellite", back_populates="planet")

class Satellite(Base):
    __tablename__ = "satellites"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    planet_id = Column(Integer, ForeignKey("planets.id"))

    planet = relationship("Planet", back_populates="satellites")

class PlanetCreate(BaseModel):
    name: str
    size: float
    distance_from_sun: float

class SatelliteCreate(BaseModel):
    name: str
    type: str
    planet_id: int
