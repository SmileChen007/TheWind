# coding:utf-8

import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# MongoDB Config
DB_HOST = 'www.coreice.org'
DB_PORT = 27017
DB_NAME = 'wind'
DB_USER = ''
DB_PWD = ''

# Redis Config
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

# You can generate the key by the following website:
# https://asecuritysite.com/encryption/keygen
AES_KEY = 'your 32 byte aes key'
TOKEN_TIMEOUT = 60 * 60 * 24 * 30

