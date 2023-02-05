from app.model.task import Task, ILevel
from app.repository.base import Base
from sqlalchemy import asc,desc, case
from sqlalchemy.future import select
from app.config.db_config import db
from datetime import datetime
from sqlalchemy.sql import func

date_format = '%Y-%m-%d %H:%M:%S'

class TaskRepository(Base):
    model = Task

    @staticmethod
    async def find_by_project_id(proj_id:str):
        query = select(Task).where(Task.projectId == proj_id)
        return (await db.execute(query)).scalars().all() 

    @staticmethod
    async def find_by_level(proj_level:int):
        query = select(Task).where(Task.importantLevel == ILevel(proj_level))
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def find_by_due_date(proj_date:datetime):
        query = select(Task).where((func.date(Task.dueDate)) == proj_date.date() )
        return (await db.execute(query)).scalars().all() 

    @staticmethod
    async def find_by_create_date(proj_date:datetime):
        query = select(Task).where((func.date(Task.createDate)) == proj_date.date() )
        return (await db.execute(query)).scalars().all() 

    @staticmethod
    async def order_by_closest_date(proj_date:datetime):
        query = select(Task).where(Task.dueDate >= proj_date).order_by(Task.createDate.asc())
        return (await db.execute(query)).all()

    @staticmethod
    async def order_by_prior():
        query = select(Task).order_by(Task.importantLevel.asc())
        return (await db.execute(query)).all()     
    
    @staticmethod
    async def count_by_prior():
        query = select(Task.importantLevel, func.count(Task.id)).group_by(Task.importantLevel)
        return (await db.execute(query)).all() 

# TEST COMMAND
    # print((await TaskRepository.order_by_closest_date(datetime(2023,2,7)))[0][0].id)            
    # print((await TaskRepository.order_by_prior())[0][0].importantLevel)
    # print((await TaskRepository.count_by_prior()))