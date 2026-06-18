from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id:int
    title:str
    description:str
    project_id:int
    created_at:datetime