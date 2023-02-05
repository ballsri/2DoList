from app.model.task import Task
from app.repository.base import Base


class TaskRepository(Base):
    model = Task 
