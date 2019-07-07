from app import app
from app.config import Config
from app.services import create, run, example
from app.gitter import commit_push
import json

def jedi():
    return "return of the jedi"

def createApi(body):
    response = create(body['code'], getArgs(body, 'uuid'))

    try:
        if Config.GIT_ACTIVE == "true":
            commit_push(response["endpoint"])
    except Exception as e:
        print(e)

    return json.dumps(response)

def runApi(uuid, body):
    return run(uuid, getArgs(body, 'args'))

def getArgs(body, args):
    try:
        return body.get(args)
    except Exception as e:
        return None

def exampleApi():
    return example()
