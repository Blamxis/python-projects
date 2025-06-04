from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API Todo"}

def test_create_todo():
    response = client.post("/todos", json={
        "title": "Test Tâche",
        "description": "Test Description"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Tâche"
    assert data["description"] == "Test Description"
    assert data["completed"] == False
    assert "id" in data

def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
