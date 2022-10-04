"""Flask configuration."""
from os import getenv

class Config:
    SECRET_KEY = getenv('SECRET_KEY')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
   
class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig,
}

