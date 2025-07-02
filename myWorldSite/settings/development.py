# myWorldSite/settings/development.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000"]

SECRET_KEY="django-insecure-+_*5l5k^n0)^%=irfj-6sc6(kloy%byi@n^(%#"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
