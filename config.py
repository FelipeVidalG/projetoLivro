import configparser
import os
import random
import string


gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))



# Configurações do banco de dados e app
# Substitua usuario, pelo seu usuario MYSQL
# Substitua senha, pelo sua senha MYSQL
# Substitua localhost, pelo seu HOSTNAME MYSQL
# Substitua 3306, pela sua PORTA MYSQL
# Substitua projetoLivros, pela seu DataBase MYSQL

SQLALCHEMY_DATABASE_URI = 'mysql://usuario:senha**@localhost:3306/projetoLivros'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
DEBUG = True