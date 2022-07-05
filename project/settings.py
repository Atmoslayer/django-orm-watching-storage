import os
from dotenv import load_dotenv
load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('REPLACE_ME')

DEBUG = os.getenv('DEBUG')

ROOT_URLCONF = os.getenv('ROOT_URLCONF')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

USE_L10N = os.getenv('USE_L10N')
USE_TZ = os.getenv('USE_TZ')
DEFAULT_AUTO_FIELD = os.getenv('DEFAULT_AUTO_FIELD')




