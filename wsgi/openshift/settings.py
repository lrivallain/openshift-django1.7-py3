"""
Django settings for openshift project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Running on OpenShift ?
ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
     ON_OPENSHIFT = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if ON_OPENSHIFT:
    try:
        SECRET_KEY = os.environ['DJANGO_SETTINGS_SECRET_KEY']
    except KeyError:
        print("Please create env variable DJANGO_SETTINGS_SECRET_KEY (cf README)")
else:
    SECRET_KEY = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz' # dev key

# SECURITY WARNING: don't run with debug turned on in production!
if ON_OPENSHIFT:
     DEBUG = False
else:
     DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Enable debug for only selected hosts
if DEBUG:
     ALLOWED_HOSTS = []
else:
     ALLOWED_HOSTS = ['*']

# List of admins (+ 500 error report by mail)
ADMINS = (
    ('Name', 'mail@example.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'openshift.urls'

WSGI_APPLICATION = 'openshift.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if ON_OPENSHIFT: # production settings
    DATABASES = {
         'default': { # you can change the backend to any django supported
            'ENGINE':   'django.db.backends.mysql',
            'NAME':     os.environ['OPENSHIFT_APP_NAME'],
            'USER':     os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
            'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
            'HOST':     os.environ['OPENSHIFT_MYSQL_DB_HOST'],
            'PORT':     os.environ['OPENSHIFT_MYSQL_DB_PORT'],
         }
    }
else: # dev settings
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr_FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
if ON_OPENSHIFT:
    STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
STATIC_URL = '/static/'
