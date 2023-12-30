from typing import Optional
from pydantic import BaseModel

class Agency(BaseModel):
  id: int
  geo_id: int
  agency_id: int
  등록번호: str
  상호: str
  소재지: str
  대표자: str
  등록일자: str
  상태: str 
  행정처분시작일자: Optional[str]
  행정처분종료일자: Optional[str]