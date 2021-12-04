#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
import re
import numpy as np

def get_data(page):
    header = {"User-Agent": "Mozilla/5.0 (Linux Android 6.0 Nexus 5 Build/MRA58N)"
                                        "AppleWebKit/537.36 (KHTML,like Gecko) "
                                        "Chrome/73.0.3683.86 Mobile Safari/537.36"}

    url='http://gaokao.xdf.cn/college/china/searchProvincesLine/____'+str(page)
    data=requests.get(url,headers=header).text
    a=re.findall("var strs='(.*?)'",data)[0]
    years=re.findall('"year":(.*?),',a,re.S)
    scores=re.findall('"score":(.*?),',a,re.S)
    provinces=re.findall('"provinces":"(.*?)"',a,re.S)
    pcs=re.findall('"pc":"(.*?)"',a,re.S)
    types=re.findall('"type":"(.*?)"',a,re.S)
    datas=[]

    for year,pc,type,score,province in zip(years,pcs,types,scores,provinces):
        data={
            'year':year,
            'pc':pc,
            'type':type,
            'score':score,
            'province':province
        }
        datas.append(data)
    df=pd.DataFrame(data=datas,columns=['year','pc','type','score','province'])
    return df


if __name__ == '__main__':
    empty_df = pd.DataFrame(columns=['year', 'pc','type', 'score', 'province'])
    for i in range(1,38):
        df=get_data(i)
        print(df)
        empty_df=empty_df.append(df)
        print('第'+str(i)+'页--写入成功')
        # time.sleep(2)
    df1=empty_df.reset_index(drop=True)
    df1.index=np.arange(1,len(df1)+1)
    df1.to_csv('../data/csv/'+'score'+'.csv')

