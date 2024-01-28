import pytest
import requests

#VARIAVEIS PARA TESTE
BASE_URL="http://127.0.0.1:5000/"
tasks = [] #Lista de tarefas criada no teste

def test_create_task():
    new_task_data = {
        "title": "Nova Tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])


#TESTE INDEX
def test_index_task():
    response = requests.get(f"{BASE_URL}tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

#TESTE SHOW
def test_show_task():
    id = tasks[0]
    response = requests.get(f"{BASE_URL}tasks/{id}")
    assert response.status_code == 200
    response_json = response.json()
    assert "title" in response_json
    assert "id" in response_json
    assert id == response_json['id']

#TESTE SHOW
def test_update_task():
    task_data = {
        "title": "Nova Tarefa - UPDATE",
        "description": "Descrição da nova tarefa - UPDATE",
        "completed": True
    }
    id = tasks[0]
    response = requests.put(f"{BASE_URL}tasks/{id}", json=task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

#TESTE SHOW
def test_delete_task():
    
    id = tasks[0]
    response = requests.delete(f"{BASE_URL}tasks/{id}")
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

    id = tasks[0]
    response = requests.get(f"{BASE_URL}tasks/{id}")
    assert response.status_code == 404