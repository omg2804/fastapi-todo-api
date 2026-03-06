from pydantic import BaseModel
from typing import List, Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class TodoInDB(TodoBase):
    id: int

class TodoResponse(TodoInDB):
    pass

class TodoListResponse(BaseModel):
    todos: List[TodoResponse]