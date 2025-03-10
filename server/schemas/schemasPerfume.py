from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime
from typing_extensions import Literal
class PerfumeSchema(BaseModel):
    id: Optional[int] = None
    scentIds: List[int] 
    name: str
    brand: str
    fragrance_notes: str
    price: float
    volume: int
    image_url:Optional[str] = None
    buy_url:str
    deleted:Optional[bool]=False
    deleted_on:Optional[datetime]=None

 
