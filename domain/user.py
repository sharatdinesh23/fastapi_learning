from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id:int
    full_name:str
    email:str
    _is_active:bool = True
    created_at:datetime = datetime.now()
    
    def deactivate(self)->None:
        self._is_active = False
    
    def activate(self)->None:
        self._is_active = True
    
    @property
    def is_active(self)->bool:
        return self._is_active

        