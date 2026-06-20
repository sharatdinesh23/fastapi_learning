from datetime import datetime
from domain.task import Task

class TaskService:
    def get_tasks(self) ->list[Task]:
        return [
            Task(
                id = 1,
                title = "Task1",
                description= "This task to be done",
                project_id=1,
                assigned_user_id = 1,
                created_at = datetime.utcnow()
            ),
            Task(
                id = 2,
                title = "Task2",
                description= "This task to be done after task1",
                project_id=1,
                assigned_user_id = 1,
                created_at = datetime.utcnow()
            )
        ]   
