# api_consultaies
API Rest da aplicação Consulta IES, feita em Python e construída no Django Rest Framework.

Os modelos se encontram em models.py, e foram feitos baseados nas colunas do BD feito para a aplicação.


INICIALIZAÇÃO


Após a instalação, basta executar os seguintes comandos:


> cd restapi


> python manage.py runserver


UTILIZAÇÃO NA APLICAÇÃO


Os seus dados são puxados pelo Consulta IES para apresentar as informações requisitadas, através de endpoints configurados nos arquivos views.py & urls.py.


Endpoints:


>  /api/ies/[]
  
  
>  /api/curso/?search=[]
