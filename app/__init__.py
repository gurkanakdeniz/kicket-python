from flask import Flask
from app.config import Config
from app.gitter import clone_remote
import os

app = Flask(__name__)

if not os.path.exists(Config.ROOT_PATH):
    os.makedirs(Config.ROOT_PATH)

try:
    if Config.GIT_ACTIVE == "true":
        clone_remote()
except Exception as e:
    print(e)

from app import routes, models, controller, services, gitter
