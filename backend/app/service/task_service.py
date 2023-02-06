from app.schema.task import Task
from app.repository.task import TaskRepository
from app.repository.project import ProjectRepository
from fastapi import HTTPException
import uuid

class Task_CRUD_Service:

    @staticmethod
    async def create_service(task: Task):

        #create uuid
        _id = uuid.uuid4()

        #check if project exits
        _project_id = await ProjectRepository.get_by_id(task.projectId)
        if not (_project_id):
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid projectId, project must be exists"} )

        #insert task into table
        _task_dict = task.dict()
        _task_dict['id'] = _id

        await TaskRepository.create(**_task_dict)
    
    @staticmethod
    async def update_service(task_id:uuid.UUID,task: Task):
        
        #check if exists
        _id = await TaskRepository.get_by_id(task_id)
        if not _id:
            raise HTTPException(status_code=400, detail="Task's not exist")

        #check if project exits
        _project_id = await ProjectRepository.get_by_id(task.projectId)
        if not (_project_id):
            raise HTTPException(status_code=400,detail = {'status': "Bad request", 'message': "Invalid projectId, project must be exists"} )
        
        #update into table
        _task_dict = task.dict()
        _task_dict['id'] = task_id
        await TaskRepository.update_by_id(task_id,**_task_dict)

    @staticmethod
    async def delete_service(task_id: uuid.UUID):
        
         #check if exists
        _id = await TaskRepository.get_by_id(task_id)
        if not _id:
            raise HTTPException(status_code=400, detail="task's not exist")
        
        #delete from table
        await TaskRepository.delete_by_id(task_id)

        







