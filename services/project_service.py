from datetime import datetime
from domain.project import Project
from core.decorators import log_execution

class ProjectService:
    @log_execution
    def get_projects(self) -> list[Project]:
        return [
            Project(
                id=1,
                name="Website Redesign",
                description= "changing the website",
                owner_id = 1,
                tasks = [],
                created_at = datetime.utcnow()
            ),
            Project(
                id = 2,
                name = "Mobile Application",
                description = "Build custom mobile app",
                owner_id = 1,
                tasks = [],
                created_at = datetime.utcnow()
            )
        ]