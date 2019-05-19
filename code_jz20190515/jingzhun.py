# -*- coding: utf-8 -*-
import requests,time,os
import pandas as pd

#基础数据
baseurl = 'https://rong.36kr.com/n/api/'



#读取id
data = pd.read_csv(os.path.join('..','total_v2.csv'))
idlist = data['url'].values
for i in range(10):
    print(idlist[i])

#获取网页

#判断是否获取网页
#截取信息


#保存数据

#如果没有获取停止