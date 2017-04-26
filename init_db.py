#!/usr/bin/env python
# coding:utf-8

from motorengine import connect

import config
from data.db_util import init_db

global conn


def connect_db(io_loop, is_init_db=True):
    print ('-----> connecting db')
    global conn
    conn = connect(config.DB_NAME, host=config.DB_HOST, port=config.DB_PORT, io_loop=io_loop)
    print ('-----> connecting db finish')
    if is_init_db:
        io_loop.add_timeout(1, init_db)
        print ('-----> init db')


def get_conn():
    global conn
    return conn