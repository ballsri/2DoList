from typing import Generic, TypeVar
from sqlalchemy import update, delete
from sqlalchemy.future import select
from app.config.db_config import db



T = TypeVar('T')

class Base:
    model: Generic[T]

    @classmethod
    def create()