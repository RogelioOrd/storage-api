from json import dumps as json_dumps
from modules.auth import validate_token, auth_required
import bottle

app = bottle.Bottle()

@app.post("/encuesta")
def store_record(*args, **kwargs):
    bottle.response.status = 404
    bottle.response.content_type = "application/json"
    return dict(code= 404, message = "Bad Request ")

@app.get("/consulta")
def get_all_info(*args, **kwargs):
    bottle.response.status = 500
    bottle.response.content_type = "application/json"
    return dict(code = 500, message = "Not implemented")

@app.get("/historial")
def get_info_by_sn(*args, **kwargs):
    bottle.response.status = 400
    bottle.response.content_type = "application/json"
    return dict(code = 400, message = "Not found")
