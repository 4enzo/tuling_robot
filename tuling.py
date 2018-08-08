# -*- coding: utf-8 -*-
'''
Created on 2018-08-08

@author: Enzo
'''

import requests
import json

# 去掉微信，直接调用接口与图灵机器人对话

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
            'userId': 'python'
        }
    }

    r = requests.post(api_url, data=json.dumps(data))
    s = json.loads(r.text)
    answer = s['results'][0]['values']['text']
    return answer

if __name__ == '__main__':
    while True:
        que = input("我:")
        print('图灵机器人:' + get_answer(que))