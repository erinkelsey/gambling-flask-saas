from datetime import timedelta

from celery.schedules import crontab
from decouple import config

LOG_LEVEL = config('LOG_LEVEL')  # CRITICAL / ERROR / WARNING / INFO / DEBUG
DEBUG = config("DEBUG", default=False, cast=bool)
TESTING = config("TESTING", default=False, cast=bool)
SECRET_KEY = config("SECRET_KEY")

if DEBUG or TESTING:
    SERVER_NAME = 'localhost'

# ngrok
# SERVER_NAME = '815237b8bad7.ngrok.io'

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
CELERYBEAT_SCHEDULE = {
    'mark-soon-to-expire-credit-cards': {
        'task': 'snakeeyes.blueprints.billing.tasks.mark_old_credit_cards',
        'schedule': crontab(hour=0, minute=0)
    },
    'expire-old-coupons': {
        'task': 'snakeeyes.blueprints.billing.tasks.expire_old_coupons',
        'schedule': crontab(hour=0, minute=1)
    },
}

# SQLAlchemy.
db_uri = config('DB_URI')
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User.
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)

# Google Analytics
ANALYTICS_GOOGLE_UA = config('ANALYTICS_GOOGLE_UA')

# Billing.
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = config('STRIPE_PUBLISHABLE_KEY')
STRIPE_API_VERSION = '2016-03-07'
STRIPE_PLANS = {
    '0': {
        'id': 'bronze',
        'name': 'Bronze',
        'amount': 100,
        'currency': 'usd',
        'interval': 'month',
        'interval_count': 1,
        'trial_period_days': 14,
        'statement_descriptor': 'SNAKEEYES BRONZE',
        'metadata': {}
    },
    '1': {
        'id': 'gold',
        'name': 'Gold',
        'amount': 500,
        'currency': 'usd',
        'interval': 'month',
        'interval_count': 1,
        'trial_period_days': 14,
        'statement_descriptor': 'SNAKEEYES GOLD',
        'metadata': {
            'recommended': True
        }
    },
    '2': {
        'id': 'platinum',
        'name': 'Platinum',
        'amount': 1000,
        'currency': 'usd',
        'interval': 'month',
        'interval_count': 1,
        'trial_period_days': 14,
        'statement_descriptor': 'SNAKEEYES PLATINUM',
        'metadata': {}
    }
}
