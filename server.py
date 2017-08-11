#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

os.environ['MODE'] = 'PRO'  # set pro or dev
from application import Application
from data.init_db import connect_db
from config import LOGGER

define("port", group='Webserver', type=int, default=8888, help="Run on the given port")


def main():
    io_loop = tornado.ioloop.IOLoop.instance()
    connect_db(io_loop, False)
    app = Application()

    app.listen(options.port)
    LOGGER.info('Server is running at http://127.0.0.1:%s' % options.port)
    io_loop.start()


if __name__ == "__main__":
    LOGGER.info('mode ---> ' + os.environ['MODE'])
    main()
