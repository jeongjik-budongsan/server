from typing import Optional

from geo.list import fetch_geo
from geo.model import GeoItem
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
