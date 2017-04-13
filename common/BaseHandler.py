#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web


class BaseRequest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass
