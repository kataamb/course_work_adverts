# i_sql_builders/deal_sql_builder.py
from __future__ import annotations
from sqlalchemy import text
from i_sql_builders.ideal_sql_builder import IDealSqlBuilder
from i_sql_builders.sql_types.sql_types import TextAndParams, SqlParams

class DealSqlBuilder(IDealSqlBuilder):
    def create_deal(self, user_id: int, advert_id: int, address: str = "online") -> TextAndParams:
        sql = text("""
            INSERT INTO adv.deals (id_customer, id_advert, address)
            VALUES (:id_customer, :id_advert, :address)
            RETURNING id, id_customer, id_advert, date_created, address, status
        """)
        params: SqlParams = {
            "id_customer": user_id,
            "id_advert": advert_id,
            "address": address
        }
        return sql, params

    def get_deals_by_user(self, user_id: int) -> TextAndParams:
        sql = text("""
            SELECT a.* 
            FROM adv.adverts a
            JOIN adv.deals d ON a.id = d.id_advert
            WHERE d.id_customer = :user_id
            ORDER BY a.date_created DESC
        """)
        return sql, {"user_id": user_id}

    def is_in_deals(self, user_id: int, advert_id: int) -> TextAndParams:
        return (
            text("SELECT 1 FROM adv.deals WHERE id_customer = :uid AND id_advert = :aid LIMIT 1"),
            {"uid": user_id, "aid": advert_id}
        )