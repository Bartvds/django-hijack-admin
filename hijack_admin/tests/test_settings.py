"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True

SITE_ID = 1

APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:', }
}

LOGIN_REDIRECT_URL = '/hello'
HIJACK_LOGIN_REDIRECT_URL = '/hello/'
HIJACK_LOGOUT_REDIRECT_URL = '/hello/'

ROOT_URLCONF = 'hijack_admin.tests.urls'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_ROOT, '../app_static')
MEDIA_ROOT = os.path.join(APP_ROOT, '../app_media')
STATICFILES_DIRS = (os.path.join(APP_ROOT, 'static'), )

NOSE_ARGS = []

TEMPLATE_DIRS = (os.path.join(APP_ROOT, 'tests/test_app/templates'), )

PASSWORD_HASHERS = ('django.contrib.auth.hashers.PBKDF2PasswordHasher',
                    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
                    'django.contrib.auth.hashers.BCryptPasswordHasher',
                    'django.contrib.auth.hashers.SHA1PasswordHasher',
                    'django.contrib.auth.hashers.MD5PasswordHasher',
                    'django.contrib.auth.hashers.CryptPasswordHasher', )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request', )

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
    'compat',
    'hijack',
]

INTERNAL_APPS = [
    'hijack_admin',
    'hijack_admin.tests.test_app',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

SECRET_KEY = 'foobar'

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

HIJACK_ALLOW_GET_REQUESTS = True