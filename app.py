from flask import Flask, request
from models.task import Task

app = Flask(__name__)

#CRUD -> CREATE, READ, UPDATE, DELETE

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    print(data)
    return 'teste'

if __name__ == '__main__':
    app.run(debug=True)
