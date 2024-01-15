import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from math import pi
plt.rcParams['font.family'] = ['SimHei', 'Arial']  # 替换为您系统中存在的字体


'''
背景知识： ./file/农林牧渔业总产值.xlsx文件中的农林牧渔业总产值、农业、林业、牧业和渔业产值共计五张独立的sheet，列名都从第四行开始
列名有省份、2003年、2003年……一直到2022年等项，不存在汇总各个省份的全国项。产值单位为亿元，根据下列查询要求，输出实现可执行python代码
'''

'''
背景知识： 查询会给定一个xlsx文件的路径，包含的各张工作表sheet的名称，数据列名从第几行开始，行列有哪些属性，请根据下面的查询要求，输出格式正确可以执行且结果正确的python代码
'''

#饼图
def query():#查询2020年全国各省农林牧渔总产值的分布比例，使用饼图表示
    file_name='./file/农林牧渔业总产值.xlsx'
    df=pd.read_excel(file_name, sheet_name='农林牧渔业总产值',header=3,usecols=['省份','2020年'])

    plt.pie(df['2020年'],labels=df['省份'],autopct='%1.1f%%')
    plt.title('2020年全国各省农林牧渔总产值分布')
    #确保 饼图为圆形，避免被压成椭圆
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def query92():#查询2015年全国各省牧业产值的分布比例，使用饼图表示
    file_name='./file/农林牧渔业总产值.xlsx'
    df=pd.read_excel(file_name, sheet_name='牧业',header=3,usecols=['省份','2015年'])

    plt.pie(df['2015年'],labels=df['省份'],autopct='%1.1f%%')
    plt.title('2015年全国各省牧业产值分布')
    #确保 饼图为圆形，避免被压成椭圆
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

#折线图
def query81():#查询云南和广西在2003年至2022年的林业产值变化趋势对比，使用折线图表示
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农业的数据
    df_other = pd.read_excel(file_path, sheet_name="林业", header=3, index_col=0)

    # 选择浙江和福建的数据
    cities = ["广西", "云南"]
    df_selected_cities = df_other.loc[cities, "2003年":"2022年"]

    # 转置数据，使得年份成为行索引
    df_selected_cities_transposed = df_selected_cities.T

    # 绘制折线图
    ax = df_selected_cities_transposed.plot(kind="line", marker="o", figsize=(12, 6))
    ax.set_ylabel("产值（亿元）")
    ax.set_xlabel("年份")
    ax.set_title("2003年至2022年广西和云南林业产值变化趋势对比")
    # 显示图形
    plt.show()

#柱状图

def query71():#查询四川2022年农林牧渔各个产业产值对比，横坐标为农林牧渔四个产业，使用并列柱状图表示，条柱标注数值
    # 读取Excel文件的四个Sheet
    file_path = "./file/农林牧渔业总产值.xlsx"
    df_1 = pd.read_excel(file_path, sheet_name="农业", header=3)
    df_2 = pd.read_excel(file_path, sheet_name="林业", header=3)
    df_3 = pd.read_excel(file_path, sheet_name="牧业", header=3)
    df_4 = pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 选择需要的数据，包括省份和2022年的产值
    columns_to_select = ['省份', '2022年']
    df_1_selected = df_1[columns_to_select]
    df_2_selected = df_2[columns_to_select]
    df_3_selected = df_3[columns_to_select]
    df_4_selected = df_4[columns_to_select]

    # 将四个产业的数据合并到一个新的DataFrame
    df_combined = pd.DataFrame({
        "农业": df_1_selected.set_index('省份')['2022年'],
        "林业": df_2_selected.set_index('省份')['2022年'],
        "牧业": df_3_selected.set_index('省份')['2022年'],
        "渔业": df_4_selected.set_index('省份')['2022年']
    })

    # 选择四川的数据
    df_province = df_combined.loc[['四川']]

    # 绘制柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 转置以使产业成为横坐标
    bar_plot = df_province.T.plot(kind='bar', ax=ax, width=0.8, cmap='viridis')

    # 在每个条柱的中心位置添加对应的数字
    for p in bar_plot.patches:
        height = p.get_height()
        width = p.get_x() + p.get_width() / 2
        ax.text(width, height + 0.1, f'{height:.2f}', ha="center")

    # 设置图形属性
    ax.set_xlabel('产业')
    ax.set_ylabel('产值（亿元）')
    ax.set_title('2022年四川农林牧渔各个产业产值对比')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()

def query72():#查询江苏和安徽2018年农林牧渔各个产业产值对比，横坐标为农林牧渔四个产业，使用并列柱状图表示，条柱标注数值
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
    df_gd_gx = df_combined.loc[['江苏', '安徽']]

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
    ax.set_title('2018年江苏和安徽农林牧渔各个产业产值对比')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()


#柱线混合图
def query61():#查询西藏在2004年至2022年的牧业产值及年均增长率，使用柱线混合图表示，标注数值
    # 读取Excel文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df = pd.read_excel(file_path, sheet_name='牧业', header=3, index_col='省份')

    # 选择西藏的数据并提取2004年至2022年的数据
    province = "西藏"
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
    ax2.set_ylabel('牧业产值（亿元）', color=color)
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
    plt.title('西藏2004年至2022年牧业产值及年均增长率')
    plt.show()



#堆叠柱状图
def query51():#绘制2010年各省份在农林牧渔各个行业产值的堆叠柱状图，不同类型使用不同颜色表示
    # 读取Excel文件
    file_path = './file/农林牧渔业总产值.xlsx'
    # 读取农林牧渔业产值的数据
    df1 = pd.read_excel(file_path, sheet_name="农业", header=3, index_col='省份')
    df2 = pd.read_excel(file_path, sheet_name="林业", header=3, index_col='省份')
    df3 = pd.read_excel(file_path, sheet_name="牧业", header=3, index_col='省份')
    df4 = pd.read_excel(file_path, sheet_name="渔业", header=3, index_col='省份')

    year_2010="2010年"
    # 合并数据
    df_combined = pd.concat([df1[year_2010], df2[year_2010], df3[year_2010],df4[year_2010]], axis=1)
    df_combined.columns = ['农业', '林业', '牧业','渔业']

    # 绘制堆叠柱状图
    ax = df_combined.plot(kind='bar', stacked=True, figsize=(12, 8))
    ax.set_title('各省份2010年农林牧渔各个行业产值对比')
    ax.set_ylabel('产值（亿元）')

    plt.show()


#堆叠面积图
def query41():#查询2003年至2022年广东广西湖南湖北四省的农林牧渔业总产值变化，以分年度四省总产值的堆积面积图绘制
    # 读取Excel文件的五个工作表
    file_path = './file/农林牧渔业总产值.xlsx'
    df1 = pd.read_excel(file_path, sheet_name='农林牧渔业总产值', header=3, index_col=0)

    # 选择2003年至2022年的数据
    years = [str(year) + '年' for year in range(2003, 2023)]

    data = df1.loc[['广东', '广西', '湖南', '湖北'], years]#选择河北河南山东山西四省的数据
    # 计算四省的总产值，按年度堆积绘制面积图
    data_T = data.T # 转置，使得年度成为行索引
    fig, ax = plt.subplots(figsize=(12, 8))

    # 绘制堆积面积图
    data_T.plot(kind='area', stacked=True, ax=ax)

    ax.set_xlabel('年度')
    ax.set_ylabel('产值（亿元）')
    ax.set_title('2003年至2022年广东广西湖南湖北四省农林牧渔业总产值变化')

    plt.show()

def query42():# 查询2012年至2022年江西农业林业牧业渔业产值变化，以四行业产值的堆叠面积图绘制
    # 读取Excel文件的四个工作表的数据
    filename = "./file/农林牧渔业总产值.xlsx"
    df1 = pd.read_excel(filename, sheet_name="农业", header=3, index_col=0)
    df2 = pd.read_excel(filename, sheet_name="林业", header=3, index_col=0)
    df3 = pd.read_excel(filename, sheet_name="牧业", header=3, index_col=0)
    df4 = pd.read_excel(filename, sheet_name="渔业", header=3, index_col=0)

    # 提取江西的数据
    province = "江西"
    df_1 = df1.loc[[province], "2012年":"2022年"]
    df_2 = df2.loc[[province], "2012年":"2022年"]
    df_3 = df3.loc[[province], "2012年":"2022年"]
    df_4 = df4.loc[[province], "2012年":"2022年"]

    # 转置数据，使得年份成为行索引
    df_1 = df_1.transpose()
    df_2 = df_2.transpose()
    df_3 = df_3.transpose()
    df_4 = df_4.transpose()

    # 绘制堆叠面积图
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.fill_between(df_1.index, 0, df_1.values.flatten(), alpha=0.8, label="农业")
    ax.fill_between(df_2.index, df_1.values.flatten(), (df_1 + df_2).values.flatten(), alpha=0.8, label="林业")
    ax.fill_between(df_3.index, (df_1 + df_2).values.flatten(), (df_1 + df_2 + df_3).values.flatten(), alpha=0.8, label="牧业")
    ax.fill_between(df_4.index, (df_1 + df_2 + df_3).values.flatten(), (df_1 + df_2 + df_3 + df_4).values.flatten(), alpha=0.8, label="渔业")

    ax.set_xlabel("年份")
    ax.set_ylabel("产值（亿元）")
    ax.set_title("2012年至2022年江西农业林业牧业渔业产值变化堆叠面积图")
    ax.legend()
    plt.xticks(rotation=45)

    plt.show()

#热图

def query31():#查询2003年至2022年每个省份的林业产值变化率并制作热图
    # 读取 Excel 文件
    file_path = "./file/农林牧渔业总产值.xlsx"
    df = pd.read_excel(file_path, sheet_name="林业", header=3, index_col=0)

    # 提取2003年至2022年的数据
    data_years = df.loc[:, "2003年":"2022年"]
    # 计算变化率
    df_change = data_years.pct_change(axis=1) * 100

    # 制作热图
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_change, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.5, annot_kws={"size": 8})
    plt.title("2003年至2022年每个省份的林业产值变化率")
    plt.show()
    

#玫瑰图
def query21():#查询全国各个省份在2020年的农林牧渔业各个行业产值占比，使用玫瑰图表示
    # 读取Excel文件
    file_path = "./file/农林牧渔业总产值.xlsx"

    # 读取农林牧渔业产值的数据
    df1 = pd.read_excel(file_path, sheet_name="农业", header=3, index_col=0)
    df2 = pd.read_excel(file_path, sheet_name="林业", header=3, index_col=0)
    df3 = pd.read_excel(file_path, sheet_name="牧业", header=3, index_col=0)
    df4 = pd.read_excel(file_path, sheet_name="渔业", header=3, index_col=0)

    # 选择所有省份在2020年的数据
    value1_2020 = df1.loc[:, "2020年"]
    value2_2020 = df2.loc[:, "2020年"]
    value3_2020 = df3.loc[:, "2020年"]
    value4_2020 = df4.loc[:, "2020年"]

    # 创建堆叠柱状玫瑰图
    theta = np.linspace(0.0, 2*np.pi, len(value1_2020), endpoint=False)
    width = 0.2  # 设置柱状宽度

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_offset(np.pi/2)
    ax.set_theta_direction(-1)

    bars_1 = ax.bar(theta, value1_2020, width=width, label='农业')
    bars_2 = ax.bar(theta, value2_2020, width=width, label='林业', bottom=value1_2020)
    bars_3 = ax.bar(theta, value3_2020, width=width, label='牧业', bottom=value1_2020+value2_2020)
    bars_4 = ax.bar(theta, value4_2020, width=width, label='渔业', bottom=value1_2020+value2_2020+value3_2020)

    # 添加标签
    ax.set_thetagrids(np.degrees(theta), labels=df1.index)
    ax.legend()

    plt.title("2020年各省农林牧渔业产值占比")

    # 显示图形
    plt.show()


   
   #雷达图

#散点图
def query11():#查询在2005年至2022年，陕西农业产值与渔业产值之间是否存在明显的相关性？制作散点图来展示这种关系
    # 读取 Excel 文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df_agriculture = pd.read_excel(file_path, sheet_name="农业", header=3)
    df_fishery= pd.read_excel(file_path, sheet_name="渔业", header=3)

    # 提取陕西农业产值和渔业产值数据（2005年至2022年）
    years = list(map(str, range(2005, 2023)))
    national_agriculture_total = df_agriculture.sum(axis=0)['2005年':'2022年']
    national_fishery_total = df_fishery.sum(axis=0)['2005年':'2022年']
    
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

def query12():#查询在2013年，各个省份的农业产值与林业产值之间是否存在明显的相关性？制作散点图来展示这种关系
    # 读取 Excel 文件
    file_path = './file/农林牧渔业总产值.xlsx'
    df_agri = pd.read_excel(file_path, sheet_name="牧业", header=3, index_col='省份')
    df_forestry = pd.read_excel(file_path, sheet_name="林业", header=3, index_col='省份')

    # 提取各个省份在2013年的农业和渔业产值数据
    agri_2013 = df_agri.loc[:, '2013年']
    forestry_2013 = df_forestry.loc[:, '2013年']

    # 创建散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(agri_2013, forestry_2013, alpha=0.8)

    # 添加省份标签
    for province in df_agri.index:
        plt.annotate(province, (agri_2013[province], forestry_2013[province]), fontsize=8)

    plt.title('2013年各省份农业产值与林业产值散点图')
    plt.xlabel('农业产值（亿元）')
    plt.ylabel('林业产值（亿元）')
    plt.grid(True)
    plt.show()


if __name__=='__main__':
    query51()
    
   