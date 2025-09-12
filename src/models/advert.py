from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class Advert(BaseModel):
    id: UUID | None  = None
    content: str
    description: str
    id_category: UUID
    price: int
    id_seller: UUID
    date_created:  datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True