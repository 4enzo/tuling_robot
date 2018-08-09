# -*- coding: utf-8 -*-
'''
Created on 2018-08-08

@author: Enzo
'''

import itchat

import tuling

'''直接调用tuling.py中的get_answer函数，调试时比较方便'''

# 捕获收到的消息，并定义回复的内容（通过图灵回复）
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return tuling.get_answer(msg['Text'])


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
