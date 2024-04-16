from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'concesionario',
        'USER': 'postgres',
        'PASSWORD': 'perdomopulido30',
        'HOST': 'localhost',
        'DATABASE_PORT':'5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'