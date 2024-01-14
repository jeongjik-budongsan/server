from typing import Optional

from agency.model import Agency
from agency.views import fetch_agencies
from geo.list import fetch_geo
from geo.model import GeoItem
from review.model import Review
from review.list import fetch_reviews
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://frontend-e9r.pages.dev/",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/geo")
async def geo() -> list[GeoItem]:
  response = fetch_geo()
  return response.data

@app.get("/agencies")
async def agencies(geo_id: int) -> list[Agency]:
  response = fetch_agencies(geo_id)
  return response.data

@app.get("/reviews")
async def reviews(agency_id: int) -> list[Review]:
  response = fetch_reviews(agency_id)
  return response.data