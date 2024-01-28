from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import bcrypt
from database import db

from models.user import User

#inicia o projeto flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key" #DEFINE UMA KEY PARA OAUTH
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" #DEFINE ONDE IRA CONECTAR NO DB

#configuracao do login manager
login_manager = LoginManager()

#intancia o db apenas para o app
db.init_app(app=app)

#start login manager
login_manager.init_app(app)

#Define a rota de lin no login manager
login_manager.login_view = 'login'

#Metodo obrigatorio o qual ira recuperar o user logado e carrega
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Rota LogOut
@app.route("/logout", methods=["GET"])
@login_required #Valida q so acesse quem esta autenticado
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})

#Rota de login
@app.route("/login", methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        #Busca no DB
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.checkpw( str.encode(password), user.password):
            #Autentica
            login_user(user)

            #Recupera se esta autenticado
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticacao realizada com sucesso"})
            
    
    return jsonify({"message": "Credenciais invalidas"}), 400

#Rota de cadastro
@app.route("/user", methods=["POST"])
def store_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if(username and password):
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username=username, password=hashed_password, role="user")
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario cadastrado com sucesso"})
    
    return jsonify({"message": "Parametros invalidos"}), 400

#Rota de listagem de user
@app.route("/user", methods=["GET"])
@login_required
def listar_todos_os_usuarios():
    list_user = []
    all_users = User.query.all()
    for user in all_users:
        list_user.append({"username": user.username, "id": user.id})
    
    output = {
        "users": list_user,
        "quantidade_de_usuarios": len(list_user)
    }
    return jsonify(output)

#Rota de listagem de user especifico
@app.route("/user/<int:id>", methods=["GET"])
@login_required
def listar_usuario_especifico(id):
    user = User.query.get(id)
    if user:
        return jsonify({"username": user.username, "id": user.id})
    return jsonify({"message": "Usuario nao localizado"}), 404

#Rota de update de user especifico
@app.route("/user/<int:id>", methods=["PUT"])
@login_required
def update_user(id):
    user = User.query.get(id)
    data = request.json
    password = data.get("password")
    
    if id != current_user.id and current_user.role == 'user': #user nirmal nao pode editar de outros users
        return jsonify({"message": "Operacao exclusica para admins"}), 403

    if not (password):
        return jsonify({"Dados invalidos"}), 400

    if user and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user.password = hashed_password
        db.session.commit() #Salva no db
        return jsonify({"message": f"Usuario {id} atualizado com sucesso"})
    
    return jsonify({"message": "Usuario nao localizado"}), 404

#Rota de delete de user especifico
@app.route("/user/<int:id>", methods=["DELETE"])
@login_required
def delete_user(id):
    user = User.query.get(id)

    if current_user.role == 'user': #user nirmal nao pode editar de outros users
        return jsonify({"message": "Operacao exclusiva para admins"}), 403

    if user and user.id == current_user.id:
        return jsonify({"message": "Deleção não permitida"}), 401
    
    if user:
        db.session.delete(user)
        db.session.commit() #Salva no db
        return jsonify({"message": f"Usuario {id} deletado com sucesso"})
    
    return jsonify({"message": "Usuario nao localizado"}), 404


#define o servidor
if __name__ == "__main__": #Por padrao é main, no dev local é main, por isso start debug
    app.run(debug=True)