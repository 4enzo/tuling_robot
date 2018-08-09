# -*- coding: utf-8 -*-
'''
Created on 2018-08-08

@author: Enzo
'''

import itchat

import tuling

'''直接调用tuling.py中的get_answer函数，调试时比较方便'''

reply_flag = True
# 捕获收到的消息，并定义回复的内容（通过图灵回复）
'''加了一个关键字暂停/继续机器人回复功能，感觉实现方法有些不太好，还存在一个bug，改天再改吧'''
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    global reply_flag
    if msg['Text'] == '二蛋暂停':
        reply_flag = False
    elif msg['Text'] == '二蛋继续':
        reply_flag = True
    if reply_flag and msg['Text'] != '二蛋继续':
        return tuling.get_answer(msg['Text'])
    else:
        pass

reply_group_flag = True
@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def text_reply(msg):
    global reply_group_flag
    if msg['Text'] == '二蛋暂停群聊':
        reply_group_flag = False
    elif msg['Text'] == '二蛋继续群聊':
        reply_group_flag = True

    if reply_group_flag and msg['Text'] != '二蛋继续群聊' and msg['User']['NickName'] == '懵懵tengteng':
        return tuling.get_answer(msg['Text'])
    else:
        pass



if __name__ == '__main__':
    itchat.auto_login(hotReload=True,enableCmdQR=2)
    itchat.run()
