from fastapi import HTTPException
from pydantic import BaseModel, validator

class Project(BaseModel):
    title : str
    description : str

    @validator('title')
    @classmethod
    def title_validation(cls,v):
        if not v:
            raise HTTPException(status_code= 400, detail={'status': "Bad request", 'message': "Invalid title, project title can't be null"} )
        return v 

class inputProject(BaseModel):
    title: str
    description: str




