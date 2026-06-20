from fastapi import APIRouter
from services.task_service import TaskService

task_router = APIRouter(prefix="/tasks",tags=["tasks"])

task_service = TaskService()

@task_router.get("/get_tasks")
def get_tasks():
    return task_service.get_tasks()
