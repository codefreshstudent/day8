import re
s="sdhgsidgsjdg7868asdciau98wy"
#+的意思是一个或多个
w=re.split("[0123456789]+",s)
u=re.split("[0123456789]+",s)
print(w,u)

# 这是修改哦错误
# try:
#     filter_val=float(filter_val)
# except ValueError:
#     continue
p="最近比较时有时，线条要学金克斯的公司的267493847938@qq.com,谢谢"

print(re.search(r'(\w)+@(\w)+.\w+',p,flags=re.A))