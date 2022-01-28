# 文件操作流程，创建，只读，追加，遍历，二进制，混合，修改
#只写模式操作文件
# f=open("name_list",mode="w")
#
# f.write("陈添\n")
# f.write("陈广利\n")
#
# f.close()


#只读模式操作文件
# f=open("name_list",mode="r")
# # print(f.read())
#
# print(f.readline())
# f.close()

#文件追加操作
# f=open("name_list","a")
#
# f.write("王春梅\n")
# f.write("python\n")
# f.close()




#wb二进制写 rb二进制读 ab二进制追加
# f=open("1589450091035.jpg","rb")
# for i in f:
#     print(i)
#
# f1=open("eb_eb","wb")
# s="陈添"
# f1.write(s.encode("gbk"))



#遍历联系方式
# f=open("name_list","w")
# for line in f:
#     line=line.split()
#     height=int(line[3])
#     weight=int(line[4])
#     if height>170 and weight<50:
#         print(line)

















