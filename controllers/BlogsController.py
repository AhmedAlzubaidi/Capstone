from flask import Blueprint

blogs = Blueprint('blogs', __name__, url_prefix='/blogs', template_folder='templates')


@blogs.route('/')
def index():
    return 'get all blogs'


@blogs.route('/<int:id>')
def get_blog():
    return 'get blog'


@blogs.route('/create')
def create_form():
    return 'create blog form'


@blogs.route('/', method='POST')
def store():
    return 'store blog'


@blogs.route('/<int:id>/edit')
def edit_blog_form():
    return 'edit blog form'


@blogs.route('/<int:id>', method='PUT')
def edit_blog():
    return 'edit blog'


@blogs.route('/<int:id>', method='DELETE')
def delete_blog():
    return 'delete blog'
