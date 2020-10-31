from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    token = db.Column(db.String, nullable=False)
    blogs = db.relationship('blogs')


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
