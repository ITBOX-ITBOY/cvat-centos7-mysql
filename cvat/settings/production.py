# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from .base import *

DEBUG = False

INSTALLED_APPS += [
    'mod_wsgi.server',
]

NUCLIO['HOST'] = os.getenv('CVAT_NUCLIO_HOST', 'nuclio-dashboard')

for key in RQ_QUEUES:
    RQ_QUEUES[key]['HOST'] = os.getenv('CVAT_REDIS_HOST', 'cvat-redis-service')

CACHEOPS_REDIS['host'] = os.getenv('CVAT_REDIS_HOST', 'cvat-redis-service')

# Django-sendfile:
# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.xsendfile'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('CVAT_MYSQL_DATABASE', 'cvat'),
        "HOST": os.getenv('CVAT_MYSQL_HOST', 'cvat-mysql-service'),
        "USER": os.getenv('CVAT_MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('CVAT_MYSQL_ROOT_PASSWORD', '123456'),
        "PORT": os.getenv('CVAT_MYSQL_PORT', '3306')
    }
}
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_REPLACE_HTTPS_REFERER = True
