from typing import Optional
from pydantic import BaseModel

class Review(BaseModel):
  id: int
  agency_id: int
  username: str
  point: int
  date: str
  text: Optional[str]