import os
import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['djangowebone.azurewebsites.net']

DATABASES = {
    'default': dj_database_url.config()
}

REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        'TIMEOUT': 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = os.environ['<YOUR_SMTP_APP_NAME>']
EMAIL_HOST_USER = os.environ['<YOUR_SMTP_APP_NAME>_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['<YOUR_SMTP_APP_NAME>_PASSWORD']
EMAIL_PORT = os.environ['<YOUR_SMTP_APP_NAME>_PORT']
