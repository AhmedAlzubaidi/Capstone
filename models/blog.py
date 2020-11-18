import os
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def setup_db(app, database_path=None):
    if database_path:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URI')

    db.app = app
    db.init_app(app)
    db.create_all()


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    author_id = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    def format(self):
        return {
            'id': self.id,
            'author_id': self.author_id,
            'title': self.title,
            'content': self.content
        }
