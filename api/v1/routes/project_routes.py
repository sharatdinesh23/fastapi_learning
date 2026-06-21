from fastapi import APIRouter
from services.project_service import ProjectService

project_router = APIRouter(prefix="/projects",tags=["projects"])

project_service = ProjectService()

@project_router.get("/read_projects")
async def get_projects():
    return await project_service.get_projects()


