import re

# 1. 程序启动后，给用户提供查询接口，允许用户**重复查**股票行情信息。
stock_dic = {}
f = open("stock_data.txt", encoding="utf-8")

headers = f.readline().strip().split(",")

for line in f:
    line = line.strip().split(",")
    stock_dic[line[0]] = line

f.close()

# for i, j in stock_dic.items():
#     print(i,j)

while True:
    cmd = input("请输入要查询的股票指令：")

    for s_id, s_data in stock_dic.items():
        s_name = s_data[1]
        # print(headers)
        if cmd in s_name:
            print(s_data)



# 2. 允许用户通过**模糊查询**股票名，比如输入“啤酒”,
# 就把所有名称当中包含啤酒的股票都打印出来。


# 3. 允许按 **当前价、涨跌幅、换手率**这几列来筛选信息
# ，比如输入**“当前价>50**”则把价格大于50的股票都打印，
# 输入“**涨跌幅<50**“，则把涨跌幅小于50的股票都打印，不用判断等于。

# 判断公式是否合法（正则表达式）
    cmd_parser = re.split("[<>]" ,cmd)
    if len(cmd_parser) != 2:
        continue
# 判断列名是否合法
    filter_column, filter_val = cmd_parser
    if filter_column not in ["当前价", "涨跌幅", "换手率"]:
        continue
# 判断数值的合法性
    try:
        filter_val = float(filter_val)
    except ValueError:
        continue
# 根据列名，拿到想要查的列的索引
    column_index = headers.index(filter_column)
    for s_id, s_data in stock_dic.items():
        if ">" in cmd:
            if float(s_data[column_index].strip("%")) > filter_val:
                print(s_data)
        else:
            if float(s_data[column_index].strip("%")) < filter_val:
                print(s_data)
