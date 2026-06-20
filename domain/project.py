from dataclasses import dataclass
from datetime import datetime
from domain.task import Task

@dataclass
class Project:
    id:int
    name:str
    description:str
    owner_id:int
    tasks:list[Task]
    created_at:datetime
    

