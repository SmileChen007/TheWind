#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import tornado.web
from bson import ObjectId
from motorengine import Q

from tornado import gen
from handler.api.BaseApiHandler import BaseApiRequest
from util.Email import new_user_body, send
from util.time import create_time
from func_doc import *


class RegisterHandler(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            data = self.get_argument("data", None)
            data = json.loads(data)
            email = data['email']
            pwd = data['pwd']
            if email is None:
                self.write_error(**errors.status_10011)
                return
            if pwd is None:
                self.write_error(**errors.status_10012)
                return
            users = yield User.objects.filter(email=email).find_all()
            if len(users) != 0:
                # 手机号码已经被注册
                self.write_error(**errors.status_10013)
                return
            user = User(email=email, password=pwd, nickname='未设置昵称', create_time=create_time())
            yield user.save()
            user = user.to_dict()
            self.write_json(json.dumps(user))
            send(new_user_body(str(email)), subject="注册成功", msg_type='html', receiver=str(email), mail_to='新用户')
        except Exception as e:
            self.write_error(**errors.status_10010)


class LoginHandler(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            data = self.get_argument("data", None)
            data = json.loads(data)
            email = data['email']
            pwd = data['pwd']
            if email is None:
                self.write_error(**errors.status_10011)
                return
            if pwd is None:
                self.write_error(**errors.status_10012)
                return
            users = yield User.objects.filter(email=email).find_all()
            if len(users) == 0:
                # 手机号码未被注册
                self.write_error(**errors.status_10014)
            else:
                user = users[0]
                if user.password == pwd:
                    self.write_json(json.dumps(user.to_dict()))
                else:
                    self.write_error(**errors.status_23)
        except:
            self.write_error(**errors.status_10010)


class ExtraHandler(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            data = self.get_argument("data", None)
            data = json.loads(data)
            email = data['email']
            push_id = data['push_id']
            if email is None:
                self.write_error(**errors.status_10011)
                return
            if push_id is None:
                self.write_error(**errors.status_10012)
                return
            users = yield User.objects.filter(email=email).find_all()
            if len(users) == 0:
                # 手机号码未被注册
                self.write_error(**errors.status_10014)
            else:
                user = users[0]
                user.push_id = push_id
                yield user.save()
        except:
            self.write_error(**errors.status_10010)


class GetAllUsers(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            users = yield User.objects.find_all()
            if len(users) != 0:
                self.write_json([usr.to_dict() for usr in users])
            else:
                self.write_error(**errors.status_10003)
        except:
            self.write_error(**errors.status_10010)


class GetAllBooks(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            novel_category = self.get_argument('novel_category', None)
            error = errors.status_10001
            if novel_category is not None:
                status, msg = get_category(novel_category)
                if status:
                    novels = yield msg.objects.find_all()
                    if len(novels) != 0:
                        self.write_json([novel.to_dict() for novel in novels])
                    else:
                        self.write_error(**errors.status_10004)
                else:
                    self.write_error(**msg)
            else:
                error['reason'] = '请填写分类!'
                self.write_error(**error)
        except:
            self.write_error(**errors.status_10010)


class InsertBook(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        novel_category = self.get_argument('novel_category', None)
        error = errors.status_10001
        if novel_category is not None:
            status, info = get_category(novel_category)
            if status:
                info.novel_name = self.get_argument('novel_name', None)
                info.novel_img_url = self.get_argument('novel_img_url', None)
                info.novel_author = self.get_argument('novel_author', None)
                info.novel_details = self.get_argument('novel_details', None)
                info.novel_down_url = self.get_argument('novel_down_url', None)
                info.novel_size = self.get_argument('novel_size', '0.0')
                info.novel_catalog_url = self.get_argument('novel_catalog_url', None)
                info.novel_origin = self.get_argument('novel_origin', None)
                info.novel_grade = self.get_argument('novel_grade', 0)
                info.novel_status_code = self.get_argument('novel_status_code', None)
                info.create_time = create_time()
                info.novel_download_count = 0

                if info.novel_author is None:
                    error['reason'] = '请填写作者!'
                    self.write_error(**error)
                    return
                if info.novel_name is None:
                    error['reason'] = '请填写书籍名称 !'
                    self.write_error(**error)
                    return
                if info.novel_img_url is None:
                    error['reason'] = '请填写图片链接!'
                    self.write_error(**error)
                    return
                if info.novel_details is None:
                    error['reason'] = '请填写书籍简介!'
                    self.write_error(**error)
                    return
                if info.novel_down_url is None:
                    error['reason'] = '请填写下载链接!'
                    self.write_error(**error)
                    return
                try:
                    yield info.save()
                    info = info.to_dict()
                    self.write_json(info)
                except:
                    self.write_error(**info)

            else:
                self.write_error(**info)
        else:
            error['reason'] = '请填写分类!'
            self.write_error(**error)


class UpdateBook(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            _id = ObjectId(self.get_argument('id', None))
            novel_category = self.get_argument('novel_category', None)
            novel_name = self.get_argument('novel_name', None)
            novel_img_url = self.get_argument('novel_img_url', None)
            novel_author = self.get_argument('novel_author', None)
            novel_details = self.get_argument('novel_details', None)
            novel_down_url = self.get_argument('novel_down_url', None)
            novel_size = self.get_argument('novel_size', None)
            novel_catalog_url = self.get_argument('novel_catalog_url', None)
            novel_origin = self.get_argument('novel_origin', None)
            novel_grade = self.get_argument('novel_grade', None)
            novel_status_code = self.get_argument('novel_status_code', None)
            error = errors.status_10001
            if _id is None:
                error['reason'] = 'id为空 !'
                self.write_error(**error)
                return
            if novel_category is not None:
                status, info = get_category(novel_category)
                if status:
                    novel = yield info.objects.get(_id)
                    if novel is not None:
                        novel.update_time = create_time()
                        if novel_author is not None:
                            novel.novel_author = novel_author
                        if novel_name is not None:
                            novel.novel_name = novel_name
                        if novel_img_url is not None:
                            novel.novel_img_url = novel_img_url
                        if novel_category is not None:
                            novel.novel_category = novel_category
                        if novel_details is not None:
                            novel.novel_details = novel_details
                        if novel_down_url is not None:
                            novel.novel_down_url = novel_down_url
                        if novel_size is not None:
                            novel.novel_size = novel_size
                        if novel_catalog_url is not None:
                            novel.novel_catalog_url = novel_catalog_url
                        if novel_origin is not None:
                            novel.novel_origin = novel_origin
                        if novel_grade is not None:
                            novel.novel_grade = novel_grade
                        if novel_status_code is not None:
                            novel.novel_status_code = novel_status_code
                        yield novel.save()
                        self.write_json(novel.to_dict())
                    else:
                        self.write_error(**errors.status_10002)
                else:
                    self.write_error(**info)
            else:
                error['reason'] = '请填写分类!'
                self.write_error(**error)
        except:
            self.write_error(**errors.status_10010)


class QueryBook(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            novel_category = self.get_argument('novel_category', 'all')
            book_info = self.get_argument('book_info', None)
            limit_size = self.get_argument('limit_size', 5)
            if book_info is None:
                self.write_error(**errors.status_10001)
            else:
                query = Q(novel_name__icontains=book_info) | Q(novel_author__icontains=book_info)
                if novel_category == 'all':
                    books = []
                    for book_type in get_categories_local():
                        status, db_or_error = get_category(book_type)
                        if status:
                            books_add = yield db_or_error.objects.filter(query).limit(limit_size).find_all()
                            if len(books_add) != 0:
                                books.extend(books_add)
                    if len(books) != 0:
                        for book in books:
                            if 'ice' in book.novel_down_url and book.novel_category not in book.novel_down_url:
                                at = book.novel_down_url.rfind('/')
                                book.novel_down_url = book.novel_down_url[
                                                      :at] + '/' + book.novel_category + book.novel_down_url[at:]
                        self.write_json([novel.to_dict() for novel in books])
                    else:
                        self.write_error(**errors.status_10009)
                else:
                    status, db_or_error = get_category(novel_category)
                    if status:
                        books = yield db_or_error.objects.filter(query).limit(limit_size).find_all()
                        print (books)
                        if len(books) != 0:
                            self.write_json([novel.to_dict() for novel in books])
                        else:
                            self.write_error(**errors.status_10009)
                    else:
                        self.write_error(**db_or_error)
        except:
            self.write_error(**errors.status_10010)


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


class RecommendBookHandler(BaseApiRequest):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        page = self.get_argument('book_page', 1)

        pass
