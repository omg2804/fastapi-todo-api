import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI Todo API"}

def test_create_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description"})
    todo_id = response.json()["id"]
    
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id

def test_update_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description"})
    todo_id = response.json()["id"]
    
    response = client.put(f"/todos/{todo_id}", json={"title": "Updated Todo", "description": "Updated Description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Todo"

def test_delete_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description"})
    todo_id = response.json()["id"]
    
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204

    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404