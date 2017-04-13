#!/usr/bin/env python
# -*- coding:utf-8 -*-
from data.db_doc import *
from data.define import categories_local
from handler.api import errors


def get_category(category, categories=None):
    '''
    返回对应分类的实体
    未完成
    :param category: 目标分类
    :param categories:  分类集合
    :return:  分类实体
    '''
    try:
        book = categories_local.index(category)
        if book is 0: return 1, BookXH()
        if book is 1: return 1, BookDS()
        if book is 2: return 1, BookXX()
        if book is 3: return 1, BookLS()
        if book is 4: return 1, BookWY()
        if book is 5: return 1, BookKH()
        if book is 6: return 1, BookKB()
        if book is 7: return 1, BookYQ()
        if book is 8: return 1, BookWX()
        if book is 9: return 1, BookOther()
        if book is 10: return 1, BookFinish()
    except:
        return 0, errors.status_10006
