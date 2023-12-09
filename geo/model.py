from pydantic import BaseModel

class GeoItem(BaseModel):
  id: int
  sido: str
  sigungu: str
  dong: str