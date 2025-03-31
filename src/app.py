from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD -> CREATE, READ, UPDATE, DELETE

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    task_data = vars(new_task)

    return jsonify({"Message": "Nova tarefa criada com sucesso", "task": task_data})



@app.route('/tasks', methods=['GET'])
def return_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    return jsonify({"Message": "Todas as tarefas retornadas",
                    "Tasks": task_list})

if __name__ == '__main__':
    app.run(debug=True)
