#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import tornado.web
from bson import ObjectId

from tornado import gen
from data.db_doc import *
from handler.api import errors
from handler.api.BaseApiHandler import BaseApiRequest
from util.time import create_time


class RegisterHandler(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        mobile = self.get_argument('mobile', None)
        pwd = self.get_argument('pwd', None)
        error = errors.status_10001
        if mobile is None:
            error['reason'] = 'mobile is null !'
            self.write_error(**error)
            return
        if pwd is None:
            error['reason'] = 'pwd is null !'
            self.write_error(**error)
            return
        users = yield User.objects.filter(mobile=mobile).find_all()
        if len(users) != 0:
            # 手机号码已经被注册
            self.write_error(**errors.status_21)
            return

        user = User(mobile=mobile, password=pwd, nickname='test', create_time=create_time())
        yield user.save()

        user = user.to_dict()
        self.write_json(user)


class GetAllUsers(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        users = yield User.objects.find_all()
        if len(users) != 0:
            self.write_json([usr.to_dict() for usr in users])
        else:
            self.write_error(**errors.status_10003)


class GetAllNovels(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        pass
        # novels = yield NovelInfo.objects.find_all()
        # if len(novels) != 0:
        #     self.write_json([novel.to_dict() for novel in novels])
        # else:
        #     self.write_error(**errors.status_10004)


class InsertNovel(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        book = dict()
        book['novel_author'] = self.get_argument('novel_author', None)
        book['novel_name'] = self.get_argument('novel_name', None)
        book['novel_img_url'] = self.get_argument('novel_img_url', None)
        book['novel_category'] = self.get_argument('novel_category', None)
        book['novel_details'] = self.get_argument('novel_details', None)
        book['novel_down_url'] = self.get_argument('novel_down_url', None)
        error = errors.status_10001
        if book['novel_category'] is not None:
            category = yield BookCategory.object.find_all()
            if len(category) != 0:
                pass
            else:
                self.write_error(**errors.status_10005)
        else:
            error['reason'] = 'novel_category is null !'
            self.write_error(**error)
            # info = NovelInfo()
            # info.novel_author = self.get_argument('novel_author', None)
            # info.novel_name = self.get_argument('novel_name', None)
            # info.novel_img_url = self.get_argument('novel_img_url', None)
            # info.novel_category = self.get_argument('novel_category', None)
            # info.novel_details = self.get_argument('novel_details', None)
            # info.novel_down_url = self.get_argument('novel_down_url', None)
            # info.create_time = create_time()
            # info.novel_download_count = 0
            #
            # if info.novel_author is None:
            #     error['reason'] = 'novel_author is null !'
            #     self.write_error(**error)
            #     return
            # if info.novel_name is None:
            #     error['reason'] = 'name is null !'
            #     self.write_error(**error)
            #     return
            # if info.novel_img_url is None:
            #     error['reason'] = 'novel_img_url is null !'
            #     self.write_error(**error)
            #     return
            # if info.novel_category is None:
            #     error['reason'] = 'novel_category is null !'
            #     self.write_error(**error)
            #     return
            # if info.novel_details is None:
            #     error['reason'] = 'novel_details is null !'
            #     self.write_error(**error)
            #     return
            # if info.novel_down_url is None:
            #     error['reason'] = 'novel_down_url is null !'
            #     self.write_error(**error)
            #     return
            # yield info.save()
            # info = info.to_dict()
            # self.write_json(info)


class UpdateNovel(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        pass
        # _id = ObjectId(self.get_argument('id', None))
        # novel_author = self.get_argument('novel_author', None)
        # novel_name = self.get_argument('novel_name', None)
        # novel_img_url = self.get_argument('novel_img_url', None)
        # novel_category = self.get_argument('novel_category', None)
        # novel_details = self.get_argument('novel_details', None)
        # novel_down_url = self.get_argument('novel_down_url', None)
        # error = dict(status_code=10001)
        # if _id is None:
        #     error['reason'] = 'id is null !'
        #     self.write_error(**error)
        #     return
        # novel = yield NovelInfo.objects.get(_id)
        # print (novel.to_dict())
        # if novel is not None:
        #     novel.update_time = create_time()
        #     if novel_author is not None:
        #         novel.novel_author = novel_author
        #     if novel_name is not None:
        #         novel.novel_name = novel_name
        #     if novel_img_url is not None:
        #         novel.novel_img_url = novel_img_url
        #     if novel_category is not None:
        #         novel.novel_category = novel_category
        #     if novel_details is not None:
        #         novel.novel_details = novel_details
        #     if novel_down_url is not None:
        #         novel.novel_down_url = novel_down_url
        #     yield novel.save()
        #     self.write_json(novel.to_dict())
        # else:
        #     self.write_error(**errors.status_10002)


class GetSmsCode(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, *args, **kwargs):
        # recepient = Textbelt.Recipient("15755397089")
        # message = "1234"
        # result=recepient.send(message)
        import requests
        result = requests.post('https://textbelt.com/text', {
            'phone': '+8615755397089',
            'message': 'Hello world',
            'key': '4497a16d43b576a902d4f8211fb1651f808b4a87MMbLurJwhLiLqDKl9PbjuB0uX',
        })
        print (result.text)
        pass
