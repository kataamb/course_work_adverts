from __future__ import annotations
from abc import ABC, abstractmethod
from i_sql_builders.sql_types.sql_types import TextAndParams

class IUserSqlBuilder(ABC):
    @abstractmethod
    def create_user(self, user_data: dict) -> TextAndParams: ...

    @abstractmethod
    def create_customer(self, profile_id: int, rating: int = 0) -> TextAndParams: ...

    @abstractmethod
    def create_seller(self, profile_id: int, rating: int = 0) -> TextAndParams: ...

    @abstractmethod
    def delete_customer(self, profile_id: int) -> TextAndParams: ...

    @abstractmethod
    def delete_seller(self, profile_id: int) -> TextAndParams: ...

    @abstractmethod
    def delete_profile(self, profile_id: int) -> TextAndParams: ...

    @abstractmethod
    def find_by_email(self, email: str) -> TextAndParams: ...