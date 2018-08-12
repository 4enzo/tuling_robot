# -*- coding: utf-8 -*-
'''
Created on 2018-08-07

@author: Enzo
'''

import json
import os
import collections

import itchat
import pyecharts

def get_friends_list():
    '''获取好友主要信息'''
    friends = itchat.get_friends(update=True)[1:]
    # print(friends)
    friends_list = []
    for friend in friends:
        item = {}
        item['NickName'] = friend['NickName']
        item['RemarkName'] = friend['RemarkName']
        item['HeadImgUrl'] = friend['HeadImgUrl']
        item['Sex'] = friend['Sex']
        item['Province'] = friend['Province']
        item['City'] = friend['City']
        item['Signature'] = friend['Signature']
        item['UserName'] = friend['UserName']
        friends_list.append(item)
    return friends_list

def save_friends_data(friends_list):
    ''' json及pickle都可以实现数据的序列化/反序列化，json可用于多种语言的数据传输'''
    data_file = './friends.txt'
    with open(data_file,'w') as f:
        f.write(json.dumps(friends_list))

def load_friends_data():
    '''从已保存的文件中加载好友信息 #调试时方便#'''
    data_file = './friends.txt'
    try:
        with open(data_file,'r') as f:
            return json.loads(f.read())
    except Exception as e:
        print('Error:%s'%e)

def get_friends_num(friends_list):
    '''获取好友数'''
    print('一共有%d个微信好友'%len(friends_list))
    return len(friends_list)

def get_city(friends_list):
    '''获取省份/城市'''
    provice = set()
    city = set()
    for item in friends_list:
        provice.add(item['Province'])
        city.add(item['City'])
    print('来自%d个省份的%d个城市'%(len(provice),len(city)))
    print('\n其中省份是：%s\n城市为：%s'%(provice,city))


def dict2list(dict_data):
    key_list = []
    value_list = []
    for key in dict_data:
        key_list.append(key)
        value_list.append(dict_data[key])
    return key_list,value_list

def analysis_gender(friends_list):
    '''获取好友性别数：未标注/男性/女性'''
    num_unknown = 0   # 0 未标注性别
    num_male = 0   # 1 男性
    num_female = 0   # 2 女性
    for item in friends_list:
        if item['Sex'] == 0:
            num_unknown += 1
        if item['Sex'] == 1:
            num_male += 1
        if item['Sex'] == 2:
            num_female += 1
    # print('未标注：%d人\n男性：%d人\n女性：%d人'%(num_unknown,num_male,num_female))
    # 返回性别键值对，方便后面dict2list处理后进行作图分析
    # 直接返回性别及对应人数的列表
    gender_dict = {'男性':num_male,'女性':num_female,'未标注':num_unknown}
    return dict2list(gender_dict)

def analysis_province(friends_list):
    '''获取省份信息 省份:num'''
    province_list = []
    for item in friends_list:
        province_list.append(item['Province'])
    provice_dict = collections.Counter(province_list)

    return dict2list(provice_dict)

def analysis_nickname(friends_list):
    '''处理好友名称，生成词云'''
    # 方法与analysis_province类似，从friends_list中获取名称:数量键值对，再有dict2list获取名称list,数量list
    nickname_list = []
    for item in friends_list:
        nickname_list.append(item['NickName'])
    nickname_dict = collections.Counter(nickname_list)

    return dict2list(nickname_dict)

def gender_pie(title_name,gender_name,gender_num):
    total_num = 0
    for i in gender_num:
        total_num += i
    subtitle_name = '共有%d个好友'%(total_num)
    pie = pyecharts.Pie(title=title_name,subtitle=subtitle_name)
    pie.add('',gender_name,gender_num,is_label_show=True)
    pie_file_name = './' + title_name + '.html'
    try:
        pie.render(path=pie_file_name)
        print('%s已保存至%s'%(title_name,pie_file_name))
    except Exception as e:
        pass

def province_map(map_title,province_name,province_num):
    map_subtitle = '仅统计位于中国省份的信息'
    map = pyecharts.Map(title=map_title,subtitle=map_subtitle,width=1600,height=800)
    # print(map.width)
    map.add('',province_name,province_num,maptype='china',is_visualmap=True)
    map_file_name = './' + map_title + '.html'
    try:
        map.render(path=map_file_name)
        print('%s已保存至%s'%(map_title,map_file_name))
    except Exception as e:
        pass

def nickname_wc(wc_title,nickname_name,nickname_num):
    '''微信好友名生成词云'''
    # 不对好友名称进行分词，直接生成词云
    wc = pyecharts.WordCloud(title=wc_title,width=1200,height=800)
    wc.add('',nickname_name,nickname_num,shape='circle')
    wc_file_name = './' + wc_title + '.html'
    try:
        wc.render(path=wc_file_name)
        print('%s已保存至%s'%(wc_title,wc_file_name))
    except Exception as e:
        pass

def save_heads_img(friends_list):
    '''保存头像数据'''
    images_dir = './images/'
    # 判断保存头像的文件夹是否存在，如果不存在则创建
    full_path = os.getcwd()+images_dir
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    else:
        pass
    print('正在保存好友头像，保存路径为:%s 请稍等'%(os.getcwd()+images_dir))
    num = 0
    for friend in friends_list:
        image = itchat.get_head_img(userName=friend['UserName'])
        # print(image)
        # 单纯保存为RemarkName.jpg的话，未备注的好友头像文件为 .jpg，有文件覆盖情况
        # 另若头像名中包含特殊字符，保存成文件时又会报错，暂时无解？
        # 另若好友备注名相同的话也会存在文件覆盖情况----文件保存时先判断文件是否存在，如果存在文件名为xxx02.jpg?暂时不实现
        # 先按纯数字命名保存头像文件。。。
        image_name = str(num)+'.jpg'
        num += 1
        # if friend['RemarkName'] == '':
        #     image_name = friend['NickName']+'.jpg'
        # else:
        #     image_name = friend['RemarkName']+'.jpg'
        try:
            with open(images_dir+image_name,'wb') as f:
                f.write(image)
        except Exception as e:
            pass
    print('头像已保存')


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    friends_list = get_friends_list()
    save_friends_data(friends_list)
    get_friends_num(friends_list)
    get_city(friends_list)

    # 好友性别及省份可视化
    gender_name,gender_num = analysis_gender(friends_list)
    gender_pie('微信好友性别比例图', gender_name, gender_num)

    province_name, province_num = analysis_province(friends_list)
    province_map('微信好友省份分布图',province_name, province_num)

    # 微信好友名生成词云
    nickname_name, nickname_num = analysis_nickname(friends_list)
    nickname_wc('微信好友名词云',nickname_name, nickname_num)