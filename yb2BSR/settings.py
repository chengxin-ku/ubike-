"""
Django settings for yb2BSR project.

Generated by 'django-admin startproject' using Django 4.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
from dotenv import load_dotenv
from ipinfo_django.ip_selector.default import DefaultIPSelector


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# Environment variable: ACCESS_TOKEN
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(env_path)

SECRET_KEY = os.getenv("SECRET_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
GOOGLE_MAPS_API_KEY2 = os.getenv("GOOGLE_MAPS_API_KEY2")
LINE_CLIENT_ID = int(os.getenv('LINE_CLIENT_ID'))
# LINE_CLIENT_SECRET = int(os.getenv('LINE_CLIENT_SECRET'))
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
METEOROLOGICAL_DATA_OPEN_PLATFORM = os.getenv('METEOROLOGICAL_DATA_OPEN_PLATFORM')
LINE_LOGIN_CHANNEL_SECRET = os.getenv('LINE_LOGIN_CHANNEL_SECRET')
# LINE_REDIRECT_URI = "https://08c5-2401-e180-8d51-544-1b2-96f3-db0-e241.ngrok-free.app"
LINE_REDIRECT_URI_CALLBACK=os.getenv('LINE_REDIRECT_URI_CALLBACK')
LINE_NOTIFY_URL = 'https://notify-api.line.me/api/notify'
ENGINE = os.getenv('ENGINE')
NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
#X-Forwarded-For 用
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["*"]
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mapAPP.apps.MapappConfig",
    "Line_Official_Account_Bot",
    # line 第三方登入使用
    'allauth.socialaccount.providers.line',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'web',
    'allauth.socialaccount.providers.github',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'web.backed.LineUserBackend',
]
SITE_ID = 2
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'line': {

        "SCOPE":[
            "profile",
            "openid",
            "email",
        ]
}}

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "yb2BSR.middleware.Custom404Middleware",  # 404頁面
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'ipinfo_django.middleware.IPinfoMiddleware',

]

ROOT_URLCONF = "yb2BSR.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "web", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": ["django.templatetags.static"],
        },
    }
]

WSGI_APPLICATION = "yb2BSR.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': ENGINE,
#         'NAME': NAME,
#         'USER': USER,
#         'PASSWORD': PASSWORD,
#         'HOST': HOST,
#         'PORT': PORT,
#     }
# }
#Local use
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 使用數據庫儲存 session

SESSION_ENGINE = "django.contrib.sessions.backends.db"  # 使用數據庫儲存 session
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',  # 设定日志级别为 DEBUG
            'class': 'logging.FileHandler',
            'filename': '/path/to/your/django/logs/debug.log',  # 指定日志文件路径
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'web': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# LINE_CLIENT_SECRET = 'your_line_client_secret_here'
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 使用数据库会话
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "zh-Hant"

TIME_ZONE = "Asia/Taipei"

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'web.UserProfile'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "web/static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

django_heroku.settings(locals())

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#ipinfo
IPINFO_TOKEN = '06f4652bdf5283'
IPINFO_SETTINGS = {
  'cache_options': {
      'ttl':30,
      'maxsize': 128
  },
#   'countries_file': 'custom_countries.json',
#   'cache': my_fancy_custom_cache_object
}
IPINFO_FILTER = lambda request: request.scheme == 'http'
IPINFO_IP_SELECTOR = DefaultIPSelector()
