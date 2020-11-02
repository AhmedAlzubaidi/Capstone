from flask import Flask, jsonify, redirect
from flask_cors import CORS
from models.blog import setup_db
from controllers.blogs_controller import blogs


app = Flask(__name__)
app.config.from_object('config')
CORS(app)
setup_db(app)
app.register_blueprint(blogs, url_prefix='/blogs')


@app.route('/')
def index():
    redirect('/blogs')


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }), 401


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404


@app.errorhandler(500)
def internal(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
