#!/usr/bin/env python
# coding:utf-8
from config import CONFIG
import redis
import logging


def init_redis():
    logging.info('----------------->>>  init redis')
    try:
        r = redis.Redis(
            connection_pool=
            redis.ConnectionPool(
                host=CONFIG.REDIS_DICT['REDIS_ENDPOINT'],
                port=CONFIG.REDIS_DICT['REDIS_PORT'],
                db=CONFIG.REDIS_DICT['SESSION_DB'],
            )
        )
        logging.info('----------------->>>  init redis success ！')
        return r
    except Exception as e:
        logging.WARNING('----------------->>>  init redis failed ！')
        logging.WARNING(e.message)


Redis = init_redis()
