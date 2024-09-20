import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-_t^dho6=39_9(z+^)zbwoth*p(xnin9p^b2!(8qlvzioll84!7"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
    "cabinet",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# NOTE: All storage things start from here:

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "media"

# MEDIA_URL = "http://localhost:4566/django-localstack/"
# MEDIA_URL = "/media/"

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "LOCATION": "media",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "LOCATION": "static",
    },
}

AWS_STORAGE_BUCKET_NAME = "django-localstack"

# Local-only settings
# AWS_ACCESS_KEY_ID = "test"
# AWS_SECRET_ACCESS_KEY = "test"
# AWS_S3_ENDPOINT_URL = "http://localhost:4566"

# Deployment-only settings
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_REGION_NAME = "us-east-1"
# AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = False
# AWS_QUERYSTRING_AUTH = False  # Disable signed URLs for public access (optional)
