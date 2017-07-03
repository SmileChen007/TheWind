#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 第三方 SMTP 服务  使用阿里云邮箱
mail_host = "smtp.mxhichina.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令


def body_txt():
    return ''


def body_html():
    return ''


def new_user_body(email):
    mail_msg = """
    <p>尊敬的用户：</p>
    <p>恭喜您，成功完成了Wind帐号的创建，您所创建的账号是:""" + email + """</p>"""
    return mail_msg


def send(mail_msg, subject, receiver, msg_type='plain', mail_from="Wind", mail_to="用户"):
    '''
    发送邮件
    :param mail_msg:  邮件主体内容
    :param subject:  邮件标题
    :param receiver: 收件人
    :param msg_type: 邮件主体内容 格式 as 'html' ,'plain'
    :param mail_from: 发件人名称
    :param mail_to: 收件人名称
    :return:
    '''
    ret = True
    try:
        msg = MIMEText(mail_msg, msg_type, 'utf-8')  # 邮件主体内容
        msg['From'] = formataddr([mail_from, mail_user])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([mail_to, receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = subject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP(mail_host, 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(mail_user, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(mail_user, receiver, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print("邮件发送失败")
    return ret

# 测试
# send(new_user_body('1130212665@qq.com'), subject="注册成功", msg_type='html', receiver="1130212665@qq.com", mail_to='新用户')
