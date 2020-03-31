# -*- coding: utf-8 -*-

#import yagmail
import keyring
from imbox import Imbox

#authcode = input("Authorization Code: ")
#yagmail.register('jonsenma@qq.com',authcode)
mail_pass = keyring.get_password('yagmail','XXX@qq.com')
with Imbox('imap.qq.com','jonsenma@qq.com',mail_pass,ssl=True) as imbox:
    # imap服务器地址，邮箱，密码，是否支持ssl
    print('正在连接QQ邮箱...')
    unread_mails = imbox.messages(unread=True)
    # 读取收件箱所有信息
    for uid, messages in unread_mails:
        title = messages.subject
        sent_from = messages.sent_from
        print(f'收到来自{sent_from}的邮件\n邮件主题为：{title}\n')
        #imbox.mark_seen(uid)
        #print('已标记为已读')
