a={'股票名称': ['股票代码', '股票名称', '当前价', '涨跌额', '涨跌幅', '年初至今成交量', '成交额', '换手率', '股息率', '市值'], 'N晶科': ['SH601778', 'N晶科', '6.29', '+1.92', '+43.94%', '+43.94%', '259.66万', '1625.52万', '0.44%', '22.32', '-', '173.95亿']}
# print(a['股票名称'])

# for i in a['股票名称']:
#     h=a['股票名称'].index(i)
#     print(h)

def catch_info(A,name,key):
    for i in A[key]:
        if i in name:
            h=A[key].index(i)
            return(h)

for t in a.items():
    print(t)
    print(t[1][4])

if '+1.92%'>'+0.88%':
    print('----------')

a='换手率>25'
a=a.replace("换手率>","")
print(a)


print( '1'>'1.92%')


'''
f = open("股票hoomework", "r")
stock_info = {}
for line in f:
    line = line.strip().split(",")
    stock_info[line[1]] = line


# stock_info1=stock_info
# stock_info2=stock_info1.pop('股票名称')
print(stock_info)

def catch_info(A,name,key):
    for i in A[key]:
        if i in name:
            h=A[key].index(i)
            return(h)

while True:
    condition = input("股票查询接口：")
    stock_name = [x[0] for x in stock_info.items() if condition in x[1][1]]
    for i in stock_name:
        print(stock_info[i])
    # break
    #h为查询的目标在字典中值列表的索引
    h=catch_info(stock_info,condition,'股票名称')
    if h>1:
        for t in stock_info.items():
            if t[0]=='股票名称':
                continue
            con1=condition.replace(f"{stock_info['股票名称'][h]}",f"t[1][{h}]")
            if ">" in con1:
                con1 = con1.replace(f"{t[1][h]}>","")
                if float(t[1][h])>float(con1):
                    print(stock_info[t[0]])
            elif "<" in con1:
                con1 = con1.replace(f"{t[1][h]}<", "")
                if float(t[1][h]) < float(con1):
                    print(stock_info[t[0]])
            elif "=" in con1:
                con1 = con1.replace(f"{t[1][h]}=", "")
                if float(t[1][h]) == float(con1):
                    print(stock_info[t[0]])
'''

def str2value(valueStr):
    valueStr = str(valueStr)
    idxOfYi = valueStr.find('亿')
    idxOfWan = valueStr.find('万')
    idxOfbai=valueStr.find('%')
    idxOfp=valueStr.find('+' or '-')
    if idxOfbai != -1:
        return float(valueStr[:idxOfbai])
    elif idxOfYi != -1 :
        return float(valueStr[:idxOfYi])
    elif  idxOfWan != -1:
        return float(valueStr[:idxOfWan])
    elif idxOfYi == -1 and idxOfWan == -1:
        return float(valueStr)
    elif idxOfp!=-1:
        return float(valueStr[1:idxOfWan])

print(str2value('+1.76'))
