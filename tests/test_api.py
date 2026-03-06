import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_create_todo():
    response = client.post("/todos", json={"task": "Test Todo"})
    assert response.status_code == 200
    assert response.json()["task"] == "Test Todo"


def test_create_todo_invalid():
    response = client.post("/todos", json={})
    assert response.status_code == 422


def test_read_todo():
    response = client.post("/todos", json={"task": "Test Todo"})
    todo_id = response.json()["id"]
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id


def test_update_todo():
    response = client.post("/todos", json={"task": "Test Todo"})
    todo_id = response.json()["id"]
    response = client.put(f"/todos/{todo_id}", json={"task": "Updated Todo"})
    assert response.status_code == 200
    assert response.json()["task"] == "Updated Todo"


def test_delete_todo():
    response = client.post("/todos", json={"task": "Test Todo"})
    todo_id = response.json()["id"]
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404