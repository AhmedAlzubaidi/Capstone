from flask import Blueprint, render_template, redirect, request, abort, jsonify
from sqlalchemy.exc import SQLAlchemyError

from models.blog import Blog, db
from middleware.auth import requires_auth

blogs = Blueprint('blogs', __name__,
                  url_prefix='/blogs', template_folder='templates')


@blogs.route('/')
def index():
    return jsonify({
        'success': True,
        'blogs': Blog.query.all()
    })


@blogs.route('/<int:blog_id>')
def get_blog(blog_id, payload):
    blog = Blog.query.get(blog_id)

    if not blog:
        abort(404)

    data = {
        'user_id': payload['sub'],
        'blog': blog
    }
    return jsonify({
        'success': True,
        'data': data
    })


@requires_auth('create_blog')
@blogs.route('/', methods=['POST'])
def store(payload):
    data = request.get_json()

    try:
        blog = Blog(
            author_id=payload['sub'],
            title=data['title'],
            content=data['content']
        )

        db.session.add(blog)
        db.session.flush(blog)
        db.session.commit()
    except (SQLAlchemyError, AttributeError) as e:
        blog = None
        db.session.rollback()
    finally:
        db.session.close()

    if not blog:
        abort(400)

    return jsonify({
        'success': True,
        'blog': blog
    })


@requires_auth('edit_blog')
@blogs.route('/<int:blog_id>', methods=['PUT'])
def edit_blog(blog_id, payload):
    data = request.get_json()
    blog = Blog.query.get(blog_id)

    if not blog:
        abort(404)

    return jsonify({
        'success': True,
        'blog': blog
    })


@requires_auth()
@blogs.route('/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id, payload):
    blog = Blog.query.get(blog_id)

    if not blog:
        abort(404)

    if blog.user_id != payload['sub']:
        requires_auth('delete_blogs')

    return jsonify({
        'success': True
    })
