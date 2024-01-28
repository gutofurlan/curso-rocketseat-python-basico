from database import db #Recupera a instancia do sql
from flask_login import UserMixin #Classe do flask login para autenticar

class User(db.Model, UserMixin): #Herda da class db model
    #define as colunas
    id = db.Column(db.Integer, primary_key=True) #Define como chave primaria
    username = db.Column(db.String(80), nullable=False, unique=True) #coluna varchar 80 q n aceita null, e seja unico
    password = db.Column(db.String(80), nullable=False, unique=False)
    role = db.Column(db.String(80), nullable=False, unique=False, default="user")