"""
Django settings for tango_with_django_project project.

Generated by 'django-admin startproject' using Django 1.9.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # main project folder -> 'tango_with_django_project'
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')  # .../tango_with_django_project/templates/
STATIC_DIR = os.path.join(BASE_DIR, 'static') # .../tango_with_django_project/static/  -  127.0.0.1/static/...
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

print(TEMPLATE_DIR)

print("=========PATHS==========")
print(__file__)
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))  # BASE_DIR - main project folder
print(TEMPLATE_DIR)

# .../tango_with_django_project/tango_with_django_project/settings.py
# .../tango_with_django_project/tango_with_django_project
# .../tango_with_django_project
# .../tango_with_django_project/templates
# =======================================================================================


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# =========================================================================================
# SECURITY WARNING: keep the secret key used in production secret!
import json
from django.core.exceptions import ImproperlyConfigured
# JSON-based secrets module
with open("secrets.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

# ==============================================================================================

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
    'registration',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tango_with_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#====================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [STATIC_DIR, ]

#====================================================================#
# Media files:

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'


# ==============================================================================
# cookies can be either browser-length sessions or persistent sessions

SESSION_EXPIRE_AT_BROWSER_CLOSE = False # default

SESSION_COOKIE_AGE = 1209600  # seconds. --> 14 days

# http://eli.thegreenplace.net/2011/06/24/django-sessions-part-i-cookies/

#clear the database that stores cookies : $ python manage.py clearsessions

#====================================================================================
#

# DJANGO AUTHENTICATION:
#__________________________________________________________________
# URL you’d like to redirect users to that aren’t logged in:
# LOGIN_URL = '/rango/login/'

# REDUX AUTHENTICATION:
#__________________________________________________________________
# If True, users can register
REGISTRATION_OPEN = True
# One-week activation window; you may, of course, use a different value.
ACCOUNT_ACTIVATION_DAYS = 7
# If True, the user will be automatically logged in.
REGISTRATION_AUTO_LOGIN = True
# The page you want users to arrive at after they successfully log in
LOGIN_REDIRECT_URL = '/rango/'# The page users are directed to if they are not logged in,
# and are trying to access pages requiring authentication
LOGIN_URL = '/accounts/login/'



















#
