from fastapi import HTTPException
from app.repository.project import ProjectRepository
from app.service.util import uuid_checker
from app.schema.project import Project, inputProject
import uuid

class Project_CRUD_Service:

    @staticmethod
    async def create_service(project: inputProject):

        #create uuid
        _id = uuid.uuid4()

        # check if title exist
        _project_check = await ProjectRepository.get_by_title(project.title)
        if _project_check:
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid title, project title has already exists"} )

        # create project schema
        _project = Project(title=project.title, description=project.description)


        # insert project into table
        _project_dict = _project.dict()
        _project_dict['id'] = _id

        await ProjectRepository.create(**_project_dict)
    
     
    @staticmethod
    async def update_service(project_id: str,project: inputProject):

        
        ## INPUT VALIDATATION ##
        # uuid checker
        uuid_checker(project_id)

        # create project id
        _project_id = uuid.UUID(project_id)

        # check if title exist
        _project_check = await ProjectRepository.get_by_title(project.title)
        if _project_check:
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid title, project title has already exists"} )


        # create project schema
        _project = Project(title=project.title, description=project.description)


        # check if project exists
        _id = await ProjectRepository.get_by_id(_project_id)
        if not _id:
            raise HTTPException(status_code=400, detail={'status': "Bad request", 'message': "Invalid projectId, project's not exist"})

        
        # update into table
        _project_dict = _project.dict()
        _project_dict['id'] = _project_id
        await ProjectRepository.update_by_id(_project_id,**_project_dict)


    @staticmethod
    async def delete_service(project_id : str):

        ## INPUT VALIDATATION ##
        # uuid checker
        uuid_checker(project_id)

        # create project id
        _project_id = uuid.UUID(project_id)

        # check if exists
        _id = await ProjectRepository.get_by_id(_project_id)
        if not _id:
            raise HTTPException(status_code=400, detail={'status': "Bad request", 'message': "project's not exist"})
        
        # delete from table
        await ProjectRepository.delete_by_id(_project_id)

    @staticmethod
    async def get_by_id_service(project_id : str):

        ## INPUT VALIDATATION ##
        # uuid checker
        uuid_checker(project_id)
       
        # create ids
        _project_id = uuid.UUID(project_id)
     
        # get from db
        result = await ProjectRepository.get_by_id(_project_id)
        return result



        







