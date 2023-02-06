from fastapi import APIRouter
from app.schema.util import ResponseSchema
from app.schema.task import inputTask 
from app.service.task_service import Task_CRUD_Service as ts


# router for Tasks, more CRUD api
router = APIRouter(prefix='/{project_id}/task', tags=['Task API'])

# Raise exeption for invalid enum
@router.get("/",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_get_all(project_id : str, level : int = 0, status: int = 0):
    result = await ts.get_by_project(project_id= project_id, level= level, status = status)
    return ResponseSchema(detail="This is a task list page", result= result)

@router.get("/{task_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_get_one(project_id : str,task_id: str):
    result = await ts.get_by_id(project_id= project_id, task_id=task_id)
    return ResponseSchema(detail="This is a task description popup", result=result)

@router.post("/create",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_create(req: inputTask):
    await ts.create_service(req)
    return ResponseSchema(detail="task has been created")

@router.put("/update/{task_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_update(task_id : str,req: inputTask):
    await ts.update_service(task_id=task_id, task=req)
    return ResponseSchema(detail="task has been updated")

@router.delete("/delete/{task_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def task_delete(task_id : str):
    await ts.delete_service(task_id=task_id)
    return ResponseSchema(detail="task has been deleted")

