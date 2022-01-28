# 八天训练营第二次作业

# 1.打开文件按照规定格式进行分割字典
f = open("股票hoomework", "r")
stock_info = {}
for line in f:
    line = line.strip().split(",")
    stock_info[line[1]] = line
print(stock_info)

f.close()#要特别注意要关，有可能在第二次第三次出现稀奇古怪的错误
# 抓取需要返回的信息值索引
def catch_info(A, name, key):
    for i in A[key]:
        if i in name:
            h = A[key].index(i)
            return (h)


# 将数据统一转化为浮点型进行处理
def str2value(valueStr):
    valueStr = str(valueStr)
    idxOfYi = valueStr.find('亿')
    idxOfWan = valueStr.find('万')
    idxOfbai = valueStr.find('%')
    idxOfp = valueStr.find('+' or '-')
    if idxOfbai != -1:
        return float(valueStr[:idxOfbai])
    elif idxOfYi != -1:
        return float(valueStr[:idxOfYi])
    elif idxOfWan != -1:
        return float(valueStr[:idxOfWan])
    elif idxOfYi == -1 and idxOfWan == -1:
        return float(valueStr)
    elif idxOfp != -1:
        return float(valueStr[1:idxOfWan])

#2.开始进行条件查找
while True:
    count = 0
    condition = input("股票查询接口：")
    #只要需要用户输入要判断公式是否输入合法
    stock_name = [x[0] for x in stock_info.items() if condition in x[1][1]]
    for i in stock_name:
        print(stock_info[i])
        count = count + 1
    print(f"找到{count}条")
    # break
    # h为查询的目标在字典中值列表的索引
    h = catch_info(stock_info, condition, '股票名称')
    g = 1
    while g < 11:
        if g == h:
            print(stock_info['股票名称'])
            for t in stock_info.items():
                con1 = condition.replace(f"{stock_info['股票名称'][h]}", "")
                if t[0] == '股票名称':
                    continue
                if ">" in condition:
                    con1 = con1.replace(">", "")
                    if str2value(con1) < str2value(t[1][h]):
                        print(stock_info[t[0]])
                        count = count + 1
                if "<" in condition:
                    con1 = con1.replace("<", "")
                    if str2value(con1) > str2value(t[1][h]):
                        print(stock_info[t[0]])
                        count = count + 1
            print(f"找到{count}条")
            g = g + 1
        else:
            g = g + 1
