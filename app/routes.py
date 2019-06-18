from flask import request, redirect
from app import app
from app.controller import jedi, createApi, runApi

@app.route('/')
def index():
    return jedi()

@app.route('/create', methods=['POST'])
def create():
    return createApi(request.get_json())

@app.route('/run/<string:uuid>', methods=['POST'])
def run(uuid):
    return runApi(uuid)

# @app.errorhandler(Exception)
# def error_page(e):
#     return redirect('/')
