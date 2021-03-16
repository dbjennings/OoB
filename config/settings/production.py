import environ
from .base import *

ENV = environ.Env()

ALLOWED_HOSTS = []

DATABASES = {
    'default': ENV.db()
}