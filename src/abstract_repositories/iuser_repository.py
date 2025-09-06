from abc import ABC, abstractmethod
from models.user import User
from typing import Optional

class IUserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> Optional[User]: ...

    @abstractmethod
    async def delete(self, profile_id: int) -> bool: ...

    @abstractmethod
    async def find_by_email(self, email: str) -> User | None: ...


