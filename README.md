# tuling_robot<br>
通过图灵机器人与微信好友交流<br>
获取微信好友信息，对性别及所在省份分析并可视化<br>

## 本项目所依赖的第三方库<br>
本项目使用python3，相关库有itchat,pyecharts <br>
* pip3 install itchat<br>
* pip3 install pyecharts<br>
地图数据的可视化：从 v0.3.2+ 起，地图已经变为扩展包，需另外安装，支持全国省份，全国城市，全国区县，全球国家等地图
* pip3 install echarts-countries-pypkg<br>
* pip3 install echarts-china-provinces-pypkg<br> 
* pip3 install echarts-china-cities-pypkg<br>
## 文件说明<br>
### wechat_tuling_robot.py<br>
主要是监测收到微信好友/群聊的文本信息，并将信息post到图灵机器人接口，将收到的信息回复给好友/群聊<br>
目前只支持文本处理文本信息<br>

### tuling.py<br>
将信息post到图灵机器人并接受机器人回复的信息<br>
分成wechat_tuling_robot.py和tuling.py两个py文件为方便调试<br>  

### analysis_wechat_friends_data.py<br>
获取微信好友信息，分析好友性别比例及省份分布，并将其可视化<br>
