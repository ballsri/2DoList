from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.schema.util import ResponseSchema
from app.schema.task import inputTask ,Task 
from app.model.task import TaskLevel, TaskStatus
from app.repository.task import TaskRepository
from app.service.task_service import Task_CRUD_Service as ts
from datetime import datetime
import uuid
date_format='%Y/%m/%d %H:%M:%S'

# router for Tasks, more CRUD api
router = APIRouter(prefix='/{project_id}/task', tags=['Task API'])

# Raise exeption for invalid enum
def enumChecker(req : inputTask):
    _implevel = int(req.importantLevel)
    _status = int(req.status)
    if  _implevel < 1 or _implevel > 3 :
        raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid importantLevel, importantLevel must be enum"} )
    if  _status < 1 or _status > 3:
        raise HTTPException(status_code= 400,detail ={'status': "Bad request", 'message': "Invalid status, status must be enum"} )



@router.get("/",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_get_all(project_id : str, level : int = 0, status: int = 0):

    return ResponseSchema(detail="This is a task list page", result= (await TaskRepository.find_by_project_id(uuid.UUID(project_id), level, status)))

@router.get("/{task_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_get_one(project_id : str,task_id: str):
    return ResponseSchema(detail="This is a task description popup", result= (await TaskRepository.find_by_project_task(uuid.UUID(project_id),uuid.UUID(task_id))))

@router.post("/create",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_create(req: inputTask):
    # enum validation
    enumChecker(req)
    # then run function from service
    await ts.create_service(Task(title=req.title, description=req.description,importantLevel= TaskLevel(int(req.importantLevel)),
     dueDate= datetime.strptime(req.dueDate,date_format), status= TaskStatus(int(req.status)), projectId= uuid.UUID(req.projectId)))
    return ResponseSchema(detail="task has been created")

@router.put("/update/{task_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_update(task_id : str,req: inputTask):
    enumChecker(req)
    await ts.update_service(uuid.UUID(task_id),Task(title=req.title, description=req.description,importantLevel= TaskLevel(int(req.importantLevel)),
     dueDate= datetime.strptime(req.dueDate,date_format), status= TaskStatus(int(req.status)), projectId= uuid.UUID(req.projectId)))
    return ResponseSchema(detail="task has been updated")

@router.delete("/delete/{task_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_delete(task_id : str):
    await ts.delete_service(uuid.UUID(task_id))
    return ResponseSchema(detail="task has been delete")

