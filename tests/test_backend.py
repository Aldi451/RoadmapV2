import pytest
from fastapi.testclient import TestClient
import os
import sys

# Add roadmap root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.main import app

client = TestClient(app)

def test_get_roadmap():
    response = client.get("/api/roadmap")
    assert response.status_code == 200
    data = response.json()
    assert "project_name" in data
    assert "phases" in data
    assert len(data["phases"]) > 0

def test_update_task():
    # Update a task
    update_data = {
        "task_code": "1.1",
        "status": "Completed",
        "note": "Updated via TDD test",
        "is_active": True
    }
    response = client.post("/api/roadmap/update-task", json=update_data)
    assert response.status_code == 200
    
    # Retrieve roadmap and verify it was updated
    response = client.get("/api/roadmap")
    data = response.json()
    task_found = False
    for phase in data["phases"]:
        for task in phase["tasks"]:
            if task["code"] == "1.1":
                assert task["status"] == "Completed"
                assert "Updated via TDD test" in task["note"]
                task_found = True
                break
    assert task_found

def test_get_holidays():
    response = client.get("/api/holidays")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task_name():
    # Update task name
    update_data = {
        "task_code": "1.PRP",
        "name": "Project Preparation - Updated Name"
    }
    response = client.post("/api/roadmap/update-task", json=update_data)
    assert response.status_code == 200
    
    # Retrieve roadmap and verify the name was updated
    response = client.get("/api/roadmap")
    data = response.json()
    task_found = False
    for phase in data["phases"]:
        for task in phase["tasks"]:
            if task["code"] == "1.PRP":
                assert task["name"] == "Project Preparation - Updated Name"
                task_found = True
                break
    assert task_found

def test_update_task_progress():
    # Update progress
    update_data = {
        "task_code": "1.PRP",
        "progress": 85
    }
    response = client.post("/api/roadmap/update-task", json=update_data)
    assert response.status_code == 200
    
    # Retrieve roadmap and verify the progress was updated
    response = client.get("/api/roadmap")
    data = response.json()
    task_found = False
    for phase in data["phases"]:
        for task in phase["tasks"]:
            if task["code"] == "1.PRP":
                assert task["progress"] == 85
                task_found = True
                break
    assert task_found


