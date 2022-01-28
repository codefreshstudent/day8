import random
import string

trueage=26

# 猜年龄
# for i in range(20):
#     guess_age = int(input("guess_age"))
#     if guess_age==trueage:
#         exit("configtrions you guess righe")
#     elif guess_age<trueage:
#         print("没有这么年轻")
#     else:
#         print("也没有这么老")

# 打印偶数
for j in range(101):
    if j%2==0:
        print(f"{j}偶数")

# 打印楼层
for i in range(1,6):
    if i==3:
        continue
    print(f"----------------第{i}层-------------")
    for j in range(1,21):
        if i==4 and j==4:
            print("遇到鬼屋了")
            break #结束当前循环
        print(f"L{i}-{i}0{j}")

for i in range(10):
    if i<=5:
        print("*"*i)
    else:
        print("*"*(10-i))


count=0
while count<10:
    count+=1
    guess_age = int(input("guess_age"))
    if guess_age==trueage:
        print("configtrions you guess righe")
        break
    elif guess_age<trueage:
        print("没有这么年轻")
    else:
        print("也没有这么老")

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()

# print 后会自动加一个换行符
for i in range(1,10): # 3
    #print(f"{i}x1={i*1}")
    for j in range(1,i+1):
        print(f"{i}x{j}={i*j}",end=" ")
    print()
# 北京市车牌摇号程序
a=string.ascii_uppercase+string.digits

b=string.ascii_uppercase
count=0
car_nums=[]
while count<3:
    for i in range(21):
        a1 = random.choice(b)
        b1 = random.sample(a, 5)
        c1="".join(b1)
        car_num=f"京{a1}-{c1}"
        car_nums.append(car_num)
    print(car_nums,end="\n")
    choice=input("输入你选中的号码：")
    if choice in car_nums:
        print("恭喜你选中")
    else:
        print("输入不合法")

    count+=1

t=a.strip("jing   pppop")
print(t)




def fun(a,b):
    c=a/b
    print(c)
