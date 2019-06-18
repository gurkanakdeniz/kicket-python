import os
basedir = os.path.abspath(os.path.dirname(__file__))
directory = basedir + "/codes"

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    ROOT_PATH = directory
