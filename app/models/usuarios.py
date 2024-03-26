from app import db, ma
import datetime


class Usuarios(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement = True)
  usuario = db.Column(db.String(20), unique = True, nullable = False)
  senha = db.Column(db.String(200), nullable = False)
  nome = db.Column(db.String(60), nullable = False)
  data_criacao = db.Column(db.DateTime, default=datetime.datetime.now())

  def __init__(self, usuario, senha, nome):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome

# Definindo o Schema do Marshmallow para facilitar a utilização de JSON

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuario', 'senha', 'nome', 'data_criacao')


user_schema = UsuariosSchema()
users_schema = UsuariosSchema(many=True)
