from flask_sqlalchemy import SQLAlchemy
from webapp import app

db = SQLAlchemy(app)

class Event(db.Model):
    name_id = db.Column(db.String(255), primary_key=True)
    common_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
