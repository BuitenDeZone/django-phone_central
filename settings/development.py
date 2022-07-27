"""Settings specific to the development environment."""
from .base import BASE_DIR
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'frontend/build',
]

WEBPACK_LOADER = {
    'MANIFEST_FILE': BASE_DIR / 'frontend/build/manifest.json',
}

SITE_DOMAIN = 'dev.buitendezone.be'
