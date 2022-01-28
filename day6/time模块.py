# ----encoding='utf-8'-----
#   Chentian's code paradise

'''
时间戳1970年1月1日以后是时间戳
格式化时间字符串
'''

import time
import datetime
print(time.time()) #返回当前时间戳

print(time.localtime()) #返回元组格式的时间信息 当前时区

print(time.gmtime())#返回当前时间，格林威治时间

print(time.mktime(time.gmtime()))#转回去

print(time.strftime("%Y-%m-%d %X %p %a"))#后面%X，可换为%H:%M:%S

print(datetime.datetime.now())
#时间运算
now_time=datetime.datetime.now()
print(now_time+datetime.timedelta(+5,hours=5))

#时间替换
print(now_time.replace(year=2300,month=7))