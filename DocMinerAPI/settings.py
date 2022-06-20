#-*- coding: utf-8 -*-
'''
*******************************************************************************
 * All rights reserved.
 * -----------------------------------------------------------------------------
 * @fileName : settings.py
 * @author   : "Ko Sun Ho"
 * @date     : 2022. 06. 14.
 * @comment  : DocMinerAPI 장고 프레임워크 세팅 파일
 *
 * @revision history
 * date            author         comment
 * ----------      ---------      ----------------------------------------------
 * 2022. 06. 14.  Ko Sun Ho    최초 작성
 *******************************************************************************
'''

import os
from pathlib import Path

import os
import time

def now_time():
    now = time.localtime()
    s = "%04d%02d%02d_%02dh" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour)
    return s

################# 경로 관리 ##########################

# 기본 경로
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_file_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# APP 경로
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"

################# APP 관리 ##########################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api_docminer',
    'api_database',
    'templates',
]
################# TEMPLATES 관리 ##########################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APP_DIR, "templates"), ],
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

################# STATIC 관리 ##########################
# Static files (CSS, JavaScript, Images)
# STATIC 경로
STATIC_URL = '/static/'
STATICFILES_DIRS = [ APP_DIR + 'static' ]

WSGI_APPLICATION = 'DocMinerAPI.wsgi.application'

################# DATABASE 관리 ##########################

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SQLITE_CONFIG_DEV = {
    'table': {
        'test': 'DEV_TEST'
    }
}

# HDHS
HDFS_CONFIG_PROD = {
    "con":
        {
            'client': 'http://hmng1:17777',
            'write_bas_path': '/api_test/'
        },
}
################# DJANGO 기본 세팅 관리 ##########################

ROOT_URLCONF = 'DocMinerAPI.urls'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g2ilp23ya-4p2$3_d0$lcxnx0qc&3@_v=pkfy%+!na7emt3@14'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # ,'rest_framework.permissions.IsAuthenticated',
    ]
}

################# logging 관리 ##########################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s|%(asctime)s|%(module)s|%(process)d|%(thread)d|%(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s ::: %(message)s',
            'datefmt': '%Y-%b-%d %H:%M:%S'
        },
    },

    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': str(BASE_DIR) + '/logs/debug_' + now_time() + '.log',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10,
            'formatter': 'verbose'
        },

        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },

    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']
        },
}
