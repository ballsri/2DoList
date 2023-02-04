
from app.config import db_config 
from sqlalchemy import Column,String,Text
from sqlalchemy.orm import relationship


db , Base = db_config.db, db_config.Base

class Project(Base):
    __tablename__ = 'projects'
    id = Column(String(36), primary_key=True)
    title = Column(String(50),nullable=False)
    description = Column(Text, nullable=True)
    tasks = relationship('Task', back_populates="from_project")
