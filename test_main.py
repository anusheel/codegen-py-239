from fastapi.testclient import TestClient
from main import app, User

client = TestClient(app)

def test_create_user():
    response = client.post("/user/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json() == {"name": "John Doe", "email": "john@example.com"}

def test_read_user():
    response = client.get("/user/0")
    assert response.status_code == 200
    assert response.json() == {"name": "John Doe", "email": "john@example.com"}

def test_update_user():
    response = client.put("/user/0", json={"name": "Jane Doe", "email": "jane@example.com"})
    assert response.status_code == 200
    assert response.json() == {"name": "Jane Doe", "email": "jane@example.com"}

def test_delete_user():
    response = client.delete("/user/0")
    assert response.status_code == 200
    assert response.json() == {"name": "Jane Doe", "email": "jane@example.com"}