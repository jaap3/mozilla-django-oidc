import django


SECRET_KEY = 'can you keep a secret?'

DEBUG = True

USE_TZ = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

ROOT_URLCONF = 'mozilla_django_oidc.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'mozilla_django_oidc',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

if tuple(django.VERSION[0:2]) >= (1, 10):
    MIDDLEWARE = []
else:
    MIDDLEWARE_CLASSES = []

OIDC_USERNAME_ALGO = None
