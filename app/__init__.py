from flask import Flask, jsonify, request, jsonify, make_response, session
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)


from .models import usuarios, livros
from .routes import routes


# Cria as tabelas se ainda não existir
with app.app_context():
    db.create_all()
