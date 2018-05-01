import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
ALLOWED_HOSTS = os.environ['DJANGO_ALLOWED_HOSTS'].split(',')

# Limits rate of use to hinder attempts to brute-force the entire set of possible IDs
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle', ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/second',
    }
}
