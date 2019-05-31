from datetime import datetime

from blog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    username = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(240))
    body = db.Column(db.Text(), nullable=False)