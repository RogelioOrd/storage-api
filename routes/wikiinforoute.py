import datetime as dt
import bottle
from bottle import route, run, post, request
from modules.bottles import BottleJson
from modules.wikiinfo import add_publi


app = BottleJson()

#curl http://localhost:8080/url_messa/store  -X POST -H 'Content-Type: application/json'  -d '{"id" : "1" , "username" : "rogelio" , "password" : "1234" , "fecha":"2021-08-01" , "correo" : "tucorreofake@correo.com"}'
## Add a new user
@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        username = str(payload['username'])
        password = str(payload['password'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        email = str(payload['email'])
        print("Datos Aceptados")
        respuesta = add_user(**payload)
        print(respuesta)
        print("Datos Correctos")
    except:
        print("Datos incorrectos")
        raise bottle.HTTPError(405, "datos invalidos")
    raise bottle.HTTPError(201, respuesta)

@app.get("/wiki-info/profile")
def get_all_info(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")

@app.get("/wiki-info/query")
def get_info_by_sn(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")

@app.get("/wiki-info/profile")
def get_all_info(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code = 501, message = "Not implemented")
