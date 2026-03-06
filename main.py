from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Todo API"}

@app.get("/todos")
def read_todos():
    return [{"id": 1, "task": "Learn FastAPI"}, {"id": 2, "task": "Build a Todo API"}]

@app.post("/todos")
def create_todo(todo: dict):
    return {"id": 3, "task": todo.get("task", "No task provided")}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: dict):
    return {"id": todo_id, "task": todo.get("task", "No task provided")}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return {"status": "deleted"}