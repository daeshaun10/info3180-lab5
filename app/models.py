# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime
# from sqlalchemy import Column, String, Integer

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    desc = db.Column(db.String)
    poster = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, desc, poster):
        self.title = title
        self.desc = desc
        self.poster = poster

    def __repr__(self):
        return '<Movies %r>' % (self.title)
