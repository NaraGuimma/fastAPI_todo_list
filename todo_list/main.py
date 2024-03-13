from fastapi import FastAPI,Request
from fastapi.responses import RedirectResponse
# cria um objeto template reutilizável
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import json

app=FastAPI()

templates=Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    with open('database.json') as f:
        data = json.load(f)
    return templates.TemplateResponse("todo_list.html",{"request":request,"tododict":data})

@app.get("/delete/{id}")
async def delete_todo(request:Request,id:str):
    with open('database.json') as f:
        data=json.load(f)
    del data[id]
    with open('database.json','w') as f:
        json.dump(data,f)
    return RedirectResponse("/",303)


@app.post("/add")
async def add_todo(request:Request):
    with open('database.json') as f:
        data=json.load(f)
    formdata=await request.form()
    print(formdata)
    print(dict(formdata))
    newdata={}
    i=1
    for id in data:
        newdata[str(i)]=data[id]
        i+=1
    newdata[str(i)]=dict(formdata)
    print(newdata)
    with open('database.json','w') as f:
        json.dump(newdata,f)
    return RedirectResponse("/",303)