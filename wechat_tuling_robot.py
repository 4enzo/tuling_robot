# -*- coding: utf-8 -*-
'''
Created on 2018-08-08

@author: Enzo
'''


import itchat
import requests
import json

def get_answer(info):
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'
    # 图灵机器人api 参考https://www.kancloud.cn/turing/web_api/522992
    # 目前脚本只支持文本即reqType=0
    # apikey 通过官网注册创建机器人获取，userId任意填写即可
    data = {
        'reqType': 0,
        'perception': {'inputText':{'text':info}},
        'userInfo': {
            'apiKey': '6997c5b25a2549cab428708d61d8514e',
            'userId': 'wechat'
        }
    }

    r = requests.post(api_url, data=json.dumps(data))
    s = json.loads(r.text)
    answer = s['results'][0]['values']['text']
    return answer

# 捕获收到的消息，并定义回复的内容（通过图灵回复）
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return get_answer(msg['Text'])


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
