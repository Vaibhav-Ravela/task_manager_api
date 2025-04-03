def test_create_task(client):
    token = client.post("/auth/login", data={"username": "test@example.com", "password": "test123"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Task details"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_tasks(client):
    token = client.post("/auth/login", data={"username": "test@example.com", "password": "test123"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.get("/tasks/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
