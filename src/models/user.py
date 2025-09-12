from pydantic import BaseModel, ConfigDict
from uuid import UUID

class User(BaseModel):
    id: UUID | None = None
    nickname: str
    fio: str
    email: str
    phone_number: str
    password: str

    model_config = ConfigDict(
        json_encoders={
            UUID: str
        },
        from_attributes=True
    )