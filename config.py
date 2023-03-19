import os

from sqlalchemy import create_engine

import urllib
class Config(object):
    SECRET_KEY='MY_SECRET_KEY'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG = True
    # Cadena de conexión de la BD // NombreUsuario:Password
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@127.0.0.1/idgs801'
    SQLALCHEMY_TRACK_MODIFICATION = False