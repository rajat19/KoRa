from .base import *
import dj_database_url

DEBUG = os.environ.get('DEBUG') or False

ALLOWED_HOSTS.append('kora-kagaz.herokuapp.com')

if 'USE_LOCAL_DB' in os.environ and os.environ.get('USE_LOCAL_DB') is True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get("DB_NAME"),
            'USER': os.environ.get("DB_USER"),
            'PASSWORD': os.environ.get("DB_PASSWORD"),
            'HOST': os.environ.get("DB_HOST"),
            'PORT': os.environ.get("DB_PORT"),
        }
    }
else:
    DATABASES['default'] = dj_database_url.config()

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
