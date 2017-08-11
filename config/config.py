# coding:utf-8
import os


class Config:
    """
       Basic config for TheWind
    """
    WEBSITE = dict(
        IS_RUNNING=True,
        TOKEN=''
    )

    AES_KEY = 'your 32 byte aes key'
    TOKEN_TIMEOUT = 60 * 60 * 24 * 30
