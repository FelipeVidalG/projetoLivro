import datetime
from functools import wraps
from app import app
from flask import request, jsonify
from .usuarios import procura_usuario
import jwt
from werkzeug.security import check_password_hash
from http import HTTPStatus


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Não foi possível verificar', 'WWW-Authenticate': 'Basic auth="Login required"'}), HTTPStatus.UNAUTHORIZED
    user = procura_usuario(auth.username)
    if not user:
        return jsonify({'message': 'Usuário não encontrado', 'data': []}), HTTPStatus.UNAUTHORIZED

    if user and check_password_hash(user.senha, auth.password):
        token = jwt.encode({'username': user.usuario, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                           app.config['SECRET_KEY'])
        return jsonify({'message': 'Autenticado com sucesso', 'token': token,
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'Não foi possível verificar', 'WWW-Authenticate': 'Basic auth="Login required"'}), HTTPStatus.UNAUTHORIZED


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
      token = request.args.get('token')
      if not token:
        return jsonify({'message': 'Token expirado ou inválido', 'data': []}), HTTPStatus.UNAUTHORIZED
      try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        current_user = procura_usuario(usuario=data['username'])
      except Exception as e:
        return jsonify({'message': 'Token expirado ou inválido.', 'data': []}), HTTPStatus.UNAUTHORIZED
      return f(current_user, *args, **kwargs)
    return decorated