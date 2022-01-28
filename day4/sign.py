'''
要求用户输入账号密码
用户信息保存在文件里
用户密码输入三次后锁定用户，下次再登录不容许登录提示被锁

'''

# 问题：打开文件之后往里存储时是否该用循环存？应该怎么保存不同用户的账号密码，光标位置应该如何定位？
'''
关于怎么保存不同的用户密码的问题可以随意，因为只要在程序里可以实现切割分离就可以
'''
# 开始看视频
# 1.决定存储账号信息的结构 用户名，密码，锁定状态,读文件


f = open("account_key", "r")
accounts = {}
for line in f:
    line = line.strip().split(",")
    accounts[line[0]] = line
print(accounts)

# 2.给一个锁定状态

while True:
    user = input("请输入你的用户名：").strip()
    if user not in accounts:
        print("用户未注册 ")
        continue
    elif accounts[user][2] == '1':
        print("此账户已锁定请联系管理员")
        continue

    count = 0
    while count < 3:
        passwd = input("请输入你的密码：").strip()
        # 去账号密码字典判断
        if passwd == accounts[user][1]:
            print(f"{user}欢迎登陆！")
            exit("By By")
        else:
            print("密码错误！")
        count += 1
    if count == 3:
        print(f"输错了三次密码，需要锁定账号{user}")
        # 1.先改内存中的用户状态
        # 2.把dict里的数据转成原数据格式存储
        accounts[user][2] = '1'
        f2 = open("account_key", "w")
        for user, val in accounts.items():
            line = ",".join(val) + "\n"
            f2.write(line)
        f2.close()
        exit("By,By")

# user_aaccount=input("你的账号是（请输入正确的的手机号）：")
# user_key=input("你要设置的密码是：")
# print(f"你的密码是：{user_key}")
# a=input("确认你的密码吗，请输入Y orN: ")
# if a=='Y':
#     user_key=user_key
# else:
#     user_key=input("请输入新密码")
