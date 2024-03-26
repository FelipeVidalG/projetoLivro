from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.livros import Livros, livro_schema, livros_schema
from http import HTTPStatus

# Rotas para cadastrar um novo livro, buscar pelo nome e deletar através do id.

def cadastrar_livro(current_user):
  nome = request.json['nome']
  data_lancamento = request.json['data_lancamento']
  isbn = request.json['isbn']
  autor = request.json['autor']

  livro = Livros(nome, data_lancamento, isbn, autor)

  try:
      db.session.add(livro)
      db.session.commit()
      result = livro_schema.dump(livro)
      return jsonify({'mensagem': 'Livro registrado com sucesso', 'data': result}), HTTPStatus.CREATED
  except Exception as e:
      return jsonify({'mensagem': 'Não foi possível registrar o livro', 'data': {}}), HTTPStatus.INTERNAL_SERVER_ERROR

def buscar_livro(current_user, nome_livro):
  try:
    livro = Livros.query.filter_by(nome=nome_livro).all()
    if livro:
      result = livros_schema.dump(livro)
      return jsonify({'message': 'Livro encontrado!', 'data': result}), HTTPStatus.CREATED
    
    return jsonify({'message': "Livro não encontrado", 'data': {}}), HTTPStatus.NOT_FOUND
  
  except Exception as e:
      return jsonify({"Ocorreu um erro: ": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

def deletar_livro(current_user, livro_id):
  livro = Livros.query.get(livro_id)
  if not livro:
      return jsonify({'message': "Livro com este id não existe.", 'data': {}}), HTTPStatus.NOT_FOUND

  if livro:
      try:
          db.session.delete(livro)
          db.session.commit()
          result = livro_schema.dump(livro)
          return jsonify({'message': 'Livro apagado com sucesso.', 'data': result}), HTTPStatus.OK
      except:
          return jsonify({'message': 'Não foi possível apagar o livro', 'data': {}}), HTTPStatus.INTERNAL_SERVER_ERROR