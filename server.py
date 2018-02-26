# imports app variable that is instance of app package
from app import app, db

# Imports user model
from app.models import User

# Imports application instance when shell command ran for testing purposes
# Returns contents of db when shell command ran.
# Use dict keys to access db and User
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}
