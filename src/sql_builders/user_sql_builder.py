# i_sql_builders/user_sql_builder.py
from __future__ import annotations
from sqlalchemy import text
from i_sql_builders.iuser_sql_builder import IUserSqlBuilder
from i_sql_builders.sql_types.sql_types import TextAndParams, SqlParams

class UserSqlBuilder(IUserSqlBuilder):
    def create_user(self, user_data: dict) -> TextAndParams:
        sql = text("""
            INSERT INTO adv.profiles (id, nickname, fio, email, phone_number, password)
            VALUES ((SELECT COALESCE(MAX(id), 0) + 1 FROM adv.profiles), :nickname, :fio, :email, :phone_number, :password)
            RETURNING id, nickname, fio, email, phone_number, password
        """)
        params: SqlParams = {
            "nickname": user_data["nickname"],
            "fio": user_data["fio"],
            "email": user_data["email"],
            "phone_number": user_data["phone_number"],
            "password": user_data["password"]
        }
        return sql, params

    def create_customer(self, profile_id: int, rating: int = 0) -> TextAndParams:
        sql = text("""
            INSERT INTO adv.customers (id, profile_id, rating)
            VALUES ((SELECT COALESCE(MAX(id), 0) + 1 FROM adv.customers), :profile_id, :rating)
        """)
        return sql, {"profile_id": profile_id, "rating": rating}

    def create_seller(self, profile_id: int, rating: int = 0) -> TextAndParams:
        sql = text("""
            INSERT INTO adv.sellers (id, profile_id, rating)
            VALUES ((SELECT COALESCE(MAX(id), 0) + 1 FROM adv.sellers), :profile_id, :rating)
        """)
        return sql, {"profile_id": profile_id, "rating": rating}

    def delete_customer(self, profile_id: int) -> TextAndParams:
        return text("DELETE FROM adv.customers WHERE profile_id = :id"), {"id": profile_id}

    def delete_seller(self, profile_id: int) -> TextAndParams:
        return text("DELETE FROM adv.sellers WHERE profile_id = :id"), {"id": profile_id}

    def delete_profile(self, profile_id: int) -> TextAndParams:
        return text("DELETE FROM adv.profiles WHERE id = :id"), {"id": profile_id}

    def find_by_email(self, email: str) -> TextAndParams:
        return text("SELECT * FROM adv.profiles WHERE email = :email"), {"email": email}