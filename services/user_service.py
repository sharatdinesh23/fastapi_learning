from domain.user import User
from core.decorators import log_execution
import asyncio

class UserService:
    @log_execution
    async def get_users(self)->list[User]:
        await asyncio.sleep(5)
        return [
            User(
                id = 1,
                full_name = "Sharath Dinesh",
                email= "sharathdinesh23@gmail.com"
            )
        ]