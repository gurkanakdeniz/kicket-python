from flask import Flask
from app.config import Config
import os

app = Flask(__name__)

if not os.path.exists(Config.ROOT_PATH):
    os.makedirs(Config.ROOT_PATH)

from app import routes, models, controller, services
