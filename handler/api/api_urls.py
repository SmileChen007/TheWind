# coding:utf-8
from handler.api.api_handler.book import *

api_urls = [
    (r'/register', RegisterHandler),
    (r'/get_all_users', GetAllUsers),
    (r'/insert_book', InsertNovel),
    (r'/get_all_books', GetAllNovels),
    (r'/update_book', UpdateNovel),
    (r'/get_sms_code', GetSmsCode),
]
