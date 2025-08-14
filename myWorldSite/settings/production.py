# myWorldSite/settings/production.py
from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = [
    "www.kudzayibamhare.com",
    "radiant-brushlands-79772-293c5a123503.herokuapp.com"
]

CSRF_TRUSTED_ORIGINS = [
    "https://www.kudzayibamhare.com",
    "https://radiant-brushlands-79772-293c5a123503.herokuapp.com"
]

# Use PostgreSQL on Heroku
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Activate Django-Heroku settings
django_heroku.settings(locals())
