#!/usr/bin/env python
# coding:utf-8

from motorengine import connect
from config import CONFIG, LOGGER
from data.db_util import init_db

global conn


def connect_db(io_loop, is_init_db=True):
    config = CONFIG
    LOGGER.info('-----> connecting db')
    global conn
    conn = connect(config.MONGODB['DATABASE'], host=config.MONGODB['HOST'], port=config.MONGODB['PORT'],
                   io_loop=io_loop)
    LOGGER.info('-----> connecting db finish')
    if is_init_db:
        io_loop.add_timeout(1, init_db)
        LOGGER.info('-----> init db')


def get_conn():
    global conn
    return conn
