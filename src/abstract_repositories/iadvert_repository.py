from abc import ABC, abstractmethod
from typing import List, Optional
from models.advert import Advert
from datetime import datetime


class IAdvertRepository(ABC):
    @abstractmethod
    async def create(self, advert: Advert) -> Advert: ...
    @abstractmethod
    async def get_by_id(self, advert_id: int) -> Optional[Advert]: ...
    @abstractmethod
    async def get_all_adverts(self) -> List[Advert]: ...

    @abstractmethod
    async def get_advert_by_user(self, user_id: int) -> List[Advert]: ...

    @abstractmethod
    async def is_created(self, user_id: int, advert_id: int) -> bool: ...

    @abstractmethod
    async def get_adverts_by_key_word(self, key_word: str) -> List[Advert]: ...

    @abstractmethod
    async def get_adverts_by_filter(self, begin_time: datetime, end_time: datetime) -> List[Advert]: ...

    @abstractmethod
    async def get_adverts_by_category(self, category_id: int) -> List[Advert]: ...

    @abstractmethod
    async def delete_advert(self, advert_id: int, user_id: int) -> None: ...
