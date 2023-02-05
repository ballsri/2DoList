from app.config.db_config import db , Base
from sqlalchemy import Column,ForeignKey,Text ,  String,Enum, DateTime, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum


class ILevel(enum.Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(UUID, primary_key=True, server_default=func.gen_random_uuid(), index=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    importantLevel = Column(Enum(ILevel), nullable=False)
    createDate = Column(DateTime, server_default=func.current_timestamp())
    dueDate = Column(DateTime, nullable=False)
    projectId = Column(UUID, ForeignKey("projects.id"), nullable=False) 
    from_project = relationship('Project', back_populates="tasks")