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

def test_add_phase():
    phase_data = {
        "name": "Phase Baru TDD",
        "code": "3"
    }
    response = client.post("/api/roadmap/phase", json=phase_data)
    assert response.status_code == 200
    
    # Verify phase was added
    response = client.get("/api/roadmap")
    data = response.json()
    phase_found = False
    for p in data["phases"]:
        if p["code"] == "3":
            assert p["name"] == "Phase Baru TDD"
            phase_found = True
            break
    assert phase_found

def test_update_phase():
    # Update phase name
    update_data = {
        "name": "Phase Baru TDD Updated"
    }
    response = client.post("/api/roadmap/phase/3", json=update_data)
    assert response.status_code == 200
    
    # Verify phase was updated
    response = client.get("/api/roadmap")
    data = response.json()
    phase_found = False
    for p in data["phases"]:
        if p["code"] == "3":
            assert p["name"] == "Phase Baru TDD Updated"
            phase_found = True
            break
    assert phase_found

def test_add_task():
    task_data = {
        "phase_code": "3",
        "code": "3.TSK",
        "name": "Task TDD Baru"
    }
    response = client.post("/api/roadmap/task", json=task_data)
    assert response.status_code == 200
    
    # Verify task was added under Phase 3
    response = client.get("/api/roadmap")
    data = response.json()
    task_found = False
    for p in data["phases"]:
        if p["code"] == "3":
            for t in p["tasks"]:
                if t["code"] == "3.TSK":
                    assert t["name"] == "Task TDD Baru"
                    task_found = True
                    break
    assert task_found

def test_delete_task():
    response = client.delete("/api/roadmap/task/3.TSK")
    assert response.status_code == 200
    
    # Verify task is deleted
    response = client.get("/api/roadmap")
    data = response.json()
    task_found = False
    for p in data["phases"]:
        if p["code"] == "3":
            for t in p["tasks"]:
                if t["code"] == "3.TSK":
                    task_found = True
    assert not task_found

def test_delete_phase():
    response = client.delete("/api/roadmap/phase/3")
    assert response.status_code == 200
    
    # Verify phase is deleted
    response = client.get("/api/roadmap")
    data = response.json()
    phase_found = False
    for p in data["phases"]:
        if p["code"] == "3":
            phase_found = True
            break
    assert not phase_found



