from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Advert(BaseModel):
    id: int | None = None
    content: str
    description: str
    id_category: int
    price: int
    id_seller: int
    date_created: Optional[datetime] = None
