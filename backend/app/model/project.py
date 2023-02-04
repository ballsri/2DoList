from pydantic import BaseModel, Field
from db_config import db, Base
from sqlalchemy import Table, Column,Boolean,ForeignKey, Integer, String,Text, Enum, DateTime
from sqlalchemy.orm import relationship



class Project(Base):
    __tablename__ = 'projects'
    id = Column(String(36), primary_key=True)
    title = Column(String(50),nullable=False)
    description = Column(Text, nullable=True)
    tasks = relationship('Task', back_populates="from_project")
