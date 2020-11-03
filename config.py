import os

SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'postgres://dlntzgezpcdfla:7398e6b6470f4b8a749e9d184e6433b872921170d71ce0b914407ffa263356a3@ec2-54-160-202-3.compute-1.amazonaws.com:5432/d296dsetq9a197'
SQLALCHEMY_TRACK_MODIFICATIONS = False
