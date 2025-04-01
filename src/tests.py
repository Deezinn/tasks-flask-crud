import pytest
import requests

base_url = 'http://127.0.0.1:5000'

tasks = []

def teste_create_task():

    new_task_data = {
        "title": "nova tarefa",
        "description": "descrição da nova tarefa"
        }
    response = requests.post(f'{base_url}/tasks', json=new_task_data)
    assert response.status_code == 200

