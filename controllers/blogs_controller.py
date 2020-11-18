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
        'blogs': [blog.format() for blog in Blog.query.all()]
    })


@blogs.route('/<int:blog_id>')
@requires_auth('view_blog')
def get_blog(payload, blog_id):
    blog = Blog.query.get(blog_id)

    if not blog:
        abort(404)

    return jsonify({
        'success': True,
        'user_id': payload['sub'],
        'blog': blog.format()
    })


@blogs.route('/', methods=['POST'])
@requires_auth('create_blog')
def store(payload):
    data = request.get_json()
    blog = None

    if 'title' not in data or 'content' not in data:
        abort(400)

    try:
        blog = Blog(
            author_id=payload['sub'],
            title=data['title'],
            content=data['content'],
        )

        db.session.add(blog)
        db.session.expunge(blog)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500)
    finally:
        db.session.close()

    return jsonify({
        'success': True,
        'blog': blog.format()
    })


@blogs.route('/<int:blog_id>', methods=['PUT'])
@requires_auth('edit_blog')
def edit_blog(payload, blog_id):
    data = request.get_json()
    blog = Blog.query.get(blog_id)

    if not blog:
        abort(404)

    if blog.author_id != payload['sub']:
        abort(401)

    if 'title' not in data or 'content' not in data:
        abort(400)

    try:
        blog.title = data['title'],
        blog.content = data['content']
        db.session.expunge(blog)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500)
    finally:
        db.session.close()

    return jsonify({
        'success': True,
        'blog': blog.format()
    })


@blogs.route('/<int:blog_id>', methods=['DELETE'])
@requires_auth('delete_own_blog')
def delete_blog(payload, blog_id):
    blog = Blog.query.get(blog_id)

    if not blog:
        abort(404)

    if blog.author_id != payload['sub']:
        requires_auth('delete_blog')

    blog.delete()
    return jsonify({
        'success': True
    })
