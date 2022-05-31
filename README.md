# API- Consulta_IES
API Rest da aplicação Consulta IES. 

## Objetivo

Fornecer dados sobre as instituiçõoes pública e privadas de ensino superior. 

## Formas de Instalação

### Via Docker Compose

Basta clonar o repositório e utilizar o docker-compose para inciar a API.

### Via Python

Basta clonar o projeto, e utilizar o PIP para instalar as dependências do projeto logo após seguir os passos da inicialização.


> pip install requirements.txt


> cd restapi


> python manage.py runserver


## UTILIZAÇÃO NA APLICAÇÃO

Swagger pode ser acessado:

Aqui é possível acessar as informações dos endpoints e ainda visualizar os models da API.

> http://localhost:8000/swagger/

Endpoints:
>  /api/ies/[]
  
  
>  /api/curso/?search=[]

