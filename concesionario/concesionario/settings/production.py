from .base import *
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# SECURITY WARNING: don't run with debug turned on in production!

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