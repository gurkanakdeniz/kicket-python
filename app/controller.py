from app import app
from app.services import create, run, example

def jedi():
    return "return of the jedi"

def createApi(body):
    return create(body['code'])

def runApi(uuid):
    return run(uuid)

def exampleApi():
    return example()
