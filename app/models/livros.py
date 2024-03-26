import datetime

from app import db, ma

class Livros(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60), nullable=False)
    data_lancamento = db.Column(db.DateTime, nullable=True)
    isbn = db.Column(db.String(17), nullable=False)
    autor = db.Column(db.String(60), nullable=False)

    def __init__(self, nome, data_lancamento, isbn, autor):
        self.nome = nome
        self.data_lancamento = data_lancamento
        self.isbn = isbn
        self.autor = autor

# Definindo o Schema do Marshmallow para facilitar a utilização de JSON

class LivrosSchema(ma.Schema):

    class Meta:
        fields = ('id', 'nome', 'data_lancamento', 'isbn', 'autor')


livro_schema = LivrosSchema()
livros_schema = LivrosSchema(many=True)