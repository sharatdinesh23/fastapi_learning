from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id:int
    full_name:str
    email:str
    is_active:bool
    created_at:datetime = datetime.now()
