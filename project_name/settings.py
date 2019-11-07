"""Django settings for project."""
import os
from datetime import timedelta
from distutils.util import strtobool
from typing import Any, Dict, List, Optional

BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Security

SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY")
DEBUG: bool = strtobool(os.getenv("DEBUG", "False"))
ALLOWED_HOSTS: List[str] = os.getenv("ALLOWED_HOSTS", "").split(",")
CORS_ORIGIN_ALLOW_ALL: bool = True
CSRF_COOKIE_SECURE: bool = not DEBUG
SESSION_COOKIE_SECURE: bool = not DEBUG
SECURE_CONTENT_TYPE_NOSNIFF: bool = not DEBUG
SECURE_BROWSER_XSS_FILTER: bool = not DEBUG
SECURE_HSTS_SECONDS: bool = not DEBUG
SECURE_HSTS_INCLUDE_SUBDOMAINS: bool = not DEBUG
SECURE_HSTS_PRELOAD: bool = not DEBUG
X_FRAME_OPTIONS: str = "DENY"

# Application definition

INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "project_name",
]

MIDDLEWARE: List[str] = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "project_name.urls"

TEMPLATES: List[Dict[str, Any]] = [
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

WSGI_APPLICATION: str = "project_name.wsgi.application"

# Database

DATABASES: dict = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    },
}

# Password validation

AUTH_PASSWORD_VALIDATORS: List[Dict[str, str]] = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Mail settings

EMAIL_HOST: Optional[str] = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER: Optional[str] = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD: Optional[str] = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT: Optional[str] = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS: bool = strtobool(os.getenv("EMAIL_USE_TLS", "False"))
EMAIL_USE_SSL: bool = strtobool(os.getenv("EMAIL_USE_SSL", "True"))
SERVER_EMAIL: Optional[str] = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL: Optional[str] = EMAIL_HOST_USER

# Cache

MEMCACHED_HOST: str = os.getenv("MEMCACHED_HOST", "cache")
MEMCACHED_PORT: str = os.getenv("MEMCACHED_PORT", "11211")

CACHES: dict = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "{}:{}".format(MEMCACHED_HOST, MEMCACHED_PORT),
    }
}

# Redis

REDIS_HOST: str = os.getenv("REDIS_HOST", "redis")
REDIS_PORT: str = os.getenv("REDIS_PORT", "6379")
REDIS_DB: str = os.getenv("REDIS_DB", "0")

# Celery broker

CELERY_BROKER_URL: str = "redis://{}:{}/{}".format(REDIS_HOST, REDIS_PORT, REDIS_DB)

# Internationalization

LANGUAGE_CODE: str = "en-us"
TIME_ZONE: str = "UTC"
USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True

# Static files (CSS, JavaScript, Images)

STATIC_ROOT: str = os.path.join("storage", "static")
STATIC_URL: str = os.getenv("STATIC_URL", "/static/")
MEDIA_ROOT: str = os.path.join("storage", "media")
MEDIA_URL: str = os.getenv("MEDIA_URL", "/media/")
FILE_UPLOAD_PERMISSIONS: int = 0o644
SITE_URL: Optional[str] = os.getenv("SITE_URL")

# DRF settings

REST_FRAMEWORK: dict = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.QueryParameterVersioning",
    "DEFAULT_VERSION": "v1",
    "ALLOWED_VERSIONS": ["v1"],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S.%fZ",
}

# Simple JWT

SIMPLE_JWT: dict = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=3),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# Documentation

SWAGGER_SETTINGS: dict = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"},
    },
}

# Logging

LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d] %(message)s"
        },
        "short": {"format": "[%(asctime)s] %(levelname)s/%(name)s: %(message)s"},
    },
    "filters": {
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "short",
            "filters": ["require_debug_true"],
        },
        "file": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "error.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 10,  # 10 MB
            "backupCount": 5,
        },
        "celery": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs", "celery.log"),
            "formatter": "short",
            "maxBytes": 1024 * 1024 * 10,  # 10 mb
            "backupCount": 5,
        },
    },
    "loggers": {
        "": {"handlers": ["console", "file"], "propagate": False},
        "celery": {"handlers": ["console", "celery"], "level": "DEBUG"},
    },
}
