import os

# references DB object in __init__.py
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    WTF_CSRF_ENABLED = True
    #Flask-WTF extension uses it secret key to protect web forms against CSRS attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xxxxx BAHAHA'

    # Uses env variable for DB path, sets tracking to false so doesnt single app everytime change is going to happen to DB
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False