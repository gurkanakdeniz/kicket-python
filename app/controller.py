from app import app
from app.services import create, run, example

def jedi():
    return "return of the jedi"

def createApi(body):
    return create(body['code'], getArgs(body, 'uuid'))

def runApi(uuid, body):
    return run(uuid, getArgs(body, 'args'))

def getArgs(body, args):
    try:
        return body.get(args)
    except Exception as e:
        return None

def exampleApi():
    return example()
