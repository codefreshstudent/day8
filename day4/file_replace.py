import sys

# print(sys.argv)
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]

# 1 读取文件至内存中
f = open(filename, "r+")
data = f.read()
new_data = data.replace(old_str, new_str)
old_count = data.count(old_str)

# 2清空文件
f.seek(0)
f.truncate()

# 3写入文件
f.write(new_data)
print(new_data)
f.close()

print(f"{old_str}被替换为{new_str},共被替换{old_count}次")
