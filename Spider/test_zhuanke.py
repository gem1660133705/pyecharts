#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import re
import pandas as pd
import numpy as np
import time

def get_info(page):
    header = {"User-Agent": "Mozilla/5.0 (Linux Android 6.0 Nexus 5 Build/MRA58N)"
                                    "AppleWebKit/537.36 (KHTML,like Gecko) "
                                    "Chrome/73.0.3683.86 Mobile Safari/537.36"}

    url='http://college.gaokao.com/schlist/a100/s2/p'+str(page)
    html=requests.get(url,headers=header).text
    all=re.findall(r'>全部</h4>(.*?)"fany">',html,re.S)
    datas=[]
    url_infos=[]
    # img_infos=[]
    sname_infos=[]
    location_infos=[]
    feature_infos=[]
    type_infos=[]
    membership_infos=[]
    nature_infos=[]
    website_infos=[]

    for i in all:
        data=re.findall(r'<dl>(.*?)</dl>',i,re.S)
        for i in data:
            s_info=re.findall(r'<dt>(.*?)</ul>',i,re.S)
            url_info=re.findall(r'<a href="(.*?)" target="_blank">',str(s_info),re.S)[0]
            # img_info=re.findall(r'<img src="(.*?)".*?',str(s_info),re.S)[0]
            sname_info=re.findall(r'<a href=".*?">(.*?)</a>',str(s_info),re.S)[1]
            s_list=re.findall(r'<li>(.*?)</li>',str(s_info),re.S)
            location_info=s_list[0].replace('高校所在地：',' ')
            feature_info=re.findall(r'<span class=".*?">(.*?)</span>',s_list[1],re.S)
            if len(feature_info)==2:
                feature_infos.append(feature_info[0] + '-' + feature_info[1])
            if not feature_info:
                feature_infos.append('——')
            else:
                for i in feature_info:
                    feature_infos.append(i)
            type_info = s_list[2].replace('高校类型：', ' ')
            membership_info = s_list[3].replace('高校隶属：', ' ')
            nature_info=s_list[4].replace('高校性质：', ' ')
            website_info = s_list[5].replace('学校网址：', ' ')

            url_infos.append(url_info)
            # img_infos.append(img_info)
            sname_infos.append(sname_info)
            type_infos.append(type_info)
            location_infos.append(location_info)
            membership_infos.append(membership_info)
            nature_infos.append(nature_info)
            website_infos.append(website_info)


    for sname,location,url,type,membership,website,nature in zip(sname_infos,location_infos,url_infos,type_infos,membership_infos,website_infos,nature_infos):
        data = {
            "sname": sname,
            "location": location,
            "url": url,
            "type": type,
            "membership": membership,
            "website": website,
            "nature": nature
        }
        datas.append(data)
    df = pd.DataFrame(data=datas,columns=['sname', 'location', 'url', 'type', 'membership','website', 'nature'])
    return df



if __name__ == '__main__':
    empty_df = pd.DataFrame(columns=['sname', 'location', 'url', 'type', 'membership', 'website', 'nature'])
    for i in range(1,45):
        df=get_info(i)
        print(df)
        empty_df=empty_df.append(df)
        print('第'+str(i)+'页--写入成功')
        # time.sleep(2)
    df1=empty_df.reset_index(drop=True)
    df1.index=np.arange(1,len(df1)+1)
    df1.to_csv('../data/csv/'+'zhuanke'+'.csv')

