import uuid
import os
import sys
import json
from app import app
from app.config import Config

def example():
    example = {'exampleCode' : "def ex():\n\treturn \"jedi\"", 'exampleRequest' : "{}"}
    return json.dumps(example)

def create(code):
    uuidStr = str(uuid.uuid4()).replace("-", "")
    createFolder(uuidStr)
    createFile(uuidStr,code)
    createResponse = {'endpoint' : uuidStr, 'platform' : "python"}
    return json.dumps(createResponse)

def run(uuidStr):
    m = load_module(uuidStr)
    response = {'response' : str(m.ex())}
    return json.dumps(response)

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
