from dataclasses import dataclass
from domain.user import User

@dataclass
class AdminUser(User):
    can_change_users:bool = True