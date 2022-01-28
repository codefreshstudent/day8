

# 字符串操作 字符串不可变 列表与字典都可变
a="chentian  day3"
# print(a.center(50,"-"))
#
# print(a.count("c",0,2))
#
# print(a.endswith("3"))
#
# print(a.startswith("v"))
#
# print(a.find("p")) #找到返回索引，没找到-1，找到返回索引
#
# print(a.isdigit())
# print("99".isdigit())
#
# l=["chentian ","is","a good boy"]
# print(" ".join(l))

print(a.replace("chentian","chenguangli"))

print(a.split()) #split()括号中的值是按照什么来分割，后面可以指定参数-

#列表操作
b=["chentian","alex"]

b.append("wangchunmei")
print(b)

b.insert(2,"dawang")
print(b)

b.insert(2,[1,2,3])
print(b)

#使用列表嵌套

b[2][1]="陈**" #列表嵌套取值
print(b)

b.extend(a)
print(b)

# a.pop删除索引 a.remove删除名字
#a.index“要查找的名字” 查找索引 a.count("要查找个数的名字")

#字符串切片操作n.[1；n]包括左边不包括右边、顾头不顾尾

# 列表循环
# n=[3,4,5,6,4,23,5,3,5,3,54]
#
# for i in n:
#     print(i)
#
# for i in enumerate(n):
#     print(i)












