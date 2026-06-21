from datetime import datetime
from domain.project import Project
from core.decorators import log_execution
import asyncio

class ProjectService:
    @log_execution
    async def get_projects(self) -> list[Project]:
        await asyncio.sleep(2)
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