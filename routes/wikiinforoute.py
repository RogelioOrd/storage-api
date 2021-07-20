from modules.bottles import BottleJson

app = BottleJson()

@app.get("/")
@app.get("/<name>")
@app.get("/<name>/<age:int>")
def index(name="mariano", age=10):
    payload = bottle.request.query_storage
    print(name)
    print(bottle.request.query_string)
    print(payload.dict)
    print(name, age)
    raise bottle.HTTPError(501, 'Error')

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
