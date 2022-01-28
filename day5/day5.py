#关键参数与位置参数，关键参数必须放在位置参数后面，指定值就是关键参数
def stu_re(**kwargs):
    print("-----------info------")
    print("Nmae:",kwargs.get('Name'))
    print("age:",kwargs.get('age'))
    print("sex:",kwargs.get('sex'))
    print("hobbie:",kwargs.get('hobbie'))

stu_re(name='陈添',age=23,sex='M',hobbie='money')

name='chen tian'
def change_name():
    name="大家好我是 name"
    print("after change",name)

change_name()
print("看看改没改",name)

#abs()取绝对值
a=[0,2,3,4,5,6]
print(any(a))
print(all(a))
#打印地址
print(__file__)

#打印当前作用域的所有的变量名与变量值locals()

l=list(range(10))
print(l)
def cal(x):
    return x**2

m=map(cal,l)
for i in m:
    print(i)

w=3.14156789876
print(round(w,4))


