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
    task_data = vars(new_task)  # Usando vars() para serializar a tarefa
    return jsonify({"Message": "Nova tarefa criada com sucesso", "task": task_data})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]  # Chamando to_dict() para cada tarefa
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
    return jsonify({"Message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task is None:
        return jsonify({"Message": "Task não foi encontrada!"}), 404

    # Atualizando a tarefa com os novos dados
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)

    return jsonify({"Message": "Atualizado com sucesso", "task": task.to_dict()})  # Usando to_dict()

if __name__ == '__main__':
    app.run(debug=True)
