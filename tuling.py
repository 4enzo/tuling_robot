# -*- coding: utf-8 -*-
'''
Created on 2018-08-08

@author: Enzo
'''

import requests
import json

# 直接调用接口与图灵机器人对话

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
    reply_code = s['intent']['code']

    if reply_code == 10003:
        '''code = 10003 新闻类标识码'''
        news = s['results'][1]['values']['news']
        news_str = s['results'][0]['values']['text'] + '：\n'
        for list in news:
            # print(list)
            news_str = news_str + list['name'] +'\n来源：' + list['info'] +'\n链接：' + list['detailurl'] + '\n\n'
        return news_str
    elif reply_code == 10014:
        '''code = 10014 链接类标识码'''
        pic = s['results'][1]['values']['text'] + '\n' + s['results'][0]['values']['url']
        return pic
    elif reply_code == 10015:
        '''code = 10015 菜谱类标识码'''
        cook = s['results'][1]['values']['news']
        cook_str = s['results'][0]['values']['text'] + '：\n'
        for list in cook:
            cook_str = cook_str + list['name'] +'\n' + list['info'] +'\n链接：' + list['detailurl'] + '\n\n'
        return cook_str
    else:
        '''很多code值的处理结果都可以用如下方法，暂时这样用着？'''
        answer = s['results'][0]['values']['text']
        return answer

if __name__ == '__main__':
    while True:
        que = input("我:")
        print('图灵机器人:' + get_answer(que))