f = open("stock_data", "r+")
# 1.加载到内存
data = f.read()  # 从硬盘加载到内存中进行更改
new_data = data.replace("吉贝尔", "路飞学城")
# 2.清空文件
f.seek(0)
f.truncate()  # 截断文件
# 3.重写文件
f.write(new_data)
print(f)

f.close()

# 因为python不能从内存中直接保存的功能所以就没有办法在内存中修改了之后直接保存到硬盘中如下例子stock_datatest就没有保存
h = open("stock_datatest", "r+")
# 1.加载到内存
data = h.read()  # 从硬盘加载到内存中进行更改
data.replace("吉贝尔", "路飞学城")
print(data.replace("吉贝尔", "路飞学城"))
h.close()
