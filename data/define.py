#!/usr/bin/env python
# coding:utf-8

book_code = [
    dict(book_code=0, book_status='连载', extra=''),
    dict(book_code=1, book_status='完结', extra=''),
    dict(book_code=2, book_status='冻结', extra='')]

categories_local = ['xuanhuan', 'dushi', 'xianxia', 'lishi', 'wangyou', 'kehuan', 'kongbu', 'yanqing', 'wenxue',
                    'other', 'finish']
book_category = [
    dict(novel_category=categories_local[0], category_include='xuanhuan'),
    dict(novel_category=categories_local[1], category_include='dushi'),
    dict(novel_category=categories_local[2], category_include='xianxia'),
    dict(novel_category=categories_local[3], category_include='lishi'),
    dict(novel_category=categories_local[4], category_include='wangyou'),
    dict(novel_category=categories_local[5], category_include='kehuan'),
    dict(novel_category=categories_local[6], category_include='kongbu'),
    dict(novel_category=categories_local[7], category_include='yanqing'),
    dict(novel_category=categories_local[8], category_include='wenxue'),
    dict(novel_category=categories_local[9], category_include='other'),
    dict(novel_category=categories_local[10], category_include='finish')]
