from app.schema import project
from app.model.task import TaskLevel, TaskStatus
from fastapi.exceptions import HTTPException
from pydantic import validator, BaseModel
from datetime import datetime, timezone
import uuid

class Task(project.Project):
    
    importantLevel : TaskLevel
    dueDate : datetime
    status : TaskStatus
    projectId : uuid.UUID
    
    @validator('projectId')
    def uuid_validation(cls,v):
        if not v:
            raise HTTPException(status_code=400,detail ={'status': "Bad request", 'message':  "Invalid projectId, id must not be null"} )
        if type(v) != uuid.UUID:
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid projectId, id must be uuid"} )
        return v
    
    @validator('importantLevel')
    def task_level_validation(cls,v):
        if not v:
            raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid level, level must not be null"} )
        if type(v) != TaskLevel:
            raise HTTPException(status_code = 400,detail = {'status': "Bad request", 'message': "Invalid level, level must be enum"} )
        return v

    @validator('status')
    def task_status_validation(cls,v):
        if not v:
            raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid status, status must not be null"} )
        if type(v) != TaskStatus:
            raise HTTPException(status_code = 400,detail = {'status': "Bad request", 'message': "Invalid status, status must be enum"} )
        return v
      
    @validator('dueDate')
    def due_date_validator(cls,v):
        if not v:
            raise HTTPException(status_code= 400,detail = {'status': "Bad request", 'message': "Invalid dueDate, dueDate must not be null"} )
        if type(v) != datetime:
            raise HTTPException(status_code = 400,detail = {'status': "Bad request", 'message': "Invalid dueDate, dueDate must be datetime"} )
        
        # dueDate can't be in the past
        if v.astimezone(timezone.utc) < datetime.now(timezone.utc):
            raise HTTPException(status_code =400,detail = {'status': "Bad request", 'message': "Invalid dueDate, dueDate must not be in the past"} )
        return v

class inputTask(BaseModel):
    title: str
    description: str
    importantLevel : int
    dueDate : str
    status : int
    projectId : str
    


