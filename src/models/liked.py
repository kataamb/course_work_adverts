from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class Liked(BaseModel):
    id: UUID
    id_customer: int
    id_advert: int
    date_created: Optional[datetime] = None