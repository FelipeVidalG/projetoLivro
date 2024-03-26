from app import app
from flask import Flask, jsonify, request, make_response, session, url_for, redirect
from http import HTTPStatus
from datetime import datetime, timedelta
from ..views import usuarios, helper, livros


@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():
  return usuarios.cadastrar_usuario()

@app.route('/auth', methods=['POST'])
def authenticate():
  return helper.auth()

@app.route("/livro", methods=["POST"])
@helper.token_required
def cadastrar_livro(current_user):
  return livros.cadastrar_livro(current_user)

@app.route("/livro/<nome_livro>", methods=["GET"])
@helper.token_required
def buscar_livro(current_user, nome_livro):
  return livros.buscar_livro(current_user, nome_livro)
   
@app.route("/livro/<livro_id>", methods=["DELETE"])
@helper.token_required
def deletar_livro(current_user, livro_id):
  return livros.deletar_livro(current_user, livro_id)