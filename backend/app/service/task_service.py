from fastapi import HTTPException
from app.service.util import date_format, date_format_checker, uuid_checker, enum_checker
from app.schema.task import Task, inputTask
from app.model.task import TaskLevel, TaskStatus
from app.repository.task import TaskRepository
from app.repository.project import ProjectRepository
from datetime import datetime
import uuid

class Task_CRUD_Service:


    @staticmethod
    async def create_service(task: inputTask):

        #create uuid
        _id = uuid.uuid4()

        ##INPUT VALIDATION##

        # enum validation
        enum_checker(int(task.importantLevel), int(task.status), isQuery = False)
        # date validation
        date_format_checker(task.dueDate)
        # uuid checker
        uuid_checker(task.projectId)


        # create Task schema
        _task = Task(title=task.title, description=task.description,importantLevel= TaskLevel(int(task.importantLevel)),
     dueDate= datetime.strptime(task.dueDate,date_format), status= TaskStatus(int(task.status)), projectId= uuid.UUID(task.projectId))

        # check if project exits
        _project_id = await ProjectRepository.get_by_id(task.projectId)
        if not (_project_id):
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid projectId, project must be exists"} )

        # insert task into table
        _task_dict = _task.dict()
        _task_dict['id'] = _id

        await TaskRepository.create(**_task_dict)
    
    @staticmethod
    async def update_service(task_id: str,task: inputTask):

        
        ## INPUT VALIDATATION ##

        # enum validation
        enum_checker(int(task.importantLevel), int(task.status), isQuery = False)
        # date validation
        date_format_checker(task.dueDate)
        # uuid checker
        uuid_checker(task_id)
        uuid_checker(task.projectId)

        # create task id
        _task_id = uuid.UUID(task_id)

        # create Task schema
        _task = Task(title=task.title, description=task.description,importantLevel= TaskLevel(int(task.importantLevel)),
     dueDate= datetime.strptime(task.dueDate,date_format), status= TaskStatus(int(task.status)), projectId= uuid.UUID(task.projectId))


        # check if task exists
        _id = await TaskRepository.get_by_id(_task_id)
        if not _id:
            raise HTTPException(status_code=400, detail={'status': "Bad request", 'message': "Invalid taskId, task's not exist"})

        # check if project exits
        _project_id = await ProjectRepository.get_by_id(_task.projectId)
        if not (_project_id):
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid projectId, project's not exists"} )
        
        # update into table
        _task_dict = _task.dict()
        _task_dict['id'] = _task_id
        await TaskRepository.update_by_id(_task_id,**_task_dict)

    @staticmethod
    async def delete_service(task_id: str):

        ## INPUT VALIDATATION ##
        # uuid checker
        uuid_checker(task_id)

        # create task id
        _task_id = uuid.UUID(task_id)

        # check if exists
        _id = await TaskRepository.get_by_id(_task_id)
        if not _id:
            raise HTTPException(status_code=400, detail={'status': "Bad request", 'message': "Task's not exist"})
        
        # delete from table
        await TaskRepository.delete_by_id(_task_id)

    @staticmethod
    async def get_by_project(project_id: str, level : int, status : int ):

        ## INPUT VALIDATATION ##
        # enum validation
        enum_checker(importantLevel=level, status= status, isQuery = True)
        # uuid validation
        uuid_checker(project_id)

        # create project id
        _project_id = uuid.UUID(project_id)

        # get from db
        result = await TaskRepository.find_by_project_id(_project_id, level, status)
        return result

    @staticmethod
    async def get_by_id(project_id: str, task_id: str):
        
        ## INPUT VALIDATATION ##
        uuid_checker(project_id)
        uuid_checker(task_id)

        # create ids
        _project_id = uuid.UUID(project_id)
        _task_id = uuid.UUID(task_id)

        # get from db
        result = await TaskRepository.find_by_project_task(_project_id, _task_id)
        return result
        



        







