#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyecharts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType,CurrentConfig, NotebookType
import pandas as pd
from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

# 读取数据
data = pd.read_csv('../data/csv/score.csv')
# 删除多余列
data = data.drop('Unnamed: 0',axis=1)
# 分组
a = data.groupby(by='province')
# 取出北京df
b = a.get_group('北京')
# print(b)
# 取出year不等于2011的df
b = b[b["year"]!=2011]
# 取出本科一批和二批的df
c = b[(b["pc"]=='本科一批')|(b["pc"]=='本科二批')]
# 分组
d = c.groupby(by='type')
# 取出文理科数据
arts = d.get_group('文科')
science = d.get_group('理科')
# 取出score转为list
y1_arts_scores = arts['score'].tolist()
y2_science_scores = science['score'].tolist()
x_alls=['2015本科一批','2015本科二批', '2016本科一批', '2016本科二批', '2017本科一批', '2017本科二批', '2018本科一批',  '2018本科二批']


# 绘制柱状图
bar = Bar("柱状图数据堆叠示例")
bar.add('文科',x_alls,y1_arts_scores,mark_point=['average'])
bar.add('理科',x_alls,y2_science_scores,mark_line=['min','max'])
bar.render('柱状图标记线和标记点.html')


# bar = (
#     Bar(init_opts=opts.InitOpts(theme = ThemeType.DARK,page_title="录取分数线",width="1200px",height="600px")) # 设置主题
#     .add_xaxis(x_alls)
#     .add_yaxis("文科", y1_arts_scores)
#     .add_yaxis("理科", y2_science_scores)
#     .set_global_opts(title_opts=opts.TitleOpts(title="北京地区2015-2018本科录取分数线",
#                                                subtitle_textstyle_opts={"color":"gray","fontSize":"14"},
#                                                subtitle="Source:gaokao.xdf.cn",
#                                                subtitle_link='http://gaokao.xdf.cn/college/china/searchProvincesLine/____1'),
#                      toolbox_opts = opts.ToolboxOpts(is_show = True),
#                      xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=25),),
#                      datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(type_='inside')]) # 全局变量
#     .set_series_opts(
#      label_opts = opts.LabelOpts(is_show = True)
#     ,markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max"),
#                                                  opts.MarkPointItem(name = "min",type_ = "min")])
#     ,markline_opts = opts.MarkLineOpts(data = [opts.MarkLineItem(name = "average",type_ = "average")]))
# )
# bar.load_javascript()
# bar.render_notebook()
# bar.render('../data/view/Beijing-score-bar.html')
# make_snapshot(snapshot, bar.render(), "../data/img/Beijing-score-bar.png")

