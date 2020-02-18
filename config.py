import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '972a48c7469fd846a231d1f8c2bb5ffc'
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    DATABASE_URL = "postgresql://desenvolvimento:abc,123@34.95.201.225:5432/ecommerce"
    # DATABASE_URL = "postgresql://postgres:d4t4b4S3@localhost:5432/ecommerce"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = True

class StartingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
