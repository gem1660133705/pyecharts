#!/usr/bin/env python
# coding: utf-8

from pyecharts.charts import Bar,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType,CurrentConfig, NotebookType,ChartType, SymbolType
import pandas as pd
# from snapshot_selenium import snapshot
# from pyecharts.render import make_snapshot
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB 
# 导入包


# 读取数据,删除多余列
data1 = pd.read_csv('../data/csv/benke.csv').drop(['feature','Unnamed: 0'],axis=1)
data2 = pd.read_csv('../data/csv/zhuanke.csv').drop(['Unnamed: 0'],axis=1)
data = data1.append(data2)
# 筛选数据
a = data.loc[(data.location!=" ------")&(data.location!=" ——")]
b = a.groupby(by='location').size()
c = b.sort_values(ascending=False)
indexs = c.index.tolist()
cities = c.values.tolist()
# 绘制柱状图
bar = (
    Bar(init_opts=opts.InitOpts(theme = ThemeType.PURPLE_PASSION,page_title="各城市高校数量统计",width="1200px",height="600px")) # 设置主题
    .add_xaxis(indexs)
    .add_yaxis("数量", cities)
    .set_global_opts(title_opts=opts.TitleOpts(title="各地区高校数量统计",
                                               subtitle_textstyle_opts={"color":"gray","fontSize":"14"},
                                               subtitle="Source:college.gaokao.com",
                                               subtitle_link='http://college.gaokao.com/schlist'),
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
# bar.render('../data/view/all_school-bar.html')

# 绘制Geo地图

geo= (
    Geo()
        .add_schema(maptype="china")
        .add("数量", [list(z) for z in zip(indexs, cities)],type_=ChartType.EFFECT_SCATTER,)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_=330),
            title_opts=opts.TitleOpts(title="各地区高校数量统计"),
        )
)
geo.load_javascript()
geo.render_notebook()
# geo.render('../data/view/all-score-geo.html')
# make_snapshot(snapshot, bar1.render(), "../data/img/all-score-geo.png")


pros=[]
zhuankes=[]
benkes=[]
d  = a.groupby(by=['location','nature'])
for group in d:
    if group[0][1] == " 本科":
        pros.append(group[0][0])
        benkes.append(group[1].sname.size)
    elif group[0][1] == " 高职专科":
        zhuankes.append(group[1].sname.size)

        
#  绘制柱状图
bar1 = (
    Bar(init_opts=opts.InitOpts(theme = ThemeType.DARK,page_title="全国高校分布",width="1200px",height="600px")) # 设置主题
    .add_xaxis(pros)
    .add_yaxis("本科", benkes)
    .add_yaxis("高职专科", zhuankes)
    .set_global_opts(title_opts=opts.TitleOpts(title="全国高校分布情况",
                                               subtitle_textstyle_opts={"color":"gray","fontSize":"14"},
                                               subtitle="Source:gaokao.xdf.cn",
                                               subtitle_link='http://gaokao.xdf.cn/college/china/searchProvincesLine/____1'),
                     toolbox_opts = opts.ToolboxOpts(is_show = True),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=25),),
                     datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(type_='inside')]) # 全局变量
    .set_series_opts(
     label_opts = opts.LabelOpts(is_show = True))
)



bar1.load_javascript()
bar1.render_notebook()
# bar1.render('../data/view/two-type-bar.html')
# make_snapshot(snapshot, bar1.render(), "../data/img/two-type-bar.png")






