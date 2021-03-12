import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# default Config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY  = environ.get('SECRET_KEY')
    API_KEY  = environ.get('API_KEY')


class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False


class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True
