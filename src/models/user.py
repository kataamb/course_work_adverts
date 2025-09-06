from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    nickname: str
    fio: str
    email: str
    phone_number: str
    password: str
