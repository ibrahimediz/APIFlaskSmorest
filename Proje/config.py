import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'never-guess'
    PROPOGATE_EXCEPTIONS = os.environ.get('PROPOGATE_EXCEPTIONS') or 'never-guess'
    API_TITLE = os.environ.get('API_TITLE') or 'never-guess'
    API_VERSION = os.environ.get('API_VERSION') or 'never-guess'
    OPENAPI_VERSION = os.environ.get('OPENAPI_VERSION') or 'never-guess'
    OPENAPI_URL_PREFIX = os.environ.get('OPENAPI_URL_PREFIX') or 'never-guess'
    OPENAPI_SWAGGER_UI_PATH = os.environ.get('OPENAPI_SWAGGER_UI_PATH') or 'never-guess'
    OPENAPI_SWAGGER_UI_URL = os.environ.get('OPENAPI_SWAGGER_UI_URL') or 'never-guess'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////data.db'
    JWT_SECRET_KEY= os.environ.get('JWT_SECRET_KEY') or 'jamiryo'