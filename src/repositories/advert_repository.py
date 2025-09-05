from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from abstract_repositories.iadvert_repository import IAdvertRepository
from i_sql_builders.iadvert_sql_builder import IAdvertSqlBuilder
from models.advert import Advert
from datetime import datetime

class AdvertsRepository(IAdvertRepository):
    def __init__(self, session: AsyncSession, builder: IAdvertSqlBuilder):
        self.session = session
        self.builder = builder

    async def create(self, advert: Advert) -> Optional[Advert]:
        try:
            sql, params = self.builder.create(advert)
            result = await self.session.execute(sql, params)
            row = result.mappings().first()
            await self.session.commit()
            return Advert(**row) if row else None
        except IntegrityError:
            await self.session.rollback()
            return None
        except SQLAlchemyError:
            await self.session.rollback()
            return None

    async def get_by_id(self, advert_id: int) -> Optional[Advert]:
        try:
            sql, params = self.builder.get_by_id(advert_id)
            result = await self.session.execute(sql, params)
            row = result.mappings().first()
            return Advert(**row) if row else None
        except SQLAlchemyError:
            return None

    async def get_all_adverts(self) -> List[Advert]:
        try:
            sql, params = self.builder.get_all()
            result = await self.session.execute(sql, params)
            return [Advert(**r) for r in result.mappings()]
        except SQLAlchemyError:
            return []

    async def get_advert_by_user(self, user_id: int) -> List[Advert]:
        try:
            sql, params = self.builder.get_by_user(user_id)
            result = await self.session.execute(sql, params)
            return [Advert(**r) for r in result.mappings()]
        except SQLAlchemyError:
            return []

    async def is_created(self, user_id: int, advert_id: int) -> bool:
        sql, params = self.builder.is_created(user_id, advert_id)
        result = await self.session.execute(sql, params)
        return result.first() is not None

    async def get_adverts_by_key_word(self, key_word: str) -> List[Advert]:
        try:
            sql, params = self.builder.search_by_keyword(f"%{key_word}%")
            result = await self.session.execute(sql, params)
            return [Advert(**r) for r in result.mappings()]
        except SQLAlchemyError:
            return []

    async def get_adverts_by_filter(self, begin_time: datetime, end_time: datetime) -> List[Advert]:
        try:
            sql, params = self.builder.filter_by_dates(begin_time, end_time)
            result = await self.session.execute(sql, params)
            return [Advert(**r) for r in result.mappings()]
        except SQLAlchemyError:
            return []

    async def get_adverts_by_category(self, category_id: int) -> List[Advert]:
        try:
            sql, params = self.builder.by_category(category_id)
            result = await self.session.execute(sql, params)
            return [Advert(**r) for r in result.mappings()]
        except SQLAlchemyError:
            return []

    async def delete_advert(self, advert_id: int, user_id: int) -> None:
        try:
            sql, params = self.builder.delete(advert_id, user_id)
            await self.session.execute(sql, params)
            await self.session.commit()
        except SQLAlchemyError:
            await self.session.rollback()
