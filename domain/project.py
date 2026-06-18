from dataclasses import dataclass
from datetime import datetime

@dataclass
class Project:
    id:int
    name:str
    description:str
    owner_id:int
    created_at:datetime
    

