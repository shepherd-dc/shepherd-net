from datetime import timedelta

import os

DEBUG = True
SECRET_KEY = os.urandom(24)
TOKEN_EXPIRATION = 7 * 24 * 3600
REMEMBER_COOKIE_DURATION = timedelta(days=7)
PERMANENT_SESSION_LIFETIME = timedelta(days=7)

# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'cymysql'
USERNAME = 'root'
PASSWORD = 'Pr@ject1302'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'fisher'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'\
    .format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
