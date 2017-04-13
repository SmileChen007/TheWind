#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options, parse_command_line

from application import Application
from init_db import connect_db

define("port", group='Webserver', type=int, default=8888, help="Run on the given port")


def main():
    options.logging = None
    parse_command_line()

    io_loop = tornado.ioloop.IOLoop.instance()
    connect_db(io_loop, True)
    app = Application()

    app.listen(options.port)
    print('Server is running at http://127.0.0.1:%s' % options.port)
    io_loop.start()

if __name__ == "__main__":
    main()