from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.usuarios import Usuarios, user_schema, users_schema
from http import HTTPStatus

# Rotas para cadastrar um novo usuário e procurar usuário para realizar verificações.

def cadastrar_usuario():
    usuario = request.json['usuario']
    senha = request.json['senha']
    nome = request.json['nome']

    user = procura_usuario(usuario)
    if user:
        result = user_schema.dump(user)
        return jsonify({'mensagem': 'Nome de usuário já existe.', 'data': {}})

    senha_hash = generate_password_hash(senha)
    user = Usuarios(usuario=usuario, senha=senha_hash, nome=nome)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'mensagem': 'Registrado com sucesso', 'data': result}), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({'mensagem': 'Não foi possível registrar', 'data': {}}), HTTPStatus.INTERNAL_SERVER_ERROR

def procura_usuario(usuario):
    try:
        return Usuarios.query.filter(Usuarios.usuario == usuario).one()
    except:
        return None