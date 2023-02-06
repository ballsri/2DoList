from app.model.task import Task, TaskLevel, TaskStatus
from app.repository.base import Base
from sqlalchemy import asc,desc, case
from sqlalchemy.future import select
from app.config.db_config import db
from datetime import datetime
from sqlalchemy.sql import func
import uuid


class TaskRepository(Base):
    model = Task

    @staticmethod
    async def find_by_project_id(proj_id:uuid.UUID):
        query = select(Task).where(Task.projectId == proj_id)
        return (await db.execute(query)).scalars().all() 

    @staticmethod
    async def find_by_project_task(proj_id:uuid.UUID,task_id:uuid.UUID):
        query = select(Task).where(Task.projectId == proj_id, Task.id== task_id)
        return (await db.execute(query)).scalars().all() 

    @staticmethod
    async def find_by_level(proj_level:int):
        query = select(Task).where(Task.importantLevel == TaskLevel(proj_level))
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
    async def find_by_status(proj_status:int):
        query = select(Task).where(Task.status == TaskLevel(proj_status))
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def order_by_prior():
        query = select(Task).order_by(Task.importantLevel.asc())
        return (await db.execute(query)).all()     
    
    @staticmethod
    async def count_by_prior():
        query = select(Task.importantLevel, func.count(Task.id)).group_by(Task.importantLevel)
        return (await db.execute(query)).all() 

    @staticmethod
    async def order_by_progress():
        query = select(Task).order_by(Task.status.asc())
        return (await db.execute(query)).all()

    @staticmethod
    async def count_by_progress():
        query = select(Task.status, func.count(Task.id)).group_by(Task.status)
        return (await db.execute(query)).all() 
