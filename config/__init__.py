# coding:utf-8

import os
import logging


def load_config():
    mode = os.environ.get('MODE', 'DEV')
    logging.info('mode ---> ' + mode)
    try:
        if mode == 'PRO':
            from .pro_config import ProConfig
            return ProConfig
        elif mode == 'DEV':
            from .dev_config import DevConfig
            return DevConfig
        else:
            from .dev_config import DevConfig
            return DevConfig
    except ImportError:
        from .config import Config
        return Config


logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

handler = logging.FileHandler('wind.log')
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(logging_format))

logging.basicConfig(
    format=logging_format,
    level=logging.DEBUG
)
logging.getLogger().addHandler(handler)
LOGGER = logging.getLogger()
CONFIG = load_config()
