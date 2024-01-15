import pandas as pd
import numpy as np  

# '''
# 背景知识：r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\民用汽车拥有量汇总.xlsx"文件中
# 共有4个独立的sheet，分别为“民用汽车拥有量汇总”、“民用载货”、“民用载客”、“民用其他”。
# “民用汽车拥有量汇总”的列名从第5行开始，“民用载货”、“民用载客”的列名从第4行开始，
# 列名有省份、2002年、2003年……一直到2020年等项，不存在汇总各个省份的全国项。
# 单位为万辆，根据下列查询要求，输出实现代码。
# '''



def querySI01():#2016年，北京和天津的民用汽车拥有量分别是多少？
    file_path=r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\民用汽车拥有量汇总.xlsx"
    data = pd.read_excel(file_path, sheet_name='民用汽车拥有量汇总', engine='openpyxl', header=4)  # 从第五行开始读取数据

    # 要查询的城市和年份
    city_1 = '北京'  # 可以根据需要修改为其他城市
    city_2 = '天津'  # 可以根据需要修改为其他城市
    year_to_check = '2016'  # 可以根据需要修改为其他年份

    # 获取特定城市在特定年份的民用汽车拥有量
    car_count_city_1 = data.loc[data['省份'] == city_1, f'{year_to_check}年'].values[0]
    car_count_city_2 = data.loc[data['省份'] == city_2, f'{year_to_check}年'].values[0]

    print(f"{year_to_check}年，{city_1}的民用汽车拥有量为：{car_count_city_1} 万辆")
    print(f"{year_to_check}年，{city_2}的民用汽车拥有量为：{car_count_city_2} 万辆")


def querySI02():#海南省2008年、2013年、2018年的民用汽车拥有量分别是多少？
    file_path=r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\民用汽车拥有量汇总.xlsx"
    data = pd.read_excel(file_path, sheet_name='民用汽车拥有量汇总',engine='openpyxl', header=4)  # 从第五行开始读取数据

    # 要查询的省份和年份列表
    province = '海南'
    years_to_check = ['2008', '2013', '2018']

    for year in years_to_check:
        car_count = data.loc[data['省份'] == province, f'{year}年'].values[0]
        print(f"{year}年，{province}的民用汽车拥有量为：{car_count} 万辆")

def querySI03():#2010年，民用载货汽车拥有量最多的省份是哪个？
    file_path=r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\民用汽车拥有量汇总.xlsx"
    data = pd.read_excel(file_path, sheet_name='民用载货',engine='openpyxl', header=3)  # 从第四行开始读取数据

    # 获取2010年民用载货汽车拥有量最多的省份
    year_to_check = '2010'
    max_car_province = data.loc[data[year_to_check + '年'].idxmax(), '省份']

    print(f"{year_to_check}年，民用载货汽车拥有量最多的省份是：{max_car_province}")

def querySI04():#2007年，民用载货汽车拥有量最少的省份是哪个？
    file_path = r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\民用汽车拥有量汇总.xlsx"
    data = pd.read_excel(file_path, sheet_name='民用载货', engine='openpyxl', header=3)  # 从第四行开始读取数据

    # 获取2007年民用载货汽车拥有量最少的省份
    year_to_check = '2007'
    min_car_province = data.loc[data[year_to_check + '年'].idxmin(), '省份']

    print(f"{year_to_check}年，民用载货汽车拥有量最少的省份是：{min_car_province}")

def querySI05():#河南省民用载客汽车拥有量最多的年份是哪一年？
    file_path = r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\民用汽车拥有量汇总.xlsx"
    data = pd.read_excel(file_path, sheet_name='民用载客', engine='openpyxl', header=3)  # 从第四行开始读取数据

    # 获取河南省民用载客汽车拥有量最多的年份
    province = '河南'
    an_hui_data = data.loc[data['省份'] == province]

    max_year_index = an_hui_data.iloc[0, 1:].astype(float).idxmax()
    # max_year_index = max_year_index.replace('年', '')  # 去掉 "年" 字符
    # print(max_year_index)
    # max_year = an_hui_data.columns[int(max_year_index)]
    # print(max_year)
    #max_year = max_year.replace('年', '')  # 去掉 "年" 字符
    #max_year = int(max_year)  # 转换为整数类型
    print(f"{province}省民用载客汽车拥有量最多的年份是：{max_year_index}")

    # max_year_index = an_hui_data.iloc[0, 1:].astype(float).idxmax()
    # max_year = an_hui_data.columns['max_year_index']
    # print(f"{province}省民用载客汽车拥有量最多的年份是：{max_year}年")


# '''
# 背景知识:r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\农林牧渔业总产值.xlsx"文件中的农林牧渔业总产值、农业、林业、牧业和渔业产值共计五张独立的sheet，列名都从第四行开始
# 列名有省份、2003年、2003年……一直到2022年等项,不存在汇总各个省份的全国项。产值单位为亿元，根据下列查询要求，输出实现代码
# '''

def querySI16():#2013年，林业总产值最少和倒数第二少的省份分别是哪个？
    file_path = r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\农林牧渔业总产值.xlsx"
    data = pd.read_excel(file_path, sheet_name='林业', engine='openpyxl', header=3)

    # 获取2013年林业总产值最少和倒数第二少的省份
    year_to_check = '2013'

    # 找到最少和倒数第二少的值
    min_values = data[year_to_check + '年'].nsmallest(2).values

    # 找到对应省份
    min_provinces = data[data[year_to_check + '年'].isin(min_values)]['省份'].values
    #print(min_provinces)
    print(f"{year_to_check}年，林业总产值最少的省份是：{min_provinces[1]}，倒数第二少的省份是：{min_provinces[0]}")

def querySI17():#2015年，所有省份的牧业总产值总和为多少元？
    file_path = r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\农林牧渔业总产值.xlsx"
    data = pd.read_excel(file_path, sheet_name='牧业', engine='openpyxl', header=3)

    # 获取2015年所有省份的牧业总产值总和
    year_to_check = '2015'

    total_agri_value_2015 = data[year_to_check + '年'].sum()

    print(f"{year_to_check}年，所有省份的牧业总产值总和为：{total_agri_value_2015} 亿元")


def querySI18():#2009年，是否存在牧业总产值为792.08亿元的省份？如果有，是哪个省？
    file_path = r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\农林牧渔业总产值.xlsx"
    data = pd.read_excel(file_path, sheet_name='牧业', engine='openpyxl', header=3)

    # 检查是否存在2008年牧业总产值为792.08亿元的省份
    year_to_check = '2009'
    target_value = 792.08

    provinces_with_target_value = data.loc[data[year_to_check + '年'] == target_value, '省份']

    if not provinces_with_target_value.empty:
        print(f"{year_to_check}年，存在牧业总产值为{target_value}亿元的省份，分别是：")
        print(provinces_with_target_value.to_string(index=False))  # 去掉索引信息
    else:
        print(f"{year_to_check}年，不存在牧业总产值为{target_value}亿元的省份")


def querySI19():#是否存在渔业总产值为415.45亿元的省份和年份？如果有，是哪一年和哪个省？
    file_path = r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\农林牧渔业总产值.xlsx"
    data = pd.read_excel(file_path, sheet_name='渔业', engine='openpyxl', header=3)

    # 检查是否存在渔业总产值为415.45亿元的省份和年份
    target_value = 415.45

    provinces_years_with_target_count = data.iloc[:, 1:].eq(target_value)

    # 找到特定值的索引位置
    indices = np.where(provinces_years_with_target_count)

    if len(indices[0]) > 0:
        rows, cols = indices
        provinces = data.iloc[rows, 0].values  # 获取行名
        years = data.columns[cols + 1]  # 获取列名，需加1以匹配实际列索引
        print(f"存在渔业总产值为{target_value}亿元的省份和年份，分别是：")
        for province, year in zip(provinces, years):
            print(f"省份：{province}，年份：{year}")
    else:
        print(f"不存在渔业总产值为{target_value}亿元的省份和年份")

def querySI20():#贵州省是否有哪一年的渔业总产值为57.7亿元？如果有，是哪一年？
    file_path = r"C:\Users\86186\ShareCache\张少彤_2000017739\大四上学期\机器学习基础\大作业\农林牧渔业总产值.xlsx"
    data = pd.read_excel(file_path, sheet_name='渔业', engine='openpyxl', header=3)

    # 检查贵州省是否有渔业总产值为57.7亿元的年份
    province = '贵州'
    target_value = 57.7

    years_with_target_value = data.loc[data['省份'] == province].iloc[:, 1:].eq(target_value).any()

    if years_with_target_value.any():
        target_years = years_with_target_value.index[years_with_target_value].str.replace('年', '')
        print(f"{province}省存在渔业总产值为{target_value}亿元的年份，分别是：")
        print(f"{target_years[0]}年")
    else:
        print(f"{province}省不存在渔业总产值为{target_value}亿元的年份")


if __name__=='__main__':
    querySI20()



