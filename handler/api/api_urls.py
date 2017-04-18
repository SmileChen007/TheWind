# coding:utf-8
from handler.api.api_handler.book import *

api_urls = [
    (r'/register', RegisterHandler),
    (r'/get_all_users', GetAllUsers),
    (r'/insert_book', InsertBook),
    (r'/get_books', GetAllBooks),
    (r'/update_book', UpdateBook),
    (r'/get_sms_code', GetSmsCode),
    (r'/query_book', QueryBook),
]
