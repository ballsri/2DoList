from pydantic import BaseModel, Field
from db_config import db, Base
from sqlalchemy import Table, Column,Boolean,ForeignKey, Integer,Text ,  String,Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from datetime import datetime

class ILevel(enum.Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String(36), primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    importantLevel = Column(Enum(ILevel), nullable=False)
    createDate = Column(DateTime, server_default=func.current_timestamp())
    dueDate = Column(DateTime, nullable=False)
    projectId = Column(String(36), ForeignKey("projects.id"), nullable=False) 
    from_project = relationship('Project', back_populates="tasks")