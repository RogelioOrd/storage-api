import datetime as dt
import bottle
from bottle import route, run, post, request
from modules.bottles import BottleJson
from modules.wikiinfo import *


app = BottleJson()


@app.post("/store")
def store(*args, **kwargs):
    '''Add a new user
    Para probar esta rutauno puede ejecutar el siguiente comando

        curl http://localhost:8081/wikiinfo/store \
            -X POST \
            -H 'Content-Type: application/json' \
            -d '{"id" : "1" , "username" : "rogelio" , "password" : "1234" , "mail" : "tucorreofake@correo.com"}'

    '''
    payload = bottle.request.json
    print(payload)
    try:
        id = str(payload['id'])
        username = str(payload['username'])
        password = str(payload['password'])
        mail = str(payload['mail'])
        print("Datos Aceptados")
        respuesta = add_user(**payload)
        print(respuesta)
        print("Datos Correctos")
    except:
        print("Datos incorrectos")
        raise bottle.HTTPError(400, "datos invalidos")
    raise bottle.HTTPError(201, respuesta)

'''
## Ver Usuarios
curl http://localhost:8081/wikiinfo/store/1/rogelio \
-X GET \
'''
@app.get("/<id>/<username>")
def users(*args, id=None, username=None, **kwargs):
    try:
       respuesta = get_users(id=id, username=username)
    except:
        raise bottle.HTTPError(500, "Error")
    raise bottle.HTTPError(200, respuesta)

'''
## Añadir una Wiki
curl http://localhost:8081/wikiinfo/store \
-X POST \
-H 'Content-Type: application/json'  \
-d '{"publicatrion_id" : "1" , "titulo" : "titulo Random" , "autor" : "rogelio" , "categoria" : "ciencia" , "fecha":"2021-01-01" , "publication" : "contenido de la publicacion", "bibliografia" : "fuentes de informacion"}' \
'''
@app.post("/wikis")
def noticias(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        publication_id = str(payload['publication_id'])
        titulo = str(payload['titulo'])
        autor = str(payload['autor'])
        categoria = str(payload['categoria'])
        fecha = dt.date.fromisoformat(payload['fecha'])
        publication = str(payload['publication'])
        bibliografia = str(payload['bibliografia'])
        print("Datos Aceptados")
        respuesta = add_noticia(**payload)
        print(respuesta)
        print("Done")
    except:
        print("Datos incorrectos")
        raise bottle.HTTPError(400, "datos no validos")
    raise bottle.HTTPError(201, respuesta)

'''
## ver wikis
curl http://localhost:8081/wikiinfo/1 \
-X GET \
'''
@app.get("/<publication_id>")
def get_publi(*args, id_noticia=None, **kwargs):
    try:
       respuesta = get_publi(publicatrion_id)
    except:
        raise bottle.HTTPError(500, "Error")
    raise bottle.HTTPError(200, respuesta)

###################################################################
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
