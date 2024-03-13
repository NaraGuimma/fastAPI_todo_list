# fastAPI TODO list 

<img width="980" alt="Screenshot 2024-03-13 at 11 41 58" src="https://github.com/NaraGuimma/fastAPI_todo_list/assets/60903424/d099b7b9-2829-4761-a330-898a442788d7">


## Overview:
Para o desenvolvimento desse projeto precisamos ter instaladas as seguintes bibliotecas:

`pip install fastapi uvicorn jinja2 python-multipart`

O intuito do mesmo é criar uma tabela contendo as tarefas com os seus respectivos dias, permitindo com que as mesmas sejam excluidas e que outras sejam inseridas na lista

## Rotas:

`/` - GET: obter os dados no arquivo `database.json` que faz o papel do nosso banco de dados 

`/delete/{id}` - GET: exclui o item da lista de tarefas

`/add` - POST: adiciona um item a lista de tarefas 

<img width="1406" alt="Screenshot 2024-03-13 at 11 42 50" src="https://github.com/NaraGuimma/fastAPI_todo_list/assets/60903424/bbee451b-b102-432d-8d21-1ebadc10e3cb">

## Estilizacao:

Usou-se bootstrap e css para definir o estilo dos elementos

## Organizacao do Repositório:

```
todo_list/
├── main.py
├── database.json
├── static/
│   └── styles.css
└── templates/
    └── todo_list.html

```
