#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyecharts.charts import Bar,Geo,Pie
from pyecharts import options as opts
# from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType,CurrentConfig, NotebookType,ChartType, SymbolType
import pandas as pd
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB 




# 读取数据
data = pd.read_csv('../data/csv/benke.csv')
# 删除多余列
data = data.drop('Unnamed: 0',axis=1)
# 筛选数据
a = data.loc[(data.feature!="——")&(data.location!=" ------")]
# 分组计算每组大小
b = a.groupby(by ="location").size()
# 降序
c = b.sort_values(ascending=False)
# indexs列表
indexs = c.index.tolist()
# cities_nums列表
cities_nums = c.values.tolist()

# 绘制柱状图
bar = (
    Bar(init_opts=opts.InitOpts(theme = ThemeType.LIGHT,page_title="各地区985-211学校数量统计",width="1200px",height="600px")) # 设置主题
    .add_xaxis(indexs)
    .add_yaxis("数量", cities_nums)
    .set_global_opts(title_opts=opts.TitleOpts(title="各地区985-211学校数量统计",
                                               subtitle_textstyle_opts={"color":"gray","fontSize":"14"},
                                               subtitle="Source:college.gaokao.com",
                                               subtitle_link='http://college.gaokao.com/schlist/a100/s1/p1'),
                     toolbox_opts = opts.ToolboxOpts(is_show = True),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=25),),
                     datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(type_='inside')]) # 全局变量
    .set_series_opts(
     label_opts = opts.LabelOpts(is_show = True)
    ,markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max"),
                                                 opts.MarkPointItem(name = "min",type_ = "min")])
    ,markline_opts = opts.MarkLineOpts(data = [opts.MarkLineItem(name = "average",type_ = "average")]))
)
bar.load_javascript()
bar.render_notebook()
# bar.render('../data/view/high_school-bar.html')
# make_snapshot(snapshot, bar.render(), "../data/img/high_school-bar.png")


# In[6]:


# 读取数据,删除多余列
data1 = pd.read_csv('../data/csv/benke.csv').drop(['feature','Unnamed: 0'],axis=1)
data2 = pd.read_csv('../data/csv/zhuanke.csv').drop(['Unnamed: 0'],axis=1)
data = data1.append(data2)
# 筛选数据
a = data.loc[data.type!=" ------"]
b = a.groupby(by='type').size()
c = b.sort_values(ascending=False)
indexs = c.index.tolist()
cities = c.values.tolist()
pie = (
        Pie(init_opts=opts.InitOpts(theme = ThemeType.MACARONS,page_title="高校类型所占比",width="1200px",height="600px"))
        .add(
            "",
            [list(z) for z in zip(indexs,cities)],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="高校类型所占比"))
    )
pie.load_javascript()
pie.render_notebook()
# pie.render('../data/view/school-type-pie.html')
# make_snapshot(snapshot, pie.render(), "../data/img/school-type-pie.png")






