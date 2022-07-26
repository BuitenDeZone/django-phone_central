"""Base configuration."""

import environ
from pathlib import Path
from split_settings.tools import include as include_settings, optional as optional_settings

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'static/'

WEBPACK_LOADER = {
    'MANIFEST_FILE': BASE_DIR / 'frontend/build/manifest.json',
}

include_settings('components/*.py', optional_settings('local_settings.py'))
