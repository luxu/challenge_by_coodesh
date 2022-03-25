# Projeto Space Flight News

Link da apresentação: https://youtu.be/ALxOjE0vCbM

Tem como objetivo pegar os dados do site [site da API]{https://api.spaceflightnewsapi.net/v3/articles} 
e disponibilizar no nosso siSteMA para ser consumidos via API pelos clientes

Projeto rodando no heroku: [Site]{https://intense-eyrie-53568.herokuapp.com/}

### *Linguagens*
- Python

### *Frameworks*
- Django
- Django Rest Framework

### *Banco de dados*
- Postgres

### *Hospedagem*
- Heroku

## Como instalar o sistema:
- Faça o clone do projeto: 
````
git clone https://github.com/zicadopv/challenge_by_coodesh.git
````
- Entre na pasta
````
cd challenge_by_coodesh
````
- Criar uma máquina virtual, entrar e instalar as libs
````
python.exe -m venv .venv
.venv\Scripts\activate
python.exe -m pip install --upgrade pip 
pip install -r requirements.txt
````
- Faça uma cópia do arquivo **env-sample**
````
cp contrib\env-sample .env
````
- Rode as migrations
````
python manage.py migrate
````
- Criar um usuário e rodar o scripts para baixar os dados do site 
````
python manage.py createsuperuser
python api_spaceflight.py
````

## Endpoints

### Melhor maneira de acessar os endpoints é através do programa INSOMNIA

Todos artigos tem limite de 5 registros por vez, se quiser navegar pelas páginas:
````
http://localhost:8000/articles/?page=3
````

Acesso sem TOKEN
````
[GET]http://localhost:8000/articles/ -> Lista todos os artigos da base
[GET]http://localhost:8000/article_details/key/ -> Lista de um artigo específico
````
Acesso com TOKEN
````
[POST]http://localhost:8000/article/ -> Cria um novo artigo
[PUT]http://localhost:8000/article/key/ -> Edita um novo artigo
[DELETE]http://localhost:8000/article_delete/key/ -> Deleta um artigo
````
Para gerar o TOKEN é só acessar o endpoint a seguir e logar
````
[POST]http://localhost:8000/api/token/
````

Testar DEMO:
````
https://intense-eyrie-53568.herokuapp.com/
````
## ***This is a challenge by Coodesh***
