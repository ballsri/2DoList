from typing import Generic, TypeVar
from sqlalchemy import update, delete
from sqlalchemy.future import select
from app.config.db_config import db, commit_rollback

# print(await ProjectRepository.create(id="x"*36,title="y"*5,description="x"*4))

T = TypeVar('T')

class Base:
    model: Generic[T]

    @classmethod
    async def create(cls, **arg):
        model = cls.model(**arg)
        db.add(model)
        await commit_rollback()
        return model

    @classmethod
    async def get_all(cls):
        return (await db.execute(select(cls.model))).scalars().all()

    @classmethod
    async def get_by_id(cls,model_id:str):
        model = cls.model
        query = select(cls.model).where(model.id == model_id)
        return (await db.execute(query)).scalars().all()

    @classmethod
    async def update_by_id(cls,model_id:str, **arg):
        model = cls.model
        query = update(model).where(model.id == model_id).values(**arg)
        await db.execute(query)
        await commit_rollback()

    @classmethod
    async def delete_by_id(cls,model_id:str):
        model = cls.model
        query = delete(model).where(model.id == model_id)
        await db.execute(query)
        await commit_rollback()
        