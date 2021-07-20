from json import dumps as json_dumps
from modules.auth import validate_token, auth_required
import bottle
from modules.bottles import BottleJson

app = BottleJson()

@app.post("/wiki-info/login")
def store_record(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Bad Request ")

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
