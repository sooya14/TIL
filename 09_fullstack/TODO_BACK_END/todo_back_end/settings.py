"""
Django settings for todo_back_end project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@&y*gm2zlu+^wc1#@widf4_r@kkjz%l)pssvlr+tx_@kuln!n*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# REST_framework 설정
REST_FRAMEWORK = {
		# 로그인 여부를 확인하는 클래스
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
		# 인증 여부를 확인하는 클래스
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# JWT 설정
JWT_AUTH = {
		# JWT를 encrypt함.절대 외부 노출 금지, default는 settings.SECRET_KEY
    'JWT_SECRET_KEY': SECRET_KEY,
		# 토큰 해싱 알고리즘(HMAC using SHA-256 hash algorithm (default)
    'JWT_ALGORITHM': 'HS256',
		# 토큰 갱신 허용 여부
    'JWT_ALLOW_REFRESH': True,
		# 1주일간 유효한 토큰 - default는 5분
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
		# 28일 마다 토큰이 갱신(유효 기간 연장시)
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
}

# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'rest_framework',
    'corsheaders',  # CORS 관련 설정 담당. 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todos',
    'accounts',
]

MIDDLEWARE = [
    # CorsMiddleware should be placed as high as possible especially
    # before any middleware that can generate responses such as
    # Django's CommonMiddleware
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todo_back_end.urls'

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

WSGI_APPLICATION = 'todo_back_end.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# CORS_ORIGIN_WHITELIST = [
#     "http://127.0.0.1:8000",
#     "http://my-cool-site.com"
# ]
CORS_ORIGIN_ALLOW_ALL = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'accounts.User'
