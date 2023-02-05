from app.schema import project
from http.client import HTTPException
from pydantic import validator
import uuid
from datetime import datetime
from enum import Enum

class Task(project.Project):
    
    importantLevel : Enum
    createDate : datetime
    dueDate : datetime
    projectId : uuid.UUID
    
    @validator('projectId')
    @classmethod
    def uuid_validation(cls,v):
        if not v:
            raise HTTPException("status:%s,data:%s" % (400,"Invalid id, id must not be null" ))
      
        elif type(v) != uuid.UUID:
            raise  HTTPException("status:%s,data:%s" % (400,  "Invalid id, id must be uuid") )
        return v
    



