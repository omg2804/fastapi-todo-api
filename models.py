from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    completed: Optional[bool] = None

class TodoInDB(TodoBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True