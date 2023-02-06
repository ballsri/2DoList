from app.config.db_config import Base
from sqlalchemy import Column,String,Text, UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = 'projects'
    id = Column(UUID, primary_key=True, server_default=func.gen_random_uuid(), index=True)
    title = Column(String(50),nullable=False, unique=True)
    description = Column(Text, nullable=True)
    tasks = relationship('Task', back_populates="from_project")



 