import os
from typing import List

from dotenv import load_dotenv

load_dotenv()

DEBUG = False
SECRET_KEY = NotImplemented

DEV_MODE = os.getenv('DEV_MODE')

ALLOWED_HOSTS: List[str] = ['*']
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = ['https://api.mysillydreams.com', 'https://www.api.mysillydreams.com']
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS: List[str] = []

INTERNAL_IPS = [
    '127.0.0.1',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'corsheaders',
    'rest_framework',
    'djoser',
    'social_django',
    'storages',

    # Apps
    'msd.users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'msd.project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'msd.project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'msd',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 600,
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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

if DEV_MODE:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'  # type: ignore # noqa: F821
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'  # type: ignore # noqa: F821
else:
    STORAGES = {
        'staticfiles': {
            'BACKEND': 'storages.backends.s3.S3Storage',
            'OPTIONS': {
                'access_key': '',
                'secret_key': '',
                'bucket_name': 'msd-s3-backend',
                'region_name': '',
                'querystring_auth': False,
                'endpoint_url': 'https://s3.ap-south-2.amazonaws.com',
                'location': 'static',
                'object_parameters': {
                    'CacheControl': 'max-age=86400'
                },
            },
        },
    }

    STATIC_URL = f'https://{STORAGES["staticfiles"]["OPTIONS"]["bucket_name"]}.s3.{STORAGES["staticfiles"]["OPTIONS"]["region_name"]}.amazonaws.com/static/'  # type: ignore # noqa: E501
    MEDIA_URL = f'https://{STORAGES["staticfiles"]["OPTIONS"]["bucket_name"]}.s3.{STORAGES["staticfiles"]["OPTIONS"]["region_name"]}.amazonaws.com/media/'  # type: ignore # noqa: E501

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.apple.AppleIdAuth',
    # 'social_core.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['msd.users.authentication.CustomJWTAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.UserAccount'
