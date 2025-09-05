from __future__ import annotations
from abc import ABC, abstractmethod
from i_sql_builders.sql_types.sql_types import TextAndParams

class IDealSqlBuilder(ABC):
    @abstractmethod
    def create_deal(self, user_id: int, advert_id: int, address: str = "online") -> TextAndParams: ...

    @abstractmethod
    def get_deals_by_user(self, user_id: int) -> TextAndParams: ...

    @abstractmethod
    def is_in_deals(self, user_id: int, advert_id: int) -> TextAndParams: ...