#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
import numpy as np

def get_infos(page):
    header = {"User-Agent": "Mozilla/5.0 (Linux Android 6.0 Nexus 5 Build/MRA58N)"
                                    "AppleWebKit/537.36 (KHTML,like Gecko) "
                                    "Chrome/73.0.3683.86 Mobile Safari/537.36"}

    data = {
    "page":page,"size":30,"uri":"apidata/api/gk/special/lists"
    }
    # 1320/30=44
    # 20x66 1320
    # size=30 1页30条
    url='https://api.eol.cn/gkcx/api'
    infos=[]
    for i in range(0,30):
        # json.loads(response.content) 将json对象转为dict'
        # get方法
        data_json=requests.post(url,headers=header,data=data).json()['data']['item'][i]
        name = data_json['name']
        rankall = data_json['rankall']
        name_type = data_json['level3_name']
        rank_type = data_json['rank_type']
        edu = data_json['level1_name'].replace('（高职）',' ')
        limit_year = data_json['limit_year']
        view_total = data_json['view_total']
        info = {
            "name":name,
            "rank_type":rank_type,
            "name_type":name_type,
            "rankall":rankall,
            "edu":edu,
            "limit_year":limit_year,
            "view_total":view_total,
        }
        infos.append(info)
    df = pd.DataFrame(data=infos, columns=['name', 'rankall', 'name_type', 'rank_type', 'edu','limit_year','view_total'])
    return df


if __name__ == '__main__':
    empty_df = pd.DataFrame(columns=['name', 'rankall', 'name_type', 'rank_type', 'edu', 'limit_year', 'view_total'])
    for i in range(0,44):
        df=get_infos(i)
        print(df)
        empty_df=empty_df.append(df)
        print('第'+str(i+1)+'页--写入成功')
    # time.sleep(2)
    df1=empty_df.reset_index(drop=True)
    df1.index=np.arange(1,len(df1)+1)
    df1.to_csv('../data/csv/'+'zy_rank'+'.csv')


# In[ ]:




