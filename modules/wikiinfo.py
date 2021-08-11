import datetime
import hashlib
import models.auth
from bottle import response, request
import jwt

"""
    Funcion para generar una nueva wiki
    recibe los argumentos
     - id, es una cadena de texto compuesta por el nombre de la nota y la fecha de creacion
     - titulo, una cadena de texto que corresponda al nombre de la nota.
     - autor, una cadena de texto que corresponda a quien escribio la wiki.
     - categoria, una cadena de texto que carga el mensaje a estructurar.
     - fecha, cadena de texto correspondiente a la fecha en que se publico.
     - publicacion, una cadena de texto en la cual se alamacena todo el contenido de la wiki.
     - bibliografia, una cadena de texto donde se encontraran enlaces o referencias de donde proviene la informacion.

    La fecha de creacion de agregara automaticamente, al igual que el identificador correspondiente.
    Los campos que seran necesarios de llenar serian el titulo, categoria, la publicacion y la bibliografia.
    Esta funcion regresara un diccionario con el id, titulo, autor, categoria, fecha, publicacion y bibliografia.
"""

publi =[]
def add_publi(publication_id, titulo,autor, categoria, fecha_publicacion, publicacion, bibliografia):
    pub = {
        "publication_id": publication_id,
        "titulo": titulo,
	    "autor": autor,
        "categoria": categoria,
        "fecha_publicacion": fecha,
	    "publicacion": info,
	    "bibliografia": biblografia
    }
    news.append(pub)
    return json.dumps(pub)

#def get_publi()
#    return print(publi)


"""
    Funcion para generar un nuevo usuario
    recibe los argumentos
     - id, es una cadena de texto compuesta por el nombre de la nota y la fecha de creacion
     - username, una cadena de texto que corresponda al nombre de usuario.
     - password, una cadena de texto que corresponda a la contraseña.
     - fecha, cadena de texto correspondiente a la fecha en que se publico.
     - email, una cadena de texto en la cual se hace referenacia al correo del usuario.

    La fecha de creacion de agregara automaticamente, al igual que el identificador correspondiente.
"""
def add_user(id = None, username = None, password = None, mail = None):

    print("Datos del usuario")
    print(id, username, password, email)
    print("Capturado")


    almacenable = {
        "id": id,
        "username": username,
        "password": password,
        "mail": mail,
    }
    nombre_archivo = f"{username}-{password}-{id}-{mail}.json"
    datos_usuario = store_string(
        "user/users",
        nombre_archivo,
        json.dumps(almacenable)
    )
    return datos_usuario

def get_user(users=None):
    query_result = query_storage(
        "user/users",
    )
    if users is None:
        return query_result["content"]
