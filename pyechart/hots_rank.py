#!/usr/bin/env python
# coding: utf-8

# In[28]:


from pyecharts.charts import Bar,Pie # 导入Bar,Pie
from pyecharts import options as opts # 导入options
from pyecharts.globals import ThemeType,CurrentConfig, NotebookType # 导入主题,配置,类型
import pandas as pd
from snapshot_selenium import snapshot # 图片渲染
from pyecharts.render import make_snapshot # 图片渲染
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB # 修改默认notebook类型(jupyter notebook)


# In[30]:


# 读取数据,删除多余列
data = pd.read_csv('../data/csv/zy_rank.csv').drop('Unnamed: 0',axis=1) 
# 根据view_total进行降序,并去重
a = data.sort_values(by="view_total" , ascending=False).drop_duplicates()
# 取出前十
b = a.iloc[0:10]
# 取出name列表
name = b.name.tolist()
# 取出view_total列表
hots = b.view_total.tolist()

# 绘制柱状图
bar = (
    Bar(init_opts=opts.InitOpts(theme = ThemeType.CHALK,page_title="十大热门专业",width="1200px",height="600px")) # 设置主题
    .add_xaxis(name)
    .add_yaxis("热度", hots)
    # 全局变量
    .set_global_opts(title_opts=opts.TitleOpts(title="十大热门专业", # title
                                               subtitle_textstyle_opts={"color":"gray","fontSize":"14"}, # 二级titleStyle
                                               subtitle="Source:college.gaokao.com",# 文字
                                               subtitle_link='http://college.gaokao.com/schlist'), # 链接
                     toolbox_opts = opts.ToolboxOpts(is_show = True), # 显示工具栏
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=25),), # x轴倾斜
                     datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(type_='inside')]) # 外部滑动和内部滑动
    .set_series_opts(
     label_opts = opts.LabelOpts(is_show = True) # 显示值文本
    ,markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max"), # 标记点max
                                                 opts.MarkPointItem(name = "min",type_ = "min")]) # 标记点min
    ,markline_opts = opts.MarkLineOpts(data = [opts.MarkLineItem(name = "average",type_ = "average")])) # 标记线average
)
bar.load_javascript() # 加载js
bar.render_notebook() # 显示
# bar.render('../data/view/zy-rank-bar.html') # 存为html
# make_snapshot(snapshot, bar.render(), "../data/img/zy-rank-bar.png") # 存为img


# In[32]:


down1 = a.iloc[-11:-1] # 取出后十列
name = down1.name.tolist() # name列表
hots = down1.view_total.tolist() # hots列表

bar = (
    Bar(init_opts=opts.InitOpts(theme = ThemeType.DARK,page_title="十大冷门专业",width="1200px",height="600px")) # 设置主题
    .add_xaxis(name)
    .add_yaxis("热度", hots)
    # 全局变量
    .set_global_opts(title_opts=opts.TitleOpts(title="十大冷门专业", # title
                                               subtitle_textstyle_opts={"color":"gray","fontSize":"14"}, # 二级title
                                               subtitle="Source:college.gaokao.com",
                                               subtitle_link='http://college.gaokao.com/schlist'),
                     toolbox_opts = opts.ToolboxOpts(is_show = True), # 显示工具栏
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=25),), # x轴倾斜
                     datazoom_opts=[opts.DataZoomOpts(),opts.DataZoomOpts(type_='inside')]) # 内外部滑动
    .set_series_opts(
     label_opts = opts.LabelOpts(is_show = True) # 显示文本
    ,markpoint_opts = opts.MarkPointOpts(data = [opts.MarkPointItem(type_ = "max",name = "max"), # 标记点max
                                                 opts.MarkPointItem(name = "min",type_ = "min")]) # 标记点min
    ,markline_opts = opts.MarkLineOpts(data = [opts.MarkLineItem(name = "average",type_ = "average")])) #标记线
)
bar.load_javascript() # 加载js
bar.render_notebook()
# bar.render('../data/view/zy-down-rank-bar.html')
# make_snapshot(snapshot, bar.render(), "../data/img/zy-down-rank-bar.png")


# In[34]:


# 统计view_total的总数返回一个Series对象
c = a.groupby(by="name_type")['view_total'].sum()
# 进行降序,取出前十
d = c.sort_values(ascending=False).head(10)
# index列表
rank_type=d.index.tolist()
# values列表
rank_hots=d.values.tolist()

pie = (
        # 主题、title、width、height
        Pie(init_opts=opts.InitOpts(theme = ThemeType.MACARONS,page_title="热门专业类所占比",width="1200px",height="600px")) 
        .add(
            "",
            [list(z) for z in zip(rank_type,rank_hots)],
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
        .set_global_opts(title_opts=opts.TitleOpts(title="热门专业类所占比"))
    )
pie.load_javascript()
pie.render_notebook()
# pie.render('../data/view/zy-rank_type-pie.html')
# make_snapshot(snapshot, pie.render(), "../data/img/zy-rank_type-pie.png")

    


# In[36]:


# 进行降序,取出后十
down2 = c.sort_values(ascending=False).tail(10)
# index列表
rank_type=down2.index.tolist()
# values列表
rank_hots=down2.values.tolist()

pie = (
        Pie(init_opts=opts.InitOpts(theme = ThemeType.MACARONS,page_title="热门专业类所占比",width="1200px",height="600px"))
        .add(
            "",
            [list(z) for z in zip(rank_type,rank_hots)],
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
        .set_global_opts(title_opts=opts.TitleOpts(title="热门专业类所占比"))
    )
pie.load_javascript()
pie.render_notebook()
# pie.render('../data/view/zy-down-rank_type-pie.html')
# make_snapshot(snapshot, pie.render(), "../data/img/zy-down-rank_type-pie.png")


# In[ ]:





# In[ ]:




