from flask_sqlalchemy import SQLAlchemy

#cria instancia do SQLAlchemy
db = SQLAlchemy()
#Apos definir todos os atributos na model é importante entrar no flask shell e usar o comando db.create_all() e depois db.session.commit()