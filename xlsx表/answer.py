import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from math import pi
plt.rcParams['font.family'] = ['SimHei', 'Arial']  # 替换为您系统中存在的字体


'''
背景知识： ./file/农林牧渔业总产值.xlsx文件中的农林牧渔业总产值、农业、林业、牧业和渔业共计五张独立的sheet，列名都从第四行开始
列名有省份、2003年、2003年……一直到2022年等项，不存在汇总各个省份的全国项。产值单位为亿元，根据下列查询要求，输出实现可执行python代码
'''

'''
背景知识： 查询会给定一个xlsx文件的路径，包含的各张工作表sheet的名称，数据列名从第几行开始，行列有哪些属性，请根据下面的查询要求，输出格式正确可以执行且结果正确的python代码
'''

#饼图
def query11():#查询2010年全国各省农林牧渔总产值的分布比例，使用饼图表示：
    file_path='./file/农林牧渔业总产值.xlsx'
    df=pd.read_excel(file_path, sheet_name='农林牧渔总产值',header=3,usecols=['省份','2010年'])

    plt.pie(df['2010年'],labels=df['省份'],autopct='%1.1f%%')
    plt.title('2010年全国各省农林牧渔总产值分布')
    #确保 饼图为圆形，避免被压成椭圆
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def query12():#查询2020年全国各省农业的分布比例，使用饼图表示：
    file_path='./file/农林牧渔业总产值.xlsx'
    df=pd.read_excel(file_path, sheet_name='农业',header=3,usecols=['省份','2020年'])

    plt.pie(df['2020年'],labels=df['省份'],autopct='%1.1f%%')
    plt.title('2020年全国各省农业产值分布')
    #确保 饼图为圆形，避免被压成椭圆
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def query13():#查询河北2020年农林牧渔业产值的比例，使用饼图表示
    # 读取 Excel 文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农林牧渔业产值的数据
    df1 = pd.read_excel(file_path, sheet_name="农业", header=3)
    df2 = pd.read_excel(file_path, sheet_name="林业", header=3)
    df3 = pd.read_excel(file_path, sheet_name="牧业", header=3)
    df4 = pd.read_excel(file_path, sheet_name="渔业", header=3)

    
    # 提取河北省在2020年的数据
    data_1_2020 = df1.loc[df1["省份"] == "河北", "2020年"].values[0]
    data_2_2020 = df2.loc[df2["省份"] == "河北", "2020年"].values[0]
    data_3_2020 = df3.loc[df3["省份"] == "河北", "2020年"].values[0]
    data_4_2020 = df4.loc[df4["省份"] == "河北", "2020年"].values[0]
    
    # 绘制饼图
    labels = ['农业', '林业', '牧业','渔业']
    sizes = [data_1_2020, data_2_2020, data_3_2020,data_4_2020]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('河北2020年农林牧渔业产值比例')
    plt.show()

'''其中东部包括：北京、天津、河北、上海、江苏、浙江、福建、山东、广东和海南。 
中部包括：山西、安徽、江西、河南、湖北和湖南。 
西部包括：内蒙古、广西、重庆、四川、贵州、云南、西藏、陕西、甘肃、青海、宁夏和新疆。
东北包括：辽宁、吉林和黑龙江。'''
def query14():#查询2019年在东部、中部、西部和东北这四个地区内部的渔业产值比较，使用四个子图饼图表示，标注比例
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"
    df = pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 筛选出2019年的数据
    df_2019 = df[['省份', '2019年']]

    # 根据地区划分数据
    regions = {
        '东部': ['北京', '天津', '河北', '上海', '江苏', '浙江', '福建', '山东', '广东', '海南'],
        '中部': ['山西', '安徽', '江西', '河南', '湖北', '湖南'],
        '西部': ['内蒙古', '广西', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆'],
        '东北': ['辽宁', '吉林', '黑龙江']
    }

    # 添加地区信息和筛选数据
    df_2019['地区'] = None
    for region, provinces in regions.items():
        df_2019.loc[df_2019['省份'].isin(provinces), '地区'] = region

    # 筛选数据
    filtered_df = df_2019[df_2019['地区'].notnull()]

    # 绘制四个子图
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))

    def plot_pie(data, title, ax):
        ax.pie(data['2019年'], labels=data['省份'], autopct='%1.1f%%', startangle=140)
        ax.set_title(title)

    for (region, data), ax in zip(filtered_df.groupby('地区'), axes.flatten()):
        plot_pie(data, f'2019年{region}地区渔业产值比例', ax)

    plt.show()

def query15():#查询2022年在东部、中部、西部和东北这四个地区的各地区渔业产值之和的比例，使用饼图表示，标注比例
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"
    df = pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 筛选出2022年的数据
    df_2022 = df[['省份', '2022年']]

    # 根据地区划分数据
    regions = {
        '东部': ['北京', '天津', '河北', '上海', '江苏', '浙江', '福建', '山东', '广东', '海南'],
        '中部': ['山西', '安徽', '江西', '河南', '湖北', '湖南'],
        '西部': ['内蒙古', '广西', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆'],
        '东北': ['辽宁', '吉林', '黑龙江']
    }

    # 添加地区信息和筛选数据
    df_2022['地区'] = None
    for region, provinces in regions.items():
        df_2022.loc[df_2022['省份'].isin(provinces), '地区'] = region

    # 筛选数据
    filtered_df = df_2022[df_2022['地区'].notnull()]

    # 按地区分组并计算各地区渔业产值之和
    grouped_df = filtered_df.groupby('地区')['2022年'].sum().reset_index()

    # 绘制饼图
    plt.figure(figsize=(8, 8))
    plt.pie(grouped_df['2022年'], labels=grouped_df['地区'], autopct='%1.1f%%', startangle=140)
    plt.title('2022年各地区渔业产值比例')
    plt.show()


#折线图
def query21():#查询山东和河南在2003年至2022年的农业产值变化趋势对比，使用折线图表示
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农业的数据
    df_other = pd.read_excel(file_path, sheet_name="农业", header=3, index_col=0)

    # 选择山东和河南的数据
    cities = ["山东", "河南"]
    df_selected_cities = df_other.loc[cities, "2003年":"2022年"]

    # 转置数据，使得年份成为行索引
    df_selected_cities_transposed = df_selected_cities.T

    # 绘制折线图
    ax = df_selected_cities_transposed.plot(kind="line", marker="o", figsize=(12, 6))
    ax.set_ylabel("产值（亿元）")
    ax.set_xlabel("年份")
    ax.set_title("2003年至2022年山东和河南农业产值变化趋势对比")
    # 显示图形
    plt.show()

def query22():#查询江苏在2005年至2015年的渔业产值的趋势，使用折线图表示
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取渔业产值的数据
    df_total = pd.read_excel(file_path, sheet_name="渔业", header=3, index_col=0)

    # 选择江苏省的数据
    province = "江苏"
    df_jiangsu = df_total.loc[[province], "2005年":"2015年"]

    # 转置数据，使得年份成为行索引
    df_jiangsu_transposed = df_jiangsu.T

    # 绘制折线图
    ax = df_jiangsu_transposed.plot(kind="line", marker="o", figsize=(12, 6))
    ax.set_ylabel("产值（亿元）")
    ax.set_xlabel("年份")
    ax.set_title("2005年至2015年江苏渔业产值趋势")

    # 显示图形
    plt.show()

def query23():#查询2003至2022年辽宁的农林牧渔四个产业在辽宁的农林牧渔总产值中占比的变化，绘制四条折线的折线图表示，标注数值
    # 读取Excel文件
    file_path = './file/农林牧渔业总产值.xlsx'
    
    df_agriculture = pd.read_excel(file_path, sheet_name="农业", header=3)
    df_forestry = pd.read_excel(file_path, sheet_name="林业", header=3)
    df_animal_husbandry = pd.read_excel(file_path, sheet_name="牧业", header=3)
    df_fishery = pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 读取农林牧渔业总产值数据
    df_total = pd.read_excel(file_path, sheet_name="农林牧渔总产值", header=3)

    # 提取辽宁省的数据
    liaoning_total = df_total.loc[df_total["省份"] == "辽宁", "2003年":"2022年"].values.flatten()

    # 提取辽宁省各产业在2003年至2022年的数据
    liaoning_agriculture = df_agriculture.loc[df_agriculture["省份"] == "辽宁", "2003年":"2022年"].values.flatten()
    liaoning_forestry = df_forestry.loc[df_forestry["省份"] == "辽宁", "2003年":"2022年"].values.flatten()
    liaoning_animal_husbandry = df_animal_husbandry.loc[df_animal_husbandry["省份"] == "辽宁", "2003年":"2022年"].values.flatten()
    liaoning_fishery = df_fishery.loc[df_fishery["省份"] == "辽宁", "2003年":"2022年"].values.flatten()

    # 计算占比
    percentage_agriculture = liaoning_agriculture / liaoning_total * 100
    percentage_forestry = liaoning_forestry / liaoning_total * 100
    percentage_animal_husbandry = liaoning_animal_husbandry / liaoning_total * 100
    percentage_fishery = liaoning_fishery / liaoning_total * 100

    # 绘制折线图
    years = list(range(2003, 2023))
    plt.plot(years, percentage_agriculture, label='农业', marker='o')
    plt.plot(years, percentage_forestry, label='林业', marker='o')
    plt.plot(years, percentage_animal_husbandry, label='牧业', marker='o')
    plt.plot(years, percentage_fishery, label='渔业', marker='o')

    # 在每个数据点上标注具体数值
    for i, year in enumerate(years):
        plt.annotate(f"{percentage_agriculture[i]:.2f}%", (year, percentage_agriculture[i] + 1))
        plt.annotate(f"{percentage_forestry[i]:.2f}%", (year, percentage_forestry[i] + 1))
        plt.annotate(f"{percentage_animal_husbandry[i]:.2f}%", (year, percentage_animal_husbandry[i] + 1))
        plt.annotate(f"{percentage_fishery[i]:.2f}%", (year, percentage_fishery[i] + 1))

    plt.xlabel('年份')
    plt.ylabel('占比（%）')
    plt.title('2003至2022年辽宁农林牧渔业产值占比变化')
    plt.legend()
    plt.grid(True)
    plt.show()


#柱状图
def query31():#查询并比较2016年各省份农林牧渔业各业产值，使用柱状图表示
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农林牧渔业产值的数据
    df1 = pd.read_excel(file_path, sheet_name="农业", header=3, index_col=0)
    df2 = pd.read_excel(file_path, sheet_name="林业", header=3, index_col=0)
    df3 = pd.read_excel(file_path, sheet_name="牧业", header=3, index_col=0)
    df4 = pd.read_excel(file_path, sheet_name="渔业", header=3, index_col=0)

    # 选择2016年的数据
    year_2016 = "2016年"
    data1_2016 = df1[year_2016]
    data2_2016 = df2[year_2016]
    data3_2016 = df3[year_2016]
    data4_2016 = df4[year_2016]

    # 合并数据
    df_combined = pd.DataFrame({"农业": data1_2016, "林业": data2_2016, "牧业": data3_2016, "渔业": data4_2016})

    # 绘制柱状图
    ax = df_combined.plot(kind="bar", figsize=(12, 6), rot=45, colormap="viridis")
    ax.set_ylabel("产值（亿元）")
    ax.set_xlabel("省份")
    ax.set_title("2016年各省份农林牧渔业各业产值比较")
    # 显示图形
    plt.show()

def query32():#查询广东和广西2018年农林牧渔各个产业产值对比，横坐标为农林牧渔四个产业，使用并列柱状图表示，条柱标注数值，输出实现代码
    # 读取Excel文件的四个Sheet
    file_path = "./file/农林牧渔业总产值.xlsx"
    df_1 = pd.read_excel(file_path, sheet_name="农业", header=3)
    df_2 = pd.read_excel(file_path, sheet_name="林业", header=3)
    df_3 = pd.read_excel(file_path, sheet_name="牧业", header=3)
    df_4 = pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 选择需要的数据，包括省份和2018年的产值
    columns_to_select = ['省份', '2018年']
    df_1_selected = df_1[columns_to_select]
    df_2_selected = df_2[columns_to_select]
    df_3_selected = df_3[columns_to_select]
    df_4_selected = df_4[columns_to_select]

    # 将四个产业的数据合并到一个新的DataFrame
    df_combined = pd.DataFrame({
        "农业": df_1_selected.set_index('省份')['2018年'],
        "林业": df_2_selected.set_index('省份')['2018年'],
        "牧业": df_3_selected.set_index('省份')['2018年'],
        "渔业": df_4_selected.set_index('省份')['2018年']
    })

    # 选择广东和广西的数据
    df_gd_gx = df_combined.loc[['广东', '广西']]

    # 绘制柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 转置以使产业成为横坐标
    bar_plot = df_gd_gx.T.plot(kind='bar', ax=ax, width=0.8, cmap='viridis')

    # 在每个条柱的中心位置添加对应的数字
    for p in bar_plot.patches:
        height = p.get_height()
        width = p.get_x() + p.get_width() / 2
        ax.text(width, height + 0.1, f'{height:.2f}', ha="center")

    # 设置图形属性
    ax.set_xlabel('产业')
    ax.set_ylabel('产值（亿元）')
    ax.set_title('2018年广东和广西农林牧渔各个产业产值对比')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()

def query33():#查询安徽2012年农林牧渔各个产业产值对比，横坐标为农林牧渔四个产业，使用并列柱状图表示，条柱标注数值
    # 读取Excel文件的四个Sheet
    file_path = "./file/农林牧渔业总产值.xlsx"
    df_1 = pd.read_excel(file_path, sheet_name="农业", header=3)
    df_2 = pd.read_excel(file_path, sheet_name="林业", header=3)
    df_3 = pd.read_excel(file_path, sheet_name="牧业", header=3)
    df_4 = pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 选择需要的数据，包括省份和2012年的产值
    columns_to_select = ['省份', '2012年']
    df_1_selected = df_1[columns_to_select]
    df_2_selected = df_2[columns_to_select]
    df_3_selected = df_3[columns_to_select]
    df_4_selected = df_4[columns_to_select]

    # 将四个产业的数据合并到一个新的DataFrame
    df_combined = pd.DataFrame({
        "农业": df_1_selected.set_index('省份')['2012年'],
        "林业": df_2_selected.set_index('省份')['2012年'],
        "牧业": df_3_selected.set_index('省份')['2012年'],
        "渔业": df_4_selected.set_index('省份')['2012年']
    })

    # 选择安徽的数据
    df_gd_gx = df_combined.loc[['安徽']]

    # 绘制柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 转置以使产业成为横坐标
    bar_plot = df_gd_gx.T.plot(kind='bar', ax=ax, width=0.8, cmap='viridis')

    # 在每个条柱的中心位置添加对应的数字
    for p in bar_plot.patches:
        height = p.get_height()
        width = p.get_x() + p.get_width() / 2
        ax.text(width, height + 0.1, f'{height:.2f}', ha="center")

    # 设置图形属性
    ax.set_xlabel('产业')
    ax.set_ylabel('产值（亿元）')
    ax.set_title('2022年安徽农林牧渔各个产业产值对比')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()

def query34():#查询浙江在2002年至2022年的农林牧渔总产值变化，使用柱状图表示，条柱标注数值
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取渔业产值的数据
    df_total = pd.read_excel(file_path, sheet_name="农林牧渔总产值", header=3, index_col=0)

    # 选择浙江的数据
    province = "浙江"
    df_zhejiang = df_total.loc[[province], "2002年":"2022年"]

    # 转置数据，使得年份成为行索引
    df_zhejiang_transposed = df_zhejiang.T

    # 绘制柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_plot = df_zhejiang_transposed.plot(kind='bar', ax=ax, width=0.8, cmap='viridis')

    # 在每个条柱的中心位置添加对应的数字
    for p in bar_plot.patches:
        height = p.get_height()
        width = p.get_x() + p.get_width() / 2
        ax.text(width, height + 0.1, f'{height:.2f}', ha="center")

    # 设置图形属性
    ax.set_xlabel('年份')
    ax.set_ylabel('产值（亿元）')
    ax.set_title('2002到2022年浙江农林牧渔总产值变化')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()

    # 显示图形
    plt.show()


#柱线混合图
def query41():#查询新疆在2004年至2022年的农业产值及年均增长率，使用柱线混合图表示，标注数值
    # 读取Excel文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df = pd.read_excel(file_path, sheet_name='农业', header=3, index_col='省份')

    # 选择新疆的数据并提取2004年至2022年的数据
    province = "新疆"
    begin_year='2004年'
    end_year='2022年'
    
    df_province = df.loc[province, begin_year:end_year]

    # 计算年均增长率
    annual_growth_rate = df_province.pct_change() * 100

    # 绘制柱线混合图
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('年份')
    ax1.set_ylabel('年均增长率（%）', color=color)
    line = ax1.plot(df_province.index[:-1], annual_growth_rate.values[1:], color=color, marker='o', label='年均增长率')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('农业产值（亿元）', color=color)
    bars = ax2.bar(df_province.index, df_province.values, color=color, alpha=0.7)
    ax2.tick_params(axis='y', labelcolor=color)

    # 在每个数据点上标注年均增长率
    for i, value in enumerate(annual_growth_rate.values[1:]):
        ax1.text(df_province.index[i], value,
                f'{value:.2f}%', ha='right', va='bottom', color='black')

    # 在每个柱形上标注数值
    for bar, value in zip(bars, df_province.values):
        ax2.text(bar.get_x() + bar.get_width() / 2, value,
                f'{value:.2f}', ha='center', va='bottom', color='black')

    fig.tight_layout()
    plt.title('新疆2004年至2022年农业产值及年均增长率')
    plt.show()

def query42():#查询2003年至2022年的全国牧业总产值及年均增长率，使用柱线混合图表示，标注数值
    # 读取Excel文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df = pd.read_excel(file_path, sheet_name='牧业', header=3, index_col='省份')

    # 计算全国的数据并提取2003年至2022年的数据
    begin_year='2003年'
    end_year='2022年'
    national_data = df.sum(axis=0)[begin_year:end_year]

    # 计算年均增长率
    annual_growth_rate = national_data.pct_change() * 100

    # 绘制柱线混合图
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('年份')
    ax1.set_ylabel('年均增长率（%）', color=color)
    line = ax1.plot(national_data.index[:-1], annual_growth_rate.values[1:], color=color, marker='o', label='年均增长率')
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('牧业产值（亿元）', color=color)
    bars = ax2.bar(national_data.index, national_data.values, color=color, alpha=0.7)
    ax2.tick_params(axis='y', labelcolor=color)

    # 在每个数据点上标注年均增长率
    for i, value in enumerate(annual_growth_rate.values[1:]):
        ax1.text(national_data.index[i], value,
                 f'{value:.2f}%', ha='right', va='bottom', color='black')

    # 在每个柱形上标注数值
    for bar, value in zip(bars, national_data.values):
        ax2.text(bar.get_x() + bar.get_width() / 2, value,
                 f'{value:.2f}', ha='center', va='bottom', color='black')

    fig.tight_layout()
    plt.title('全国2003年至2022年牧业总产值及年均增长率')
    plt.show()
    
def query43():#查询2012年至2022年的全国林业总产值及林业总产值在农林牧渔总产值中的占比，使用柱线混合图表示，标注数值
     # 读取Excel文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df_total = pd.read_excel(file_path, sheet_name='农林牧渔总产值', header=3, index_col='省份')
    df_forestry = pd.read_excel(file_path, sheet_name='林业', header=3, index_col='省份')

    # 计算全国的数据并提取2012年至2022年的数据
    begin_year='2012年'
    end_year='2022年'
    national_agri_forestry = df_total.sum(axis=0)[begin_year:end_year]
    national_forestry = df_forestry.sum(axis=0)[begin_year:end_year]

    # 计算林业总产值在农林牧渔总产值中的占比
    percentage_forestry_in_agri_forestry = (national_forestry / national_agri_forestry) * 100

    # 绘制柱线混合图
    fig, ax1 = plt.subplots()

    color1 = 'tab:blue'
    ax1.set_xlabel('年份')
    ax1.set_ylabel('林业总产值（亿元）', color=color1)
    bars1 = ax1.bar(national_forestry.index, national_forestry.values, color=color1, alpha=0.7, label='林业总产值')
    ax1.tick_params(axis='y', labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.set_ylabel('占比（%）', color=color2)
    line2 = ax2.plot(percentage_forestry_in_agri_forestry.index, percentage_forestry_in_agri_forestry.values, color=color2, marker='s', label='占比')
    ax2.tick_params(axis='y', labelcolor=color2)

    # 在每个柱形上标注林业总产值
    for bar, value in zip(bars1, national_forestry.values):
        ax1.text(bar.get_x() + bar.get_width() / 2, value,
                 f'{value:.2f}', ha='center', va='bottom', color='black')

    # 在每个数据点上标注占比
    for i, value in enumerate(percentage_forestry_in_agri_forestry.values):
        ax2.text(percentage_forestry_in_agri_forestry.index[i], value,
                 f'{value:.2f}%', ha='center', va='bottom', color='black')

    fig.tight_layout()
    plt.title('全国2012年至2022年林业总产值及占比')
    plt.show()


#5+3+4+3
#1+3+2+1+2+2

#修改了堆叠柱状图 增加了堆叠面积图62 63
 
#堆叠柱状图
def query51():#绘制2020年各省份在农林牧渔各个行业产值的堆叠柱状图，不同类型使用不同颜色表示
    # 读取Excel文件
    file_path = './file/农林牧渔业总产值.xlsx'
    # 读取农林牧渔业产值的数据
    df1 = pd.read_excel(file_path, sheet_name="农业", header=3, index_col='省份')
    df2 = pd.read_excel(file_path, sheet_name="林业", header=3, index_col='省份')
    df3 = pd.read_excel(file_path, sheet_name="牧业", header=3, index_col='省份')
    df4 = pd.read_excel(file_path, sheet_name="渔业", header=3, index_col='省份')

    year_2020="2020年"
    # 合并数据
    df_combined = pd.concat([df1[year_2020], df2[year_2020], df3[year_2020],df4[year_2020]], axis=1)
    df_combined.columns = ['农业', '林业', '牧业','渔业']

    # 绘制堆叠柱状图
    ax = df_combined.plot(kind='bar', stacked=True, figsize=(12, 8))
    ax.set_title('各省份2020年农林牧渔各个行业产值对比')
    ax.set_ylabel('产值（亿元）')

    plt.show()


#堆叠面积图
def query61():#查询2003年至2022年每个省份的农林牧渔总产值变化，以堆叠面积图绘制
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"
    df = pd.read_excel(file_path, header=3)

    # 选择需要的数据，省份和2003年至2022年的产值
    df_selected = df[['省份'] + [str(year) + '年' for year in range(2003, 2023)]]

    # 调整数据结构，使用年份作为索引
    df_selected.set_index('省份', inplace=True)

    # 转置数据，方便堆积面积图的绘制
    df_transposed = df_selected.transpose()

    # 绘制堆积面积图
    fig, ax = plt.subplots(figsize=(12, 8))

    df_transposed.plot.area(ax=ax, cmap='tab20', alpha=0.7, stacked=True)

    # 设置图形属性
    ax.set_xlabel('年份')
    ax.set_ylabel('农林牧渔总产值')
    ax.set_title('2003年至2022年各省份农林牧渔总产值堆积面积图')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()
def query62():# 查询2003年至2022年黑龙江农业林业牧业渔业产值变化，以四行业产值的堆叠面积图绘制
    # 读取Excel文件的四个工作表的数据
    filename = "./file/农林牧渔业总产值.xlsx"
    df1 = pd.read_excel(filename, sheet_name="农业", header=3, index_col=0)
    df2 = pd.read_excel(filename, sheet_name="林业", header=3, index_col=0)
    df3 = pd.read_excel(filename, sheet_name="牧业", header=3, index_col=0)
    df4 = pd.read_excel(filename, sheet_name="渔业", header=3, index_col=0)

    # 提取黑龙江的数据
    province = "黑龙江"
    df_1 = df1.loc[[province], "2003年":"2022年"]
    df_2 = df2.loc[[province], "2003年":"2022年"]
    df_3 = df3.loc[[province], "2003年":"2022年"]
    df_4 = df4.loc[[province], "2003年":"2022年"]

    # 转置数据，使得年份成为行索引
    df_1 = df_1.transpose()
    df_2 = df_2.transpose()
    df_3 = df_3.transpose()
    df_4 = df_4.transpose()

    # 绘制堆积面积图
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.fill_between(df_1.index, 0, df_1.values.flatten(), alpha=0.8, label="农业")
    ax.fill_between(df_2.index, df_1.values.flatten(), (df_1 + df_2).values.flatten(), alpha=0.8, label="林业")
    ax.fill_between(df_3.index, (df_1 + df_2).values.flatten(), (df_1 + df_2 + df_3).values.flatten(), alpha=0.8, label="牧业")
    ax.fill_between(df_4.index, (df_1 + df_2 + df_3).values.flatten(), (df_1 + df_2 + df_3 + df_4).values.flatten(), alpha=0.8, label="渔业")

    ax.set_xlabel("年份")
    ax.set_ylabel("产值（亿元）")
    ax.set_title("2003年至2022年黑龙江农业林业牧业渔业产值变化堆叠面积图")
    ax.legend()
    plt.xticks(rotation=45)

    plt.show()
def query63():#查询2003年至2022年河北河南山东山西四省的农林牧渔业总产值变化，以分年度四省总产值的堆积面积图绘制
    # 读取Excel文件的五个工作表
    file_path = './file/农林牧渔业总产值.xlsx'
    df1 = pd.read_excel(file_path, sheet_name='农林牧渔业总产值', header=3, index_col=0)

    # 选择2003年至2022年的数据
    years = [str(year) + '年' for year in range(2003, 2023)]

    data = df1.loc[['河北', '河南', '山东', '山西'], years]#选择河北河南山东山西四省的数据
    # 计算四省的总产值，按年度堆积绘制面积图
    data_T = data.T # 转置，使得年度成为行索引
    fig, ax = plt.subplots(figsize=(12, 8))

    # 绘制堆积面积图
    data_T.plot(kind='area', stacked=True, ax=ax)

    ax.set_xlabel('年度')
    ax.set_ylabel('产值（亿元）')
    ax.set_title('2003年至2022年河北河南山东山西四省农林牧渔业总产值变化')

    plt.show()

#热图
def query71():#查询2003年至2022年每个省份的农林牧渔总产值变化率，制作一张热图
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"
    df = pd.read_excel(file_path, sheet_name='农林牧渔业总产值', header=3, index_col=0)  # 从第四行开始读取，省份作为索引列

    # 提取2003年至2022年的数据
    data_years = df.loc[:, "2003年":"2022年"]

    # 计算每个省份的汽车拥有量变化率
    change_rate = data_years.pct_change(axis=1) * 100  # 计算百分比变化率

    # print(change_rate.axes)

    # 绘制热图
    plt.figure(figsize=(12, 10))
    sns.heatmap(change_rate, annot=True,cmap="coolwarm",cbar_kws={'label': '变化率'}, annot_kws={'va': 'center', 'ha': 'center'})
    plt.title("2003年至2022年各省份农林牧渔总产值变化率热图")
    plt.show()
 
def query72():#查询2004年至2018年每个省份的农业产值变化率并制作热图
    # 读取 Excel 文件
    file_path = "./file/农林牧渔业总产值.xlsx"
    df = pd.read_excel(file_path, sheet_name="农业", header=3, index_col=0)

    # 提取2004年至2018年的数据
    data_years = df.loc[:, "2004年":"2018年"]
    # 计算变化率
    df_change = data_years.pct_change(axis=1) * 100

    # 制作热图
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_change, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.5, annot_kws={"size": 8})
    plt.title("2004年至2018年每个省份的农业产值变化率")
    plt.show()
    

#玫瑰图
def query81():#查询全国各个省份在2015年的农林牧渔业各个行业产值占比，使用玫瑰图表示
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农林牧渔业产值的数据
    df1 = pd.read_excel(file_path, sheet_name="农业", header=3, index_col=0)
    df2 = pd.read_excel(file_path, sheet_name="林业", header=3, index_col=0)
    df3 = pd.read_excel(file_path, sheet_name="牧业", header=3, index_col=0)
    df4 = pd.read_excel(file_path, sheet_name="渔业", header=3, index_col=0)

    # 选择所有省份在2015年的数据
    value1_2015 = df1.loc[:, "2015年"]
    value2_2015 = df2.loc[:, "2015年"]
    value3_2015 = df3.loc[:, "2015年"]
    value4_2015 = df4.loc[:, "2015年"]

    # 创建堆叠柱状玫瑰图
    theta = np.linspace(0.0, 2*np.pi, len(value1_2015), endpoint=False)
    width = 0.2  # 设置柱状宽度

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_offset(np.pi/2)
    ax.set_theta_direction(-1)

    bars_1 = ax.bar(theta, value1_2015, width=width, label='农业')
    bars_2 = ax.bar(theta, value2_2015, width=width, label='林业', bottom=value1_2015)
    bars_3 = ax.bar(theta, value3_2015, width=width, label='牧业', bottom=value1_2015+value2_2015)
    bars_4 = ax.bar(theta, value4_2015, width=width, label='渔业', bottom=value1_2015+value2_2015+value3_2015)

    # 添加标签
    ax.set_thetagrids(np.degrees(theta), labels=df1.index)
    ax.legend()

    plt.title("2015年各省农林牧渔业产值占比")

    # 显示图形
    plt.show()


   
   #雷达图


#雷达图
def query91():#查询河北在2003年与2022年的农林牧渔各产业产值对比，并制作雷达图：
    # 读取 Excel 文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农林牧渔业产值的数据
    df1 = pd.read_excel(file_path, sheet_name="农业", header=3)
    df2 = pd.read_excel(file_path, sheet_name="林业", header=3)
    df3 = pd.read_excel(file_path, sheet_name="牧业", header=3)
    df4 = pd.read_excel(file_path, sheet_name="渔业", header=3)

    
    # 提取河北省在2022年的数据
    hebei_1_2022 = df1.loc[df1["省份"] == "河北", "2022年"].values[0]
    hebei_2_2022 = df2.loc[df2["省份"] == "河北", "2022年"].values[0]
    hebei_3_2022 = df3.loc[df3["省份"] == "河北", "2022年"].values[0]
    hebei_4_2022 = df4.loc[df4["省份"] == "河北", "2022年"].values[0]
    
    # 提取河北省在2003年的数据
    hebei_1_2003 = df1.loc[df1["省份"] == "河北", "2003年"].values[0]
    hebei_2_2003 = df2.loc[df2["省份"] == "河北", "2003年"].values[0]
    hebei_3_2003 = df3.loc[df3["省份"] == "河北", "2003年"].values[0]
    hebei_4_2003 = df4.loc[df4["省份"] == "河北", "2003年"].values[0]
    
    # 绘制雷达图
    num_industries = 4
    angles = np.linspace(0, 2 * np.pi, num_industries, endpoint=False).tolist()
    angles += angles[:1]  # 闭合图形

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # 2022年的数据
    values_2022 = [hebei_1_2022, hebei_2_2022, hebei_3_2022, hebei_4_2022]
    values_2022 += values_2022[:1]  # 闭合图形
    ax.plot(angles, values_2022, label='2022年')
    ax.fill(angles, values_2022, alpha=0.25)

    # 2003年的数据
    values_2003 = [hebei_1_2003, hebei_2_2003, hebei_3_2003, hebei_4_2003]
    values_2003 += values_2003[:1]  # 闭合图形
    ax.plot(angles, values_2003, label='2003年')
    ax.fill(angles, values_2003, alpha=0.25)

    ax.set_thetagrids(np.degrees(angles[:-1]), ['农业', '林业', '牧业', '渔业'])
    ax.set_title('河北农林牧渔业产值对比 (2003年 vs. 2022年)')

    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.show()
    
def query92():#查询全国在2003年与2022年的农林牧渔总产值各个省份对比，并制作雷达图：
    # 读取 Excel 文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农林牧渔业总产值的数据
    df = pd.read_excel(file_path, sheet_name="农林牧渔业总产值", header=3, index_col=0)

    # 选择所有省份在2003年的数据
    value_2003 = df.loc[:, "2003年"]

    # 选择所有省份在2022年的数据
    value_2022 = df.loc[:, "2022年"]

    # 获取省份列表
    provinces = df.index
    
    # 设置雷达图的角度（省份个数）
    num_provinces = len(provinces)
    angles = np.linspace(0, 2 * np.pi, num_provinces, endpoint=False).tolist()

    # 闭合图形
    value_2003 = np.concatenate((value_2003, [value_2003.iloc[0]]))
    value_2022 = np.concatenate((value_2022, [value_2022.iloc[0]]))
    angles += angles[:1]


    # 创建雷达图
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.plot(angles, value_2003, label='2003年')
    ax.fill(angles, value_2003, alpha=0.25)

    ax.plot(angles, value_2022, label='2022年')
    ax.fill(angles, value_2022, alpha=0.25)

    # 添加标签
    ax.set_thetagrids(np.degrees(angles[:-1]), provinces)
    ax.set_title("2003年与2022年农林牧渔业总产值对比", size=14, pad=10)
    ax.legend(loc='upper right')

    # 显示图形
    plt.show()


#散点图
def query101():#查询在2012年至2022年，全国各省农业产值之和与渔业产值之和之间有什么关系？制作散点图来展示这种关系
    # 读取 Excel 文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df_agriculture = pd.read_excel(file_path, sheet_name="农业", header=3)
    df_fishery= pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 提取全国的农业总产值和渔业总产值数据（2012年至2022年）
    years = list(map(str, range(2012, 2023)))
    national_agriculture_total = df_agriculture.sum(axis=0)['2012年':'2022年']
    national_fishery_total = df_fishery.sum(axis=0)['2012年':'2022年']
    
    # 创建散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(national_agriculture_total, national_fishery_total, alpha=0.8)

    # 添加年份标签
    for i, year in enumerate(years):
        plt.annotate(year, (national_agriculture_total[i], national_fishery_total[i]), fontsize=8)

    plt.title('2012年-2022年全国农业总产值与渔业总产值散点图')
    plt.xlabel('农业总产值（亿元）')
    plt.ylabel('渔业总产值（亿元）')
    plt.grid(True)
    plt.show()

def query102():#查询在2019年，各个省份的牧业产值与林业产值之间有什么关系？制作散点图来展示这种关系
    # 读取 Excel 文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df_animal = pd.read_excel(file_path, sheet_name="牧业", header=3, index_col='省份')
    df_forestry = pd.read_excel(file_path, sheet_name="林业", header=3, index_col='省份')

    # 提取各个省份在2019年的农业和渔业产值数据
    animal_2019 = df_animal.loc[:, '2019年']
    forestry_2019 = df_forestry.loc[:, '2019年']

    # 创建散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(animal_2019, forestry_2019, alpha=0.8)

    # 添加省份标签
    for province in df_animal.index:
        plt.annotate(province, (animal_2019[province], forestry_2019[province]), fontsize=8)

    plt.title('2019年各省份牧业产值与林业产值散点图')
    plt.xlabel('牧业产值（亿元）')
    plt.ylabel('林业产值（亿元）')
    plt.grid(True)
    plt.show()


if __name__=='__main__':
    query102()