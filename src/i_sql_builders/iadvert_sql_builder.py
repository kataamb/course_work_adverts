from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from models.advert import Advert
from i_sql_builders.sql_types.sql_types import TextAndParams

class IAdvertSqlBuilder(ABC):
    @abstractmethod
    def create(self, advert: Advert) -> TextAndParams: ...

    @abstractmethod
    def get_by_id(self, advert_id: int) -> TextAndParams: ...

    @abstractmethod
    def get_all(self) -> TextAndParams: ...

    @abstractmethod
    def get_by_user(self, user_id: int) -> TextAndParams: ...

    @abstractmethod
    def is_created(self, user_id: int, advert_id: int) -> TextAndParams: ...

    @abstractmethod
    def search_by_keyword(self, keyword_like: str) -> TextAndParams: ...

    @abstractmethod
    def filter_by_dates(self, begin: datetime, end: datetime) -> TextAndParams: ...

    @abstractmethod
    def by_category(self, category_id: int) -> TextAndParams: ...

    @abstractmethod
    def delete(self, advert_id: int, user_id: int) -> TextAndParams: ...