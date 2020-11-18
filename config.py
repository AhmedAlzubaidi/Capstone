import os

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
