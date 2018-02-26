from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin

# Helps retrieve user id from the db to be loaded into user session
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# DB Model for Users
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # Formats printing of objects of the User class
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Methods that can be called to handle hashing of passwords
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)