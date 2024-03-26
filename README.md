<h1 align="center">
<img src= "./src/image.png"/>
<p>OPORTUNIDADE</p>
</h1>

## 📘 Sobre

O projeto é uma **API REST**, com Flask e controle de acesso usando autenticação **JWT**.

## 💡 Tecnologias

- [Flask](https://flask.palletsprojects.com/en/2.3.x/) 

- [MySQL](https://dev.mysql.com/doc)

- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)

- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)


##  💻 Como configurar o ambiente

**Instalação da venv**:

Com o python instalado, crie uma Virtual Environment:
Abra o terminal (ou prompt de comando) na pasta do seu projeto e execute o seguinte comando para criar uma venv:

No **Windows**:
```bash
python -m venv venv
```
No **macOS e Linux**:
```bash
python3 -m venv venv
```
Isso criará uma pasta chamada "venv" no diretório do seu projeto com uma cópia isolada do Python e suas bibliotecas.

Ative a Virtual Environment:
No **Windows**, execute:
```bash
venv\Scripts\activate
```
No **macOS e Linux**, execute:
```bash
source venv/bin/activate
```
Ao ativar a venv, você verá o prompt de comando mudar para mostrar o nome da venv.

**Instale as dependências:**

Com a venv ativada, você pode instalar as dependências usando o pip.

Em seguida, execute o seguinte comando para instalar as dependências listadas no arquivo requirements.txt:
```bash
pip install -r requirements.txt
```
##  🚀 Como utilizar
No ínicio do código faça a configuração necessária do seu banco de dados MySQL.

Está localizada no arquivo config.py.

Após isso abra sua ferramenta para testar APIs, se não tiver eu recomendo instalar o Postman.


**CRIAR USUÁRIO**

Utilize a rota: localhost:5000/usuarios, selecione o method como *POST*, em seguida passe um json neste formato:

{
    "nome": "Felipe Vidal",
    "usuario": "felipe",
    "senha": "teste1234",
    "email": "felipevgevaerd@gmail.com"
}

**AUTENTICAR USUÁRIO**

Utilize a rota: localhost:5000/auth, selecione o method como *POST*, em seguida vá até a aba authorization, selecione Basic Auth e preencha com seu usuário:

{
    "exp": "Tue, 26 Mar 2024 21:53:33 GMT",
    "message": "Autenticado com sucesso",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImJydW5hIiwiZXhwIjoxNzExNDkwMDEzfQ.p0j0sAHkoI7KYcmSs7hFnVRvBCjPkf2nrYqHwq2ZDZc"
}

**IMPORTANTE**
Este é um exemplo de resultado, este token é o que vai ser utilizado em todos os outros endpoints para controle de acesso.



**CRIAR LIVRO**

Utilize a rota: localhost:5000/livro, selecione o method como *POST*, em seguida passe um json neste formato:

{
  "nome": "Clean Code",
  "data_lancamento": "2008-08-01",
  "isbn": "978-013-235-0884",
  "autor": "Robert Cecil Martin"
}
Na aba Params, passe uma key = token e no value, passe o token que recebeu na autenticação.

**BUSCAR LIVRO**

Utilize a rota: localhost:5000/livro/<nome do livro>, selecione o method como *GET*, em seguida substitua o <nome do livro> pelo nome do livro que deseja procurar.

Na aba Params, passe uma key = token e no value, passe o token que recebeu na autenticação.

**DELETAR LIVRO**

Utilize a rota: localhost:5000/livro/ID, selecione o method como *DELETE*, em seguida substitua o ID pelo número do ID do livro que deseja deletar.

Na aba Params, passe uma key = token e no value, passe o token que recebeu na autenticação.


## 🙋‍♂️ Créditos
Feito por Felipe Vidal Gevaerd.

