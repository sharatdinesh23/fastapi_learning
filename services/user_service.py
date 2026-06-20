from domain.user import User
from core.decorators import log_execution

class UserService:
    @log_execution
    def get_users(self)->list[User]:
        
        return [
            User(
                id = 1,
                full_name = "Sharath Dinesh",
                email= "sharathdinesh23@gmail.com"
            )
        ]