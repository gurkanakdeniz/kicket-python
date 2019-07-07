import os
import json

basedir = os.path.abspath(os.path.dirname(__file__))
directory = basedir + "/codes"

git_config = {}
try:
    with open(basedir + '/config.json') as json_data_file:
        data = json.load(json_data_file)

    git_config = data.get("git")

except Exception as e:
    print(e)

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    ROOT_PATH = directory
    GIT_ROOT_PATH = directory
    GIT_URL = os.getenv('GIT_URL', git_config.get("GIT_URL"))
    GIT_BRANCH = os.getenv('GIT_BRANCH', git_config.get("GIT_BRANCH"))
    GIT_TOKEN = os.getenv('GIT_TOKEN', git_config.get("GIT_TOKEN"))
    GIT_AUTH_URL = os.getenv('GIT_AUTH_URL', git_config.get("GIT_AUTH_URL"))
    GIT_ACTIVE = os.getenv('GIT_ACTIVE', git_config.get("GIT_ACTIVE"))
