from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# creates application object and initializes new instance of flask
app = Flask(__name__)

# tells flask to apply the config object set
app.config.from_object(Config)

# DB object
db = SQLAlchemy(app)

# Migration object
migrate = Migrate(app, db)

login = LoginManager(app)

# forces users to login, telling to use login view function.
# protects views until after logging in.
login.login_view = 'login'

# Initialize bootstrap
bootstrap = Bootstrap(app)

# modules imported here to fix circular imports that occur with flask apps
from app import routes, models