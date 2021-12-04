#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar,Page
from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType,CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

# 读取数据
data = pd.read_csv('../data/csv/score.csv')
# 删除多余列
data = data.drop('Unnamed: 0',axis=1)
data1=data[(data["year"]>2016)]
# print(data1)
# 筛选条件
data2=data1[(data1["pc"]=="本科二批")|(data1["pc"]=="本科批")]
# 过滤掉分组后元素小于6的,返回df
a = data2.groupby(by='province').filter(lambda x: len(x) >= 6)
# 去重
a1 = a.drop_duplicates()
# 重置索引
a2 =a1.reset_index(drop=True)
a2.index = np.arange(1,len(a2)+1)
# 修改df 将pc列值为本科批修改成本科二批
a2.loc[a2.pc=='本科批','pc'] = '本科二批'
# a1.to_csv('../data/csv/score1.csv')

# 29
a3 = a2.groupby(by=['type','year']) # 遍历出来的元素是元组类型
arts_scores1=[]
science_scores1=[]
arts_scores2=[]
science_scores2=[]
arts_scores3=[]
science_scores3=[]
provinces=[]
all_provinces=[]

# 筛选条件
for group in a3:
  if (group[0][1] == 2017) & (group[0][0]=='文科'):
    arts_scores1=group[1]['score'].tolist()
    provinces=group[1]['province'].tolist()
  elif (group[0][1] == 2017) & (group[0][0]=='理科'):
    science_scores1 = group[1]['score'].tolist()
  elif (group[0][1] == 2018) & (group[0][0]=='文科'):
    arts_scores2=group[1]['score'].tolist()
  elif (group[0][1] == 2018) & (group[0][0]=='理科'):
    science_scores2 = group[1]['score'].tolist()
  elif (group[0][1] == 2019) & (group[0][0]=='文科'):
    arts_scores3 = group[1]['score'].tolist()
  elif (group[0][1] == 2019) & (group[0][0]=='理科'):
    science_scores3 = group[1]['score'].tolist()

#  绘制柱状图
bar1 = (
    Bar(init_opts=opts.InitOpts(theme = ThemeType.DARK,page_title="录取分数线",width="1200px",height="600px")) # 设置主题
    .add_xaxis(provinces)
    .add_yaxis("2017文科", arts_scores1)
    .add_yaxis("2017理科", science_scores1)
    .add_yaxis("2018文科", arts_scores2)
    .add_yaxis("2018理科", science_scores2)
    .add_yaxis("2019文科", arts_scores3)
    .add_yaxis("2019理科", science_scores2)
    .set_global_opts(title_opts=opts.TitleOpts(title="各地区2017-2019本科录取分数线",
                                               subtitle_textstyle_opts={"color":"gray","fontSize":"14"},
                                               subtitle="Source:gaokao.xdf.cn",
                                               subtitle_link='http://gaokao.xdf.cn/college/china/searchProvincesLine/____1'),
                     toolbox_opts = opts.ToolboxOpts(is_show = True), # 显示工具栏
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=25),), # x轴倾斜
                     datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(type_='inside')]) # 全局变量
    .set_series_opts(
     label_opts = opts.LabelOpts(is_show = True)) # 显示文本
)

bar1.load_javascript()
bar1.render_notebook()


# In[7]:


# bar1.render('../data/view/three-score-bar.html')
# make_snapshot(snapshot, bar1.render(), "../data/img/three-score-bar.png")


# In[ ]:




