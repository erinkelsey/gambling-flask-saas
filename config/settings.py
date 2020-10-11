from datetime import timedelta

from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)
TESTING = config("TESTING", default=False, cast=bool)
SECRET_KEY = config("SECRET_KEY")

if DEBUG or TESTING:
    SERVER_NAME = 'localhost'

# Toolbar
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Flask-Mail.
MAIL_USERNAME = config("MAIL_USERNAME")
MAIL_PASSWORD = config("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = config("MAIL_DEFAULT_SENDER")
MAIL_SERVER = config("MAIL_SERVER")
MAIL_PORT = config("MAIL_PORT")
MAIL_USE_TLS = True
MAIL_USE_SSL = False

# Celery.
CELERY_BROKER_URL = config("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# SQLAlchemy.
db_uri = 'postgresql://snakeeyes:devpassword@postgres:5432/snakeeyes'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)
