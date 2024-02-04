from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    length = db.Column(db.String(255), nullable=False)
    poster = db.Column(db.String(255), nullable=True)
    release_date = db.Column(db.Date, nullable=True, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Movie {self.title}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)

    def __repr__(self):
        return f'<Comment {self.text}>'
