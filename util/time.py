# coding:utf-8

import datetime


def create_time(format_time='%Y-%m-%d %H:%M:%S'):
    now = datetime.datetime.now()
    time = now.strftime(format_time)
    return time
