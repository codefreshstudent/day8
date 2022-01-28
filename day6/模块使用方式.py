import os
import sys
#遍历文件目录
print(os.getcwd())
'''
以列表形式返回所有文件
用python编写了一个工程，但在第一次运行后，发现工程根目录下生成了一个__pycache__文件夹,里面是和py文件同名的各种以.cpython-35.pyc结尾的文件。
cpython-35各项意义，cpython代表的是c语言实现的Python解释器，-35代表的是3.5版本。至于pyc，需要先了解一下模块的调用。
Python导入模块时，实际上会把被导入的模块执行一遍。例如调用test.py模块：
def haha():
  print("haha")
 
haha()

主程序main.py：

1
2
3
import test
 
print("good")
执行结果：

haha
good
如何才能只是单纯调用而不执行被调用模块的代码呢？
要想被调用模块代码不被执行，可以使用__name__。如果不涉及模块导入，__name__的值就是__main__，如果模块被导入引用的话，
那么这个模块内的__name__值就是文件的名字（不带.py），例如test.py：
def haha():
  print("haha")
 
haha()
print(__name__)
执行结果为：

haha
__main__
如果test被导入引用的话，例如test2：

在被调用的模块中，可执行代码前加上if __name__ == '__main__':这么一句判断，被调用的模块的代码就不会被执行。

由来
Python程序运行时不需要编译成二进制代码，而直接从源码运行程序。简单来说是，Python解释器将源码转换为字节码，然后再由解释器来执行这些字节码。

解释器的具体工作：

1、完成模块的加载和链接；
2、将源代码编译为PyCodeObject对象(即字节码)，写入内存中，供CPU读取；
3、从内存中读取并执行，结束后将PyCodeObject写回硬盘当中，也就是复制到.pyc或.pyo文件中，以保存当前目录下所有脚本的字节码文件。

之后若再次执行该脚本，它先检查【本地是否有上述字节码文件】和【该字节码文件的修改时间是否在其源文件之后】，是就直接执行，否则重复上述步骤。
'''
print(os.listdir())
# os.remove("testre.py")

a=os.path.abspath("模块使用方式.py")

print(a)

os.system("ipconfig")
b=os.path.basename("模块使用方式.py")
print(b)
#获取系统环境变量
sys.path
#获取脚本参数
sys.argv



















