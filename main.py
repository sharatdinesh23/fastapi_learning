from fastapi import FastAPI
from services.project_service import ProjectService
from services.task_service import TaskService

app = FastAPI(
    title = "SaaS Project Management Platform",
    version  = "1.0.0"
)

project_service = ProjectService()
task_service = TaskService()

@app.get("/projects")
def get_projects():
    projects = project_service.get_projects()
    
    return projects

@app.get("/tasks")
def get_tasks():
    tasks = task_service.get_tasks()
    
    return tasks