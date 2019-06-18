from app import app
from app.services import create, run

def jedi():
    return "return of the jedi"

def createApi(body):
    return create(body['imports'], body['method'])

def runApi(uuid):
    return run(uuid)
