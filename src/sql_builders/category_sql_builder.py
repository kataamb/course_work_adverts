from __future__ import annotations
from sqlalchemy import text
from i_sql_builders.icategory_sql_builder import ICategorySqlBuilder
from i_sql_builders.sql_types.sql_types import TextAndParams

class CategorySqlBuilder(ICategorySqlBuilder):
    def get_all(self) -> TextAndParams:
        return text("SELECT * FROM adv.categories"), {}

    def get_name_by_id(self, id_category: int) -> TextAndParams:
        return text("SELECT name FROM adv.categories WHERE id = :id"), {"id": id_category}