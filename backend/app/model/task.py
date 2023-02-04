from pydantic import BaseModel, Field
from ..db_config import db, Base
from sqlalchemy import Table, Column,Boolean,ForeignKey, Integer,Text ,  String,Enum, DateTime
from sqlalchemy.orm import relationship
import enum
from datetime import datetime



class ILevel(enum.Enum):
    HIGH = 3
    MEDIUM = 2
    LOW = 1


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(String(8), primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    ImportantLevel = Column(Enum(ILevel), nullable=False)
    createDate = Column(DateTime, default=datetime.utcnow)
    dueDate = Column(DateTime, nullable=False)
    projectId = Column(String(8), ForeignKey("projects.id"), nullable=False) 
    from_project = relationship('Project', back_populates="tasks")