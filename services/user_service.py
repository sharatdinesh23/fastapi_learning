from domain.user import User

class UserService:
    
    def get_users(self)->list[User]:
        
        return [
            User(
                id = 1,
                full_name = "Sharath Dinesh",
                email= "sharathdinesh23@gmail.com"
            )
        ]