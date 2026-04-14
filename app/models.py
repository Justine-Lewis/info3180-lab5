# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movie(db.Model):
    #Movie Database Table class initializing 
    #Table name specified is "movies" to store columns:
        #id (integer)
        #title (string)
        #description (text)
        #poster (string)
        #created_at (date/time)
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description  = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(155), nullable=False)
    created_at= db.Column(db.DateTime, default=datetime.utcnow)

    #init method
    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
        #self.created_at = created_at

    def __repr__(self):
        return f"<Movie {self.title}>"

    




