from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from .models import TodoInDB
from .schemas import TodoCreate, TodoUpdate, TodoResponse, TodoListResponse
from .database import get_db

# CRUD operations for Todo
class TodoCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_todo(self, todo: TodoCreate) -> TodoInDB:
        db_todo = TodoInDB(**todo.dict())
        self.db.add(db_todo)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def read_todo(self, todo_id: int) -> TodoInDB:
        todo = self.db.query(TodoInDB).filter(TodoInDB.id == todo_id).first()
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def read_todos(self) -> list[TodoInDB]:
        return self.db.query(TodoInDB).all()

    def update_todo(self, todo_id: int, todo: TodoUpdate) -> TodoInDB:
        db_todo = self.read_todo(todo_id)
        for key, value in todo.dict(exclude_unset=True).items():
            setattr(db_todo, key, value)
        self.db.commit()
        self.db.refresh(db_todo)
        return db_todo

    def delete_todo(self, todo_id: int) -> TodoInDB:
        db_todo = self.read_todo(todo_id)
        self.db.delete(db_todo)
        self.db.commit()
        return db_todo

# Dependency
def get_todo_crud(db: Session = Depends(get_db)) -> TodoCRUD:
    return TodoCRUD(db)