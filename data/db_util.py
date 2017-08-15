#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
from data.db_doc import *
from data import define
from tornado import gen

create_db_tasks = 14
now_create_task = 0


@gen.coroutine
def create_db():
    print('create user ...')
    User().save(callback=handler_result)
    print('create db_xuanhuan ...')
    BookXH().save(callback=handler_result)
    print('create db_dushi ...')
    BookDS().save(callback=handler_result)
    print('create db_xianxia ...')
    BookXX().save(callback=handler_result)
    print('create db_lishi ...')
    BookLS().save(callback=handler_result)
    print('create db_wangyou ...')
    BookWY().save(callback=handler_result)
    print('create db_kehuan')
    BookKH().save(callback=handler_result)
    print('create db_kongbu')
    BookKB().save(callback=handler_result)
    print('create db_yanqing')
    BookYQ().save(callback=handler_result)
    print('create db_wenxue')
    BookWX().save(callback=handler_result)
    print('create db_other')
    BookOther().save(callback=handler_result)
    print('create db_finish')
    BookFinish().save(callback=handler_result)
    print('create db_status')
    BookStatus().save(callback=handler_result)
    print('create db_category')
    BookCategory().save(callback=handler_result)
    print('create db_recommend')
    Recommend().save(callback=handler_result)


write_db_tasks = len(define.book_code) + len(define.book_category)
now_write_task = 0


@gen.coroutine
def write_db():
    print('start write db data ...')
    for book_code in define.book_code:
        BookStatus(**book_code).save(callback=handler_write_db)
    for category in define.book_category:
        BookCategory(**category).save(callback=handler_write_db)


@gen.coroutine
def init_db():
    print('start create db ...')
    yield create_db()


def handler_result(info):
    global now_create_task
    now_create_task = now_create_task + 1
    now_percent = int((now_create_task * 1.0 / create_db_tasks) * 100)
    print(info.to_dict())
    print('now percent : ' + (str(now_percent)) + '%')
    if now_percent == 100:
        print('create db finish !')
        write_db()


def handler_write_db(msg):
    global now_write_task
    now_write_task = now_write_task + 1
    now_percent = int((now_write_task * 1.0 / write_db_tasks) * 100)
    print(msg.to_dict())
    print('now percent : ' + (str(now_percent)) + '%')
    if now_percent == 100:
        print('write db finish !')
