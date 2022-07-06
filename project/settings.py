import os
from dotenv import load_dotenv
from distutils.util import strtobool
load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
    }
}

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = bool(strtobool(os.getenv('DEBUG', default=False)))

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default=['*'])


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
ROOT_URLCONF = 'project.urls'
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
INSTALLED_APPS = ['datacenter']



