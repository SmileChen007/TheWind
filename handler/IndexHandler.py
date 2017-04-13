#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.web
from tornado import gen

from common.BaseHandler import BaseRequest


class MainHandler(BaseRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        self.write("hello world !")
