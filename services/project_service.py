from datetime import datetime
from domain.project import Project

class ProjectService:
    def get_projects(self) -> list[Project]:
        return [
            Project(
                id=1,
                name="Website Redesign",
                description= "changing the website",
                owner_id = 1,
                created_at = datetime.utcnow()
            ),
            Project(
                id = 2,
                name = "Mobile Application",
                description = "Build custom mobile app",
                owner_id = 1,
                created_at = datetime.utcnow()
            )
        ]