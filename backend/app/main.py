from fastapi import FastAPI, HTTPException
from app import models, database, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Solar System API"}

@app.post("/planets/")
def create_planet(planet: models.PlanetCreate):
    return crud.create_planet(planet)

@app.get("/planets/")
def list_planets():
    return crud.get_planets()

@app.post("/satellites/")
def create_satellite(satellite: models.SatelliteCreate):
    return crud.create_satellite(satellite)

@app.get("/satellites/")
def list_satellites():
    return crud.get_satellites()
