import uuid
import os
import sys
from app import app
from app.config import Config

def create(imports, method):
    uuidStr = str(uuid.uuid4()).replace("-", "")
    createFolder(uuidStr)
    createFile(uuidStr, imports, method)
    return uuidStr

def run(uuidStr):
    m = load_module(uuidStr)
    return str(m.ex())

def createFolder(uuidStr):
    path = getPath(uuidStr)
    if not os.path.exists(path):
        os.makedirs(path)

def createFile(uuidStr, imports, method):
    f = open(getFilePath(uuidStr),"w+")
    f.write(imports)
    f.write(method)
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
