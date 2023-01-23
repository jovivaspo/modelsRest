"""Flask configuration."""
from os import getenv

class Config:
   JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
   PROPAGATE_EXCEPTIONS = True


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

