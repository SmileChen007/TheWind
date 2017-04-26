# coding:utf-8
from importlib import import_module

from tornado.options import options

from common.HttpErrorHandler import HttpErrorHandler
from handler.IndexHandler import MainHandler
from handler.api.api_urls import api_urls


def include(module=None):
    '''
    路由分层合并
    :param module: 
    :return: 
    '''
    res = module
    urls = getattr(res, 'urls', res)
    return urls


def url_wrapper(urls):
    wrapper_list = []
    for url in urls:
        path, handles = url
        if isinstance(handles, (tuple, list)):
            for handle in handles:
                pattern, handle_class = handle
                wrap = ('{0}{1}'.format(path, pattern), handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path, handles))
    return wrapper_list


urls = url_wrapper([
    (r'/', MainHandler),
    (r'/index', MainHandler),
    (r'/home', MainHandler),
    (r'/api', include(api_urls)),
    (r'.*', HttpErrorHandler),
])
