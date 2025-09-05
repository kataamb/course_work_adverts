from __future__ import annotations
from datetime import datetime
from sqlalchemy import text
from models.advert import Advert
from i_sql_builders.iadvert_sql_builder import IAdvertSqlBuilder
from i_sql_builders.sql_types.sql_types import TextAndParams, SqlParams

class AdvertsSqlBuilder(IAdvertSqlBuilder):
    def create(self, advert: Advert) -> TextAndParams:
        sql = text("""
            INSERT INTO adv.adverts (content, description, id_category, price, status, id_seller)
            VALUES (:content, :description, :id_category, :price, :status, :id_seller)
            RETURNING id, content, description, id_category, price, status, id_seller, date_created
        """)
        params: SqlParams = {
            "content": advert.content,
            "description": advert.description,
            "id_category": advert.id_category,
            "price": advert.price,
            "status": advert.status,
            "id_seller": advert.id_seller,
        }
        return sql, params

    def get_by_id(self, advert_id: int) -> TextAndParams:
        return text("SELECT * FROM adv.adverts WHERE id = :id"), {"id": advert_id}

    def get_all(self) -> TextAndParams:
        return text("SELECT * FROM adv.adverts ORDER BY date_created DESC"), {}

    def get_by_user(self, user_id: int) -> TextAndParams:
        return (
            text("SELECT * FROM adv.adverts WHERE id_seller = :user_id ORDER BY date_created DESC"),
            {"user_id": user_id},
        )

    def is_created(self, user_id: int, advert_id: int) -> TextAndParams:
        return (
            text("SELECT 1 FROM adv.adverts WHERE id_seller = :uid AND id = :aid LIMIT 1"),
            {"uid": user_id, "aid": advert_id},
        )

    def search_by_keyword(self, keyword_like: str) -> TextAndParams:
        return text("SELECT * FROM adv.search_adverts(:kw)"), {"kw": keyword_like}

    def filter_by_dates(self, begin: datetime, end: datetime) -> TextAndParams:
        sql = text("""
            SELECT * FROM adv.adverts 
            WHERE date_created BETWEEN :begin_time AND :end_time
            ORDER BY date_created DESC
        """)
        return sql, {"begin_time": begin, "end_time": end}

    def by_category(self, category_id: int) -> TextAndParams:
        return (
            text("SELECT * FROM adv.adverts WHERE id_category = :category_id ORDER BY date_created DESC"),
            {"category_id": category_id},
        )

    def delete(self, advert_id: int, user_id: int) -> TextAndParams:
        return (
            text("DELETE FROM adv.adverts WHERE id = :advert_id AND id_seller = :user_id"),
            {"advert_id": advert_id, "user_id": user_id},
        )