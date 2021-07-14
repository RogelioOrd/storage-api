import datetime
import hashlib
import models.auth
from bottle import response, request
import jwt

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

def get_publi()
    return print(publi)
