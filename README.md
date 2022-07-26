# django-channel-cryptocoin

![](app/static/page.png)

Uma aplicação com Django Bootsrap Websocket Vue channels redis - consulting realtime devcontainer  
Nesse exemplo vamos criar uma pagina web que vai consultar um website de crypto moedas e atualizar  
automaticamente com websockets, utilizadno redis e vue utilizando decontainer da microsoft.

para o uso é necessário:  
- [x] pré requisitos
    - [x] docker - Docker version 20.10.8, build 3967b7d
    - [x] docker-compose - Docker Compose version v2.2.2
    - [x] visual studio
    - [x] extensions: Remote - Containers
    - [x] [documentação](https://code.visualstudio.com/docs/remote/containers)

## Get Started

Baixe o repositorio em sua maquina tenha em mente que precisa dos pré requisitos  
Rode o devcontainer 
Abra 3 terminais do Visual Studio e execute esses comandos abaixo:  

```bash
#terminal 1
cd /app
./manager runserver

#terminal 2
cd /app
celery -A app beat -l INFO

#terminal 3
cd/app
celery -A app worker -l INFO

#abra varias instancias de browser e veja o funcionanmento
http://localhost:8000

```

## Roteiro de implementação 

- [x] criação do devcontainer
- [x] docker-compose configurando e orquestrando dockers de dependencias
- [x] instalando plugins do vscode para ajudar no desenvolviemnto
- [x] instalação do Django e suas dependencias
- [x] configurando aplicação e ambiente do django
- [x] criando html com bootstrap vue e configurações de rota
- [x] definindo diretorios de static e subindo pagina html
- [x] chamando a API de cryptos montando a pagina com os dados
- [x] instalando e configurando celery para realizar as buscas
- [x] configurando admin model no django admin e criando superuser
- [x] rodando celery gravando banco de dados e registrando dados na model
- [x] instalando e configurando channels para websocket
- [x] criando rotas de websocket para aplicacão em routing 
- [x] chamada das tarefas dentro do channels layers
- [x] configuração dos consumers e ligação na pagina com vue3


## Ajudas e curiosidades

- Depois de baixar o processo e queira ver os dados na tabela do sqlite é necessario criar um superuser
```bash 
# na pasta do projeto 
python manage.py createsuperuser
# siga as instuções ...

```

Nesse desenvolviemto, houve problemas com as versão do site da gecko,  
com html, fechamento de tags para funcionamento do vue, mas todos os problemas foram resolvidos  
o uso do devcontainer contribuiu muito para validação do projeto tando em ambiente windows com linux  

## Referencias

 - https://getbootstrap.com/
 - https://docs.celeryq.dev/en/stable/
 - https://docs.djangoproject.com/en/4.0/
 - https://www.youtube.com/watch?v=
 - https://api.coingecko.com/api/v3/coins/markets
 
 
