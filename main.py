from typing import Optional

from fastapi import FastAPI

from address.list import fetch_addresses

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/addresses")
async def addresses():
  return fetch_addresses()
