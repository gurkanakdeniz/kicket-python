from flask import request, redirect
from app import app
from app.controller import jedi, createApi, runApi, exampleApi

@app.route('/')
def index():
    return jedi()

@app.route('/create', methods=['POST'])
def create():
    return createApi(request.get_json())

@app.route('/run/<string:uuid>', methods=['POST'])
def run(uuid):
    return runApi(uuid, request.get_json())

@app.route('/run/<string:uuid>', methods=['GET'])
def runGet(uuid):
    return runApi(uuid, None)

@app.route('/example', methods=['GET'])
def example():
    return exampleApi()

# @app.errorhandler(Exception)
# def error_page(e):
#     return redirect('/')
