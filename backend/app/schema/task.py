from app.schema import project
from app.model.task import TaskLevel, TaskStatus
from fastapi import HTTPException
from pydantic import validator
from datetime import datetime
from enum import Enum
import uuid


class Task(project.Project):
    
    importantLevel : Enum
    dueDate : datetime
    status : Enum
    projectId : uuid.UUID
    
    @validator('projectId')
    def uuid_validation(cls,v):
        if not v:
            raise HTTPException(status_code=400,detail ={'status': "Bad request", 'message':  "Invalid id, id must not be null"} )
      
        if type(v) != uuid.UUID:
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid id, id must not be uuid"} )
        return v
    
    @validator('importantLevel')
    def TaskLevel_validation(cls,v):
        if not v:
            raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid level, level must not be null"} )
        if type(v) != TaskLevel:
            raise HTTPException(status_code = 400,detail = {'status': "Bad request", 'message': "Invalid level, level must be enum"} )
        return v

    @validator('status')
    def TaskStatus_validation(cls,v):
        if not v:
            raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid status, status must not be null"} )
        if type(v) != TaskStatus:
            raise HTTPException(status_code = 400,detail = {'status': "Bad request", 'message': "Invalid status, status must be enum"} )
        return v
      
    @validator('dueDate')
    def due_date_validator(cls,v):
        if not v:
            raise HTTPException(status_code= 400,detail = {'status': "Bad request", 'message': "Invalid dueDate, dueDate must not be null"} )
        if type(v) is not datetime:
            raise HTTPException(status_code = 400, detail ={'status': "Bad request", 'message':  "Invalid dueDate, dueDate must be date"} )
        if v < datetime.utcnow():
            raise HTTPException(status_code =400,detail = {'status': "Bad request", 'message': "Invalid dueDate, dueDate must not be in the past"} )
        return v




