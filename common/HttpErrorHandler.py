#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common.BaseHandler import BaseRequest


class HttpErrorHandler(BaseRequest):
    def data_received(self, chunk):
        pass

    def get(self):
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('public/404.html')
        elif status_code == 500:
            self.render('public/500.html')
        else:
            self.write('error:' + str(status_code))
