import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from math import pi
plt.rcParams['font.family'] = ['SimHei', 'Arial']  # 替换为您系统中存在的字体

'''
地区生产总值统计.xlsx
地区生产总值
第一产业增加值
第二产业增加值
第三产业增加值
'''

'''
[
    {"conversations": 
    [{"role": "system","content": "背景知识：查询会给定一个xlsx文件的路径，包含的各张工作表sheet的名称，数据列名从第几行开始，行列有哪些属性，请根据下面的查询要求，输出格式和结果正确的可执行python代码"},
    {"role": "user", "content": "./file/农林牧渔业总产值.xlsx文件中的农林牧渔业总产值、农业、林业、牧业和渔业共计5张独立的sheet，列名都从第4行开始，列名有省份、2003年到2022年等项，不存在汇总各个省份的全国项。产值单位为亿元，请查询2010年全国各省地区生产总值的分布比例，使用饼图表示："},
    {"role": "assistant", "content": "import pandas as pd\nimport seaborn as sns\nimport matplotlib.pyplot as plt\nimport numpy as np\nfrom math import pi\nplt.rcParams['font.family'] = ['SimHei', 'Arial']  # 替换为您系统中存在的字体\n\ndef query():#查询2010年全国各省地区生产总值的分布比例，使用饼图表示：\n    file_name='./file/地区生产总值统计.xlsx'\n    df=pd.read_excel(file_name, sheet_name='地区生产总值',header=3,usecols=['省份','2010年'])\n\n    plt.pie(df['2010年'],labels=df['省份'],autopct='%1.1f%%')\n    plt.title('2010年全国各省地区生产总值分布')\n    #确保 饼图为圆形，避免被压成椭圆\n    plt.axis('equal')\n    plt.tight_layout()\n    plt.show()\n "}]}]


'''


'''
背景知识：查询会给定一个xlsx文件的路径，包含的各张工作表sheet的名称，数据列名从第几行开始，行列有哪些属性，请根据下面的查询要求，输出格式和结果正确的可执行python代码"
'''

'''
./file/地区生产总值统计.xlsx文件中的地区生产总值，第一产业增加值，第二产业增加值，第三产业增加值共计4张独立的sheet，列名都从第4行开始，列名有省份、2003年到2022年等项，不存在汇总各个省份的全国项。产值单位为亿元，
请查询2018年全国各省地区生产总值的分布比例，使用饼图表示：
'''

#饼图
def query11():#查询2018年全国各省地区生产总值的分布比例，使用饼图表示：
    file_path='./file/地区生产总值统计.xlsx'
    df=pd.read_excel(file_path, sheet_name='地区生产总值',header=3,usecols=['省份','2018年'])

    plt.pie(df['2018年'],labels=df['省份'],autopct='%1.1f%%')
    plt.title('2018年全国各省地区生产总值分布')
    #确保 饼图为圆形，避免被压成椭圆
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def query12():#查询2016年全国各省第一产业增加值的分布比例，使用饼图表示：
    file_path='./file/地区生产总值统计.xlsx'
    df=pd.read_excel(file_path, sheet_name='第一产业增加值',header=3,usecols=['省份','2016年'])

    plt.pie(df['2016年'],labels=df['省份'],autopct='%1.1f%%')
    plt.title('2016年全国各省第一产业增加值分布')
    #确保 饼图为圆形，避免被压成椭圆
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def query13():#查询河北2022年一二三产业增加值的比例，使用饼图表示
    # 读取 Excel 文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取一二三产业增加值的数据
    df1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3)
    df2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3)
    df3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3)

    # 提取河北在2022年的数据
    data_1_2022 = df1.loc[df1["省份"] == "河北", "2022年"].values[0]
    data_2_2022 = df2.loc[df2["省份"] == "河北", "2022年"].values[0]
    data_3_2022 = df3.loc[df3["省份"] == "河北", "2022年"].values[0]
    
    # 绘制饼图
    labels = ['第一产业增加值', '第二产业增加值', '第三产业增加值']
    sizes = [data_1_2022, data_2_2022, data_3_2022]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title('河北2022年一二三产业增加值比例')
    plt.show()


#折线图

def query21():#查询山东和河南在2003年至2022年的第一产业增加值变化趋势对比，使用折线图表示
    # 读取Excel文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取第一产业增加值数据
    df_other = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3, index_col=0)

    # 选择山东和河南的数据
    provinces = ["山东", "河南"]
    df_selected_cities = df_other.loc[provinces, "2003年":"2022年"]
    
    # print(df_other.index)
    # print(df_other.loc[provinces, "2003年":"2022年"])
    # 转置数据，使得年份成为行索引
    df_selected_cities_transposed = df_selected_cities.T

    # 绘制折线图
    ax = df_selected_cities_transposed.plot(kind="line", marker="o", figsize=(12, 6))
    ax.set_ylabel("产值（亿元）")
    ax.set_xlabel("年份")
    ax.set_title("2003年至2022年山东和河南第一产业增加值变化趋势对比")
    # 显示图形
    plt.show()

def query22():#查询江苏在2005年至2015年的第三产业增加值的趋势，使用折线图表示
    # 读取Excel文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取第三产业增加值的数据
    df_total = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3, index_col=0)

    # 选择江苏省的数据
    province = "江苏"
    df_province = df_total.loc[[province], "2005年":"2015年"]

    # 转置数据，使得年份成为行索引
    df_province_transposed = df_province.T

    # 绘制折线图
    ax = df_province_transposed.plot(kind="line", marker="o", figsize=(12, 6))
    ax.set_ylabel("产值（亿元）")
    ax.set_xlabel("年份")
    ax.set_title("2005年至2015年江苏第三产业增加值趋势")

    # 显示图形
    plt.show()

def query23():#查询2003至2022年辽宁的一二三产业增加值在辽宁的地区生产总值中占比的变化，绘制3条折线的折线图表示，标注数值
    # 读取Excel文件
    file_path = './file/地区生产总值统计.xlsx'
    
    df_1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3)
    df_2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3)
    df_3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3)

    # 读取地区生产总值数据
    df_total = pd.read_excel(file_path, sheet_name="地区生产总值", header=3)

    # 提取辽宁的数据
    liaoning_total = df_total.loc[df_total["省份"] == "辽宁", "2003年":"2022年"].values.flatten()

    # 提取辽宁各产业在2003年至2022年的数据
    liaoning_1 = df_1.loc[df_1["省份"] == "辽宁", "2003年":"2022年"].values.flatten()
    liaoning_2 = df_2.loc[df_2["省份"] == "辽宁", "2003年":"2022年"].values.flatten()
    liaoning_3 = df_3.loc[df_3["省份"] == "辽宁", "2003年":"2022年"].values.flatten()

    # 计算占比
    percentage_1 = liaoning_1 / liaoning_total * 100
    percentage_2 = liaoning_2 / liaoning_total * 100
    percentage_3 = liaoning_3 / liaoning_total * 100

    # 绘制折线图
    years = list(range(2003, 2023))
    plt.plot(years, percentage_1, label='第一产业增加值', marker='o')
    plt.plot(years, percentage_2, label='第二产业增加值', marker='o')
    plt.plot(years, percentage_3, label='第三产业增加值', marker='o')

    # 在每个数据点上标注具体数值
    for i, year in enumerate(years):
        plt.annotate(f"{percentage_1[i]:.2f}%", (year, percentage_1[i] + 1))
        plt.annotate(f"{percentage_2[i]:.2f}%", (year, percentage_2[i] + 1))
        plt.annotate(f"{percentage_3[i]:.2f}%", (year, percentage_3[i] + 1))

    plt.xlabel('年份')
    plt.ylabel('占比（%）')
    plt.title('2003至2022年辽宁一二三产业增加值占比变化')
    plt.legend()
    plt.grid(True)
    plt.show()



#柱状图
def query31():#查询并比较2006年各省份一二三产业增加值，使用柱状图表示
    # 读取Excel文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取一二三产业增加值的数据
    df1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3, index_col=0)
    df2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3, index_col=0)
    df3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3, index_col=0)

    # 选择2006年的数据
    year_2006 = "2006年"
    data1_2006 = df1[year_2006]
    data2_2006 = df2[year_2006]
    data3_2006 = df3[year_2006]

    # 合并数据
    df_combined = pd.DataFrame({"第一产业增加值": data1_2006, "第二产业增加值": data2_2006,  "第三产业增加值": data3_2006})

    # 绘制柱状图
    ax = df_combined.plot(kind="bar", figsize=(12, 6), rot=45, colormap="viridis")
    ax.set_ylabel("产值（亿元）")
    ax.set_xlabel("省份")
    ax.set_title("2006年各省份一二三产业增加值比较")
    # 显示图形
    plt.show()


def query32():#查询广东和广西2017年一二三产业增加值对比，横坐标为一二三3个产业，使用并列柱状图表示，条柱标注数值，输出实现代码
    # 读取Excel文件的四个Sheet
    file_path = "./file/地区生产总值统计.xlsx"
    df_1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3)
    df_2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3)
    df_3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3)

    # 选择需要的数据，包括省份和2017年的产值
    columns_to_select = ['省份', '2017年']
    df_1_selected = df_1[columns_to_select]
    df_2_selected = df_2[columns_to_select]
    df_3_selected = df_3[columns_to_select]

    # 将四个产业的数据合并到一个新的DataFrame
    df_combined = pd.DataFrame({
        "第一产业增加值": df_1_selected.set_index('省份')['2017年'],
        "第二产业增加值": df_2_selected.set_index('省份')['2017年'],
        "第三产业增加值": df_3_selected.set_index('省份')['2017年'],
    })

    # 选择广东和广西的数据
    df_province = df_combined.loc[['广东', '广西']]

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
    ax.set_title('2017年广东和广西一二三产业增加值对比')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()



def query33():#查询安徽2012年一二三产业增加值对比，横坐标为一二三3个产业，使用并列柱状图表示，条柱标注数值
    # 读取Excel文件的四个Sheet
    file_path = "./file/地区生产总值统计.xlsx"
    df_1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3)
    df_2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3)
    df_3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3)

    # 选择需要的数据，包括省份和2012年的产值
    columns_to_select = ['省份', '2012年']
    df_1_selected = df_1[columns_to_select]
    df_2_selected = df_2[columns_to_select]
    df_3_selected = df_3[columns_to_select]

    # 将四个产业的数据合并到一个新的DataFrame
    df_combined = pd.DataFrame({
        "第一产业增加值": df_1_selected.set_index('省份')['2012年'],
        "第二产业增加值": df_2_selected.set_index('省份')['2012年'],
        "第三产业增加值": df_3_selected.set_index('省份')['2012年']
    })

    # 选择安徽的数据
    df_province = df_combined.loc[['安徽']]

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
    ax.set_title('2012年安徽一二三产业增加值对比')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()


def query34():#查询浙江在2003年至2022年的地区生产总值变化，使用柱状图表示，条柱标注数值
    # 读取Excel文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取地区生产总值的数据
    df_total = pd.read_excel(file_path, sheet_name="地区生产总值", header=3, index_col=0)

    # 选择浙江的数据
    province = "浙江"
    df_province = df_total.loc[[province], "2003年":"2022年"]

    # 转置数据，使得年份成为行索引
    df_province_transposed = df_province.T

    # 绘制柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_plot = df_province_transposed.plot(kind='bar', ax=ax, width=0.8, cmap='viridis')

    # 在每个条柱的中心位置添加对应的数字
    for p in bar_plot.patches:
        height = p.get_height()
        width = p.get_x() + p.get_width() / 2
        ax.text(width, height + 0.1, f'{height:.2f}', ha="center")

    # 设置图形属性
    ax.set_xlabel('年份')
    ax.set_ylabel('产值（亿元）')
    ax.set_title('2002到2022年浙江地区生产总值变化')
    
    # 设置横坐标文字横向书写
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    plt.show()

    # 显示图形
    plt.show()



#柱线混合图
def query41():#查询青海在2004年至2022年的第二产业增加值及年均增长率，使用柱线混合图表示，标注数值
    # 读取Excel文件
    file_path = './file/地区生产总值统计.xlsx'
    df = pd.read_excel(file_path, sheet_name='第二产业增加值', header=3, index_col='省份')

    # 选择青海的数据并提取2004年至2022年的数据
    province = "青海"
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
    ax2.set_ylabel('第二产业增加值（亿元）', color=color)
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
    plt.title('青海2004年至2022年第二产业增加值及年均增长率')
    plt.show()

def query42():#查询2003年至2022年的全国第三产业增加值及年均增长率，使用柱线混合图表示，标注数值
    # 读取Excel文件
    file_path = './file/地区生产总值统计.xlsx'
    df = pd.read_excel(file_path, sheet_name='第三产业增加值', header=3, index_col='省份')

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
    ax2.set_ylabel('第三产业增加值（亿元）', color=color)
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
    plt.title('全国2003年至2022年第三产业增加值及年均增长率')
    plt.show()

def query43():#查询2012年至2022年的全国第一产业增加值及第一产业增加值在地区生产总值中的占比，使用柱线混合图表示，标注数值
    # 读取Excel文件
    file_path = './file/地区生产总值统计.xlsx'
    df_total = pd.read_excel(file_path, sheet_name='地区生产总值', header=3, index_col='省份')
    df_1 = pd.read_excel(file_path, sheet_name='第一产业增加值', header=3, index_col='省份')

    # 计算全国的数据并提取2012年至2022年的数据
    begin_year='2012年'
    end_year='2022年'
    national_agri_forestry = df_total.sum(axis=0)[begin_year:end_year]
    national_forestry = df_1.sum(axis=0)[begin_year:end_year]

    # 计算第一产业增加值在地区生产总值中的占比
    percentage_forestry_in_agri_forestry = (national_forestry / national_agri_forestry) * 100

    # 绘制柱线混合图
    fig, ax1 = plt.subplots()

    color1 = 'tab:blue'
    ax1.set_xlabel('年份')
    ax1.set_ylabel('第一产业增加值亿元）', color=color1)
    bars1 = ax1.bar(national_forestry.index, national_forestry.values, color=color1, alpha=0.7, label='第一产业增加值')
    ax1.tick_params(axis='y', labelcolor=color1)

    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.set_ylabel('占比（%）', color=color2)
    line2 = ax2.plot(percentage_forestry_in_agri_forestry.index, percentage_forestry_in_agri_forestry.values, color=color2, marker='s', label='占比')
    ax2.tick_params(axis='y', labelcolor=color2)

    # 在每个柱形上标注第一产业增加值
    for bar, value in zip(bars1, national_forestry.values):
        ax1.text(bar.get_x() + bar.get_width() / 2, value,
                 f'{value:.2f}', ha='center', va='bottom', color='black')

    # 在每个数据点上标注占比
    for i, value in enumerate(percentage_forestry_in_agri_forestry.values):
        ax2.text(percentage_forestry_in_agri_forestry.index[i], value,
                 f'{value:.2f}%', ha='center', va='bottom', color='black')

    fig.tight_layout()
    plt.title('全国2012年至2022年第一产业增加值及占比')
    plt.show()

#5+3+4+3
#1+3+2+1+2+2

#修改了堆叠柱状图 增加了堆叠面积图62 63
 
#堆叠柱状图
def query51():#绘制2020年各省份一二三产业增加值的堆叠柱状图，不同类型使用不同颜色表示
    # 读取Excel文件
    file_path = './file/地区生产总值统计.xlsx'
    # 读取一二三产业增加值的数据
    df1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3, index_col='省份')
    df2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3, index_col='省份')
    df3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3, index_col='省份')

    year_2020="2020年"
    # 合并数据
    df_combined = pd.concat([df1[year_2020], df2[year_2020], df3[year_2020]], axis=1)
    df_combined.columns = ['第一产业增加值', '第二产业增加值', '第三产业增加值']

    # 绘制堆叠柱状图
    ax = df_combined.plot(kind='bar', stacked=True, figsize=(12, 8))
    ax.set_title('各省份2020年一二三产业增加值对比')
    ax.set_ylabel('产值（亿元）')

    plt.show()



#堆叠面积图
def query61():#查询2003年至2022年每个省份的地区生产总值变化，以堆叠面积图绘制
    # 读取Excel文件
    file_path = "./file/地区生产总值统计.xlsx"
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
    ax.set_ylabel('地区生产总值')
    ax.set_title('2003年至2022年各省份地区生产总值堆积面积图')
    ax.legend(title='省份', bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()
    
def query62():#查询2003年至2022年陕西一二三产业增加值变化，以增加值的堆叠面积图绘制
    # 读取Excel文件的四个工作表的数据
    filename = "./file/地区生产总值统计.xlsx"
    df1 = pd.read_excel(filename, sheet_name="第一产业增加值", header=3, index_col=0)
    df2 = pd.read_excel(filename, sheet_name="第二产业增加值", header=3, index_col=0)
    df3 = pd.read_excel(filename, sheet_name="第三产业增加值", header=3, index_col=0)

    # 提取陕西的数据
    province = "陕西"
    df_1 = df1.loc[[province], "2003年":"2022年"]
    df_2 = df2.loc[[province], "2003年":"2022年"]
    df_3 = df3.loc[[province], "2003年":"2022年"]

    # 转置数据，使得年份成为行索引
    df_1 = df_1.transpose()
    df_2 = df_2.transpose()
    df_3 = df_3.transpose()

    # 绘制堆积面积图
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.fill_between(df_1.index, 0, df_1.values.flatten(), alpha=0.8, label="第一产业增加值")
    ax.fill_between(df_2.index, df_1.values.flatten(), (df_1 + df_2).values.flatten(), alpha=0.8, label="第二产业增加值")
    ax.fill_between(df_3.index, (df_1 + df_2).values.flatten(), (df_1 + df_2 + df_3).values.flatten(), alpha=0.8, label="第三产业增加值")

    ax.set_xlabel("年份")
    ax.set_ylabel("产值（亿元）")
    ax.set_title("2003年至2022年陕西一二三产业增加值变化堆叠面积图")
    ax.legend()
    plt.xticks(rotation=45)

    plt.show()
    
def query63():#查询2003年至2022年河北河南山东山西四省的地区生产总值变化，以分年度四省总产值的堆积面积图绘制
    # 读取Excel文件的工作表
    file_path = './file/地区生产总值统计.xlsx'
    df1 = pd.read_excel(file_path, sheet_name='地区生产总值', header=3, index_col=0)

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
    ax.set_title('2003年至2022年河北河南山东山西四省地区生产总值变化')

    plt.show()


#热图
def query71():#查询2003年至2022年每个省份的地区生产总值变化率，制作一张热图
    # 读取Excel文件
    file_path = "./file/地区生产总值统计.xlsx"
    df = pd.read_excel(file_path, sheet_name='地区生产总值', header=3, index_col=0)  # 从第四行开始读取，省份作为索引列

    # 提取2003年至2022年的数据
    data_years = df.loc[:, "2003年":"2022年"]

    # 计算每个省份变化率
    change_rate = data_years.pct_change(axis=1) * 100  # 计算百分比变化率

    # print(change_rate.axes)

    # 绘制热图
    plt.figure(figsize=(12, 10))
    sns.heatmap(change_rate, annot=True,cmap="coolwarm",cbar_kws={'label': '变化率'}, annot_kws={'va': 'center', 'ha': 'center'})
    plt.title("2003年至2022年各省份地区生产总值变化率热图")
    plt.show()

def query72():#查询2005年至2022年每个省份的第二产业增加值变化率并制作热图
    # 读取 Excel 文件
    file_path = "./file/地区生产总值统计.xlsx"
    df = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3, index_col=0)

    # 提取2005年至2022年的数据
    data_years = df.loc[:, "2005年":"2022年"]
    # 计算变化率
    df_change = data_years.pct_change(axis=1) * 100

    # 制作热图
    plt.figure(figsize=(12, 8))
    sns.heatmap(df_change, cmap="coolwarm", annot=True, fmt=".2f", linewidths=.5, annot_kws={"size": 8})
    plt.title("2005年至2022年每个省份的第二产业增加值变化率")
    plt.show()



#玫瑰图
def query81():#查询全国各省份在2014年的一二三产业增加值占比，使用玫瑰图表示
    # 读取Excel文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取一二三产业增加值的数据
    df1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3, index_col=0)
    df2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3, index_col=0)
    df3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3, index_col=0)

    # 选择所有省份在2014年的数据
    value1_2014 = df1.loc[:, "2014年"]
    value2_2014 = df2.loc[:, "2014年"]
    value3_2014 = df3.loc[:, "2014年"]

    # 创建堆叠柱状玫瑰图
    theta = np.linspace(0.0, 2*np.pi, len(value1_2014), endpoint=False)
    width = 0.2  # 设置柱状宽度

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_offset(np.pi/2)
    ax.set_theta_direction(-1)

    bars_1 = ax.bar(theta, value1_2014, width=width, label='第一产业增加值')
    bars_2 = ax.bar(theta, value2_2014, width=width, label='第二产业增加值', bottom=value1_2014)
    bars_3 = ax.bar(theta, value3_2014, width=width, label='第三产业增加值', bottom=value1_2014+value2_2014)

    # 添加标签
    ax.set_thetagrids(np.degrees(theta), labels=df1.index)
    ax.legend()

    plt.title("2014年各省一二三产业增加值占比")

    # 显示图形
    plt.show()


#雷达图
def query91():#查询四川在2003年与2022年的一二三产业增加值对比，并制作雷达图：
    # 读取 Excel 文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取一二三产业增加值的数据
    df1 = pd.read_excel(file_path, sheet_name="第一产业增加值", header=3)
    df2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3)
    df3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3)

    
    # 提取四川省在2022年的数据
    df_1_2022 = df1.loc[df1["省份"] == "四川", "2022年"].values[0]
    df_2_2022 = df2.loc[df2["省份"] == "四川", "2022年"].values[0]
    df_3_2022 = df3.loc[df3["省份"] == "四川", "2022年"].values[0]
    
    # 提取四川省在2003年的数据
    df_1_2003 = df1.loc[df1["省份"] == "四川", "2003年"].values[0]
    df_2_2003 = df2.loc[df2["省份"] == "四川", "2003年"].values[0]
    df_3_2003 = df3.loc[df3["省份"] == "四川", "2003年"].values[0]
    
    # 绘制雷达图
    num_industries = 3
    angles = np.linspace(0, 2 * np.pi, num_industries, endpoint=False).tolist()
    angles += angles[:1]  # 闭合图形

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # 2022年的数据
    values_2022 = [df_1_2022, df_2_2022, df_3_2022]
    values_2022 += values_2022[:1]  # 闭合图形
    ax.plot(angles, values_2022, label='2022年')
    ax.fill(angles, values_2022, alpha=0.25)

    # 2003年的数据
    values_2003 = [df_1_2003, df_2_2003, df_3_2003]
    values_2003 += values_2003[:1]  # 闭合图形
    ax.plot(angles, values_2003, label='2003年')
    ax.fill(angles, values_2003, alpha=0.25)

    ax.set_thetagrids(np.degrees(angles[:-1]), ['第一产业增加值', '第二产业增加值', '第三产业增加值'])
    ax.set_title('四川一二三产业增加值对比 (2003年 vs. 2022年)')

    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.show()


def query92():#查询全国在2003年与2022年的地区生产总值各个省份对比，并制作雷达图：
    # 读取 Excel 文件
    file_path = "./file/地区生产总值统计.xlsx"

    # 读取地区生产总值的数据
    df = pd.read_excel(file_path, sheet_name="地区生产总值", header=3, index_col=0)

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
    ax.set_title("2003年与2022年地区生产总值对比", size=14, pad=10)
    ax.legend(loc='upper right')

    # 显示图形
    plt.show()



#散点图
def query101():#查询在2012年至2022年，全国第一产业增加值各省之和与第三产业增加值各省之和之间有什么关系？制作散点图来展示这种关系
    # 读取 Excel 文件
    file_path = './file/地区生产总值统计.xlsx'
    df_1= pd.read_excel(file_path, sheet_name="第一产业增加值", header=3)
    df_3= pd.read_excel(file_path, sheet_name="第三产业增加值", header=3)

    # 提取全国的农业总产值和渔业总产值数据（2012年至2022年）
    years = list(map(str, range(2012, 2023)))
    national_1_total = df_1.sum(axis=0)['2012年':'2022年']
    national_3_total = df_3.sum(axis=0)['2012年':'2022年']
    
    # 创建散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(national_1_total, national_3_total, alpha=0.8)

    # 添加年份标签
    for i, year in enumerate(years):
        plt.annotate(year, (national_1_total[i], national_3_total[i]), fontsize=8)

    plt.title('2012年-2022年全国第一产业与第三产业增加值散点图')
    plt.xlabel('第一产业增加值（亿元）')
    plt.ylabel('第三产业增加值（亿元）')
    plt.grid(True)
    plt.show()



def query102():#查询在2019年，各个省份的第二产业增加值与第三产业增加值之间有什么关系？制作散点图来展示这种关系
    # 读取 Excel 文件
    file_path = './file/地区生产总值统计.xlsx'
    df_2 = pd.read_excel(file_path, sheet_name="第二产业增加值", header=3, index_col='省份')
    df_3 = pd.read_excel(file_path, sheet_name="第三产业增加值", header=3, index_col='省份')

    # 提取各个省份在2019年的二三产业增加值数据
    df_2_2019 = df_2.loc[:, '2019年']
    df_3_2019 = df_3.loc[:, '2019年']

    # 创建散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(df_2_2019, df_3_2019, alpha=0.8)

    # 添加省份标签
    for province in df_2_2019.index:
        plt.annotate(province, (df_2_2019[province], df_3_2019[province]), fontsize=8)

    plt.title('2019年各省份二三产业增加值散点图')
    plt.xlabel('第二产业增加值（亿元）')
    plt.ylabel('第三产业增加值（亿元）')
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    query11()