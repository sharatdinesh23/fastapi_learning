import asyncio
from services.project_service import ProjectService
from services.user_service import UserService
from services.task_service import TaskService

class DashboardService:
    def __init__(self) -> None:
        self.user_service = UserService()
        self.task_service = TaskService()
        self.project_service = ProjectService()
    
    async def get_dashboard_data(self):
        users,projects,tasks = await asyncio.gather(
            self.user_service.get_users(),
            self.project_service.get_projects(),
            self.task_service.get_tasks()
        )
        
        return {
            "users":users,
            "projects":projects,
            "tasks":tasks
        }
    
