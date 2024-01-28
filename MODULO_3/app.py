from flask import Flask, request, jsonify
from models.task import Task

#inicia o projeto flask
app = Flask(__name__)

tasks = []
task_id_control = 1

#Cria a task
@app.route("/tasks", methods=['POST'])
def create_task():
    global task_id_control #O global permite acessar a var global dentro da func
    data = request.get_json()

    #no get ele tenta recuperar, se n existir assume o valor da segunda aspas
    task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control+=1
    tasks.append(task)
    return jsonify({"message": "Nova tarefa criada com sucesso", "id": task.id})

@app.route("/tasks", methods=['GET'])
def listar_todas_as_tasks():
    # tasks_list = []
    # for task in tasks:
    #     tasks_list.append(task.to_dict())
    tasks_list = [ task.to_dict() for task in tasks ]
    
    output = {
        "tasks": tasks_list,
        "total_tasks": len(tasks)
    }

    return jsonify(output)

@app.route("/tasks/<int:id>", methods=['GET']) #para recuperar o parametro e colocado entre <>
def exibir_task_especifica(id):

    for t in tasks:
        if(t.id == id):
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi encontrado task com esse id"}), 404

@app.route("/tasks/<int:id>", methods=['PUT']) #para recuperar o parametro e colocado entre <>
def atualizar_tarefa(id):

    task = None
    for t in tasks:
        if(t.id == id):
            task = t
            break

    if(task == None):
        return jsonify({"message": "Não foi encontrado task com esse id"}), 404
    data = request.get_json()

    task.title = data.get("title")
    task.description = data.get("description", "")
    task.completed = bool(data.get("completed"))

    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route("/tasks/<int:id>", methods=['DELETE']) #para recuperar o parametro e colocado entre <>
def deletar_tarefa(id):

    task = None
    for t in tasks:
        if(t.id == id):
            task = t
            break
    
    if(task == None):
        return jsonify({"message": "Não foi encontrado task com esse id"}), 404

    #remove
    tasks.remove(task)
    return jsonify({"message": "Tarefa removida com sucesso"})

#define o servidor
if __name__ == "__main__": #Por padrao é main, no dev local é main, por isso start debug
    app.run(debug=True)