#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import tornado.web

from url import urls

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = dict(
            template_path=TEMPLATE_PATH,
            static_path=STATIC_PATH,
            debug=True,
            allow_remote_access=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
