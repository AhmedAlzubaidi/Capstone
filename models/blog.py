from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # TODO compare it with auth0 token
    author_id = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
