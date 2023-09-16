from pathlib import Path

from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env(DEBUG=(bool, False))
Env.read_env(str(BASE_DIR / ".env"))


SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool('DEBUG')

EMAIL_CONFIRM = env.bool('EMAIL_CONFIRM')

DOCKER = env('DOCKER', default=False)

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


INSTALLED_APPS = [
    'news',
    'users',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_spectacular'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "it_bel_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "it_bel_project.wsgi.application"


if DOCKER:
    from .db_config import DOCKER_DB

    DATABASES = DOCKER_DB
else:
    from .db_config import LOCAL_DB

    DATABASES = LOCAL_DB


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'users.User'

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler',
}

DJOSER = {
    'LOGIN_FIELD': 'email',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'IT_BEL API',
    'DESCRIPTION': 'Epic',
    'VERSION': '1.0.0',
}

FIXTURE_DIRS = [
    'fixtures',
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
    }
}

if EMAIL_CONFIRM:
    IT_BEL_USER_CONFIRM_KEY = 'user_confirm_{token}'
    IT_BEL_PASSWORD_RESET_CODE = 'password_reset_{token}'
    IT_BEL_USER_CONFIRM_TIMEOUT = 300

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False

    EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
