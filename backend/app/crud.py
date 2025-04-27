from app import models, database
from sqlalchemy.orm import Session

def create_planet(planet: models.PlanetCreate):
    db = next(database.get_db())
    db_planet = models.Planet(**planet.dict())
    db.add(db_planet)
    db.commit()
    db.refresh(db_planet)
    return db_planet

def get_planets():
    db = next(database.get_db())
    return db.query(models.Planet).all()

def create_satellite(satellite: models.SatelliteCreate):
    db = next(database.get_db())
    db_satellite = models.Satellite(**satellite.dict())
    db.add(db_satellite)
    db.commit()
    db.refresh(db_satellite)
    return db_satellite

def get_satellites():
    db = next(database.get_db())
    return db.query(models.Satellite).all()
