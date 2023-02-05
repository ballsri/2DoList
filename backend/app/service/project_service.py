from app.schema.project import Project
from app.repository.project import ProjectRepository
from fastapi import HTTPException
import uuid

class Project_CRUD_Service:

    @staticmethod
    async def create_service(project: Project):

        #create uuid
        _id = uuid.uuid4()

        #check duplication
        _title = await ProjectRepository.get_by_title(project.title)
        if _title:
            raise HTTPException(status_code=400, detail="Project's name already exists")

        #insert project into table
        _project_dict = project.dict()
        _project_dict['id'] = _id

        await ProjectRepository.create(**_project_dict)
    
    @staticmethod
    async def update_service(project_id:uuid.UUID,project: Project):
        
        #check if exists
        _id = await ProjectRepository.get_by_id(project_id)
        if not _id:
            raise HTTPException(status_code=400, detail="Project's not exist")
        
        #update into table
        _project_dict = project.dict()
        _project_dict['id'] = project_id
        await ProjectRepository.update_by_id(project_id,**_project_dict)

    @staticmethod
    async def delete_service(project_id: uuid.UUID):
         #check if exists
        _id = await ProjectRepository.get_by_id(project_id)
        if not _id:
            raise HTTPException(status_code=400, detail="Project's not exist")
        
        #delete from table
        await ProjectRepository.delete_by_id(project_id)

        







