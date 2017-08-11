#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import traceback
from json import dumps

from bson import ObjectId
from tornado.web import HTTPError, RequestHandler

from common.BaseHandler import BaseRequest
from config import CONFIG
from handler.api import errors
from util.crypt import md5_data
from util.token import token_manager


class BaseApiRequest(BaseRequest):
    def data_received(self, chunk):
        pass

    def __init__(self, application, request, **kwargs):
        RequestHandler.__init__(self, application, request, **kwargs)
        self.set_header('Content-Type', 'text/json')

        if self.settings['allow_remote_access']:
            self.access_control_allow()

    def access_control_allow(self):
        # 允许 JS 跨域调用
        self.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Depth, User-Agent, X-File-Size, "
                                                        "X-Requested-With, X-Requested-By, If-Modified-Since, "
                                                        "X-File-Name, Cache-Control, Token")
        self.set_header('Access-Control-Allow-Origin', '*')

    def get(self, *args, **kwargs):
        print ('---------->>>>  get')
        raise HTTPError(**errors.status_0)

    def post(self, *args, **kwargs):
        raise HTTPError(**errors.status_0)

    def put(self, *args, **kwargs):
        raise HTTPError(**errors.status_0)

    def delete(self, *args, **kwargs):
        raise HTTPError(**errors.status_0)

    def options(self, *args, **kwargs):
        if self.settings['allow_remote_access']:
            self.write("")

    def write_error(self, status_code, **kwargs):
        self._status_code = 200

        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            lines = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                lines.append(line)

            self.write_json(dict(traceback=''.join(lines)), status_code, self._reason)

        else:
            self.write_json(None, status_code, kwargs['reason'])

    def write_json(self, data, status_code=200, msg="success"):

        result = {
            'code': status_code,
            'msg': msg,
            'data': data
        }
        self.finish(dumps(result))

    def is_running(self):
        return CONFIG.WEBSITE['IS_RUNNING']

    def is_logined(self):
        if 'Token' in self.request.headers:
            token = self.request.headers['Token']
            logined, uid = token_manager.validate_token(token)

            if logined:
                # 已经登陆
                return uid

        # 尚未登陆
        raise HTTPError(**errors.status_2)

    def upload_file_from_request(self, name, key):
        if name in self.request.files:
            fileinfo = self.request.files[name][0]
            fname = fileinfo['filename']
            body = fileinfo['body']

            extn = os.path.splitext(fname)[1]
            cname = md5_data(body) + extn

            # q = Auth(config.QINIU_AK, config.QINIU_SK)
            # key += cname
            # token = q.upload_token(config.QINIU_BUCKET_NAME)
            # ret, info = put_data(token, key, body)
            #
            # if info.status_code == 200:
            #     return config.QINIU_HOST + key
            # else:
            #     # 上传失败
            #     raise HTTPError(**errors.status_24)

        # 找不到上传文件
        raise HTTPError(**errors.status_25)

    @staticmethod
    def vaildate_id(_id):
        if _id is None or not ObjectId.is_valid(_id):
            raise HTTPError(**errors.status_3)

    @staticmethod
    def check_none(resource):
        if resource is None:
            raise HTTPError(**errors.status_22)
