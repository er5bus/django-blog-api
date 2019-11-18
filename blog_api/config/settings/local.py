"""
Django base settings for social network project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from .base import *

# ######### CACHE CONFIGURATION ###############################

# https://docs.djangoproject.com/en/dev/ref/settings/#caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# ##### APPLICATION CONFIGURATION #########################

# Toolbar configuration
# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)