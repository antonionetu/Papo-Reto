import os

from dotenv import load_dotenv
from pathlib import Path

from .utils import clean_allowed_hosts



BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == 'True'
ALLOWED_HOSTS = clean_allowed_hosts(os.getenv("ALLOWED_HOSTS"))

INSTALLED_APPS = [
    # Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom
    'apps.posts',
    'apps.entities'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

CONNECTION_STRING = os.getenv('DATABASE_CREDENTIALS')
CONNECTION_DICT = {
    key: value 
    for pair in connection_string.split(" ") 
        for key, value in [pair.split("=")]
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": CONNECTION_DICT['dbname'],
        "USER": CONNECTION_DICT['user'],
        "PASSWORD": CONNECTION_DICT['password'],
        "HOST": CONNECTION_DICT['host'],
        "PORT": CONNECTION_DICT['5432'],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
