from flask_sqlalchemy import SQLAlchemy
from webapp import app

def init_db():
    global db
    db = SQLAlchemy(app)

def get_db():
    global db
    return db
