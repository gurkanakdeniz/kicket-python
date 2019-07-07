import uuid
import os
import sys
import json
import json.decoder
import time
import multiprocessing
from app import app
from app.config import Config

def example():
    example = {'exampleCode' : "def ex(args):\n\treturn args.get('jedi')", 'exampleRequest' : "{\"args\" : {\"jedi\": \"return of the jedi\"}}"}
    return json.dumps(example)

def create(code, currentUuid):
    uuidStr = currentUuid
    if currentUuid is None:
        uuidStr = str(uuid.uuid4()).replace("-", "")

    createFolder(uuidStr)
    createFile(uuidStr,code)
    createResponse = {'endpoint' : uuidStr, 'platform' : "python"}
    return createResponse

def run(uuidStr, args):
    m = load_module(uuidStr)
    manager = multiprocessing.Manager()
    processResponse = manager.dict()
    methodArgs = None;
    if args is not None:
        methodArgs = getArgs(args)

    process = multiprocessing.Process(target=runner, args= (m.ex, methodArgs, processResponse))
    m = process.start()
    # time.sleep(8)
    process.join(8)
    process.terminate()

    response = {'response' : getRunResponse(processResponse)} #str(m.ex())}
    return json.dumps(response)

def getArgs(args):
    try:
        return json.loads(args)
    except Exception as e:
        return args

def runner(fc, args, processResponse):
    result = str(fc(args))
    processResponse["result"] = result

def getRunResponse(processResponse):
    try:
        return processResponse["result"]
    except Exception as e:
        return "null"

def createFolder(uuidStr):
    path = getPath(uuidStr)
    if not os.path.exists(path):
        os.makedirs(path)

def createFile(uuidStr, code):
    f = open(getFilePath(uuidStr),"w+")
    f.write(code)
    f.close()

def load_module(module):
    MODULE_DIR = getPath(module)
    sys.path.append(MODULE_DIR)
    module_path = module
    if module_path in sys.modules:
        return sys.modules[module_path]

    return __import__(module_path, fromlist=[module])

def api_exec(code):
    exec('global i; i = %s' % code)
    global i
    return i

def getCode(uuidStr):
    f = open(getFilePath(uuidStr),"r")
    code = f.read()
    f.close()
    return code

def getPath(uuidStr):
    return Config.ROOT_PATH + "/" + uuidStr

def getFilePath(uuidStr):
    return getPath(uuidStr) + "/" + uuidStr + ".py"
