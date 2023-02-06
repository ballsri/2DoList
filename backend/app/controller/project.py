from fastapi import APIRouter
from app.schema.util import ResponseSchema
from app.schema.project import inputProject
from app.repository.project import ProjectRepository
from app.service.project_service import Project_CRUD_Service as ps


#router for Projects, they're all CRUD api
router = APIRouter(prefix='', tags=['Project API'])


@router.get("/",response_model=ResponseSchema, response_model_exclude_none=True)
async def project_get_all():
    result = await ProjectRepository.get_all()
    return ResponseSchema(detail="This is a project list page", result= result)

@router.get("/get/{project_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def project_get_one(project_id: str):
    result = await ps.get_by_id_service(project_id)
    return ResponseSchema(detail="This is a project description popup", result= result )

@router.post("/create",response_model=ResponseSchema, response_model_exclude_none=True)
async def project_create(req: inputProject):
    await ps.create_service(req)
    return ResponseSchema(detail="Project has been created")

@router.put("/update/{project_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def project_update(project_id : str,req: inputProject):
    await ps.update_service(project_id,req)
    return ResponseSchema(detail="Project has been updated")

@router.delete("/delete/{project_id}",response_model=ResponseSchema, response_model_exclude_none=True)
async def project_delete(project_id : str):
    await ps.delete_service(project_id)
    return ResponseSchema(detail="Project has been deleted")
    

