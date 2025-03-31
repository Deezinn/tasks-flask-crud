from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD -> CREATE, READ, UPDATE, DELETE

tasks = []
task_id_control = 0

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
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify({"Message": "Todas as tarefas retornadas", "Tasks": output})

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify({"Message": "Tarefa retornada", "Task": t.to_dict()})
    return jsonify({"Message": "Não foi possível encontrar a atividade"}), 404  # Agora está fora do for

if __name__ == '__main__':
    app.run(debug=True)
