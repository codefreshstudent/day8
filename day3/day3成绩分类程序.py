#成绩分组小程序
stu_list = [['李渊', 82], ['李世民', 7], ['侯君集', 5], ['李靖', 58], ['魏征', 41], ['房玄龄', 64], ['杜如晦', 65],
            ['柴绍', 94], ['程知节', 45], ['尉迟恭', 94], ['秦琼', 54], ['长孙无忌', 85], ['李存恭', 98], ['封德彝', 16],
            ['段志玄', 44], ['刘弘基', 18], ['徐世绩', 86], ['李治', 19], ['武则天', 39], ['太平公主', 57], ['韦后', 76],
            ['李隆基', 95], ['杨玉环', 33], ['王勃', 49], ['陈子昂', 91], ['卢照邻', 70], ['杨炯', 81], ['王之涣', 82], ['安禄山', 18],
            ['史思明', 9], ['张巡', 15], ['雷万春', 72], ['李白', 61], ['高力士', 58], ['杜甫', 27], ['白居易', 5], ['王维', 14], ['孟浩然', 32],
            ['杜牧', 95], ['李商隐', 34], ['郭子仪', 53], ['张易之', 39], ['张昌宗', 61], ['来俊臣', 8], ['杨国忠', 84], ['李林甫', 95], ['高适', 100],
            ['王昌龄', 40], ['孙思邈', 46], ['玄奘', 84], ['鉴真', 90], ['高骈', 85], ['狄仁杰', 62], ['黄巢', 79], ['王仙芝', 16], ['文成公主', 13],
            ['松赞干布', 47], ['薛涛', 79], ['鱼玄机', 16], ['贺知章', 20], ['李泌', 17], ['韩愈', 100], ['柳宗元', 88], ['上官婉儿 五代十国：朱温', 55],
            ['刘仁恭', 6], ['丁会', 26], ['李克用', 39], ['李存勖', 11], ['葛从周', 25], ['王建', 13], ['刘知远', 95], ['石敬瑭', 63], ['郭威', 28],
            ['柴荣', 50], ['孟昶', 17], ['荆浩', 84], ['刘彟', 18], ['张及之', 45], ['杜宇', 73], ['高季兴', 39], ['喻皓', 50], ['历真', 70],
            ['李茂贞', 6], ['朱友珪', 7], ['朱友贞', 11], ['刘守光', 2]]
A=[]
B=[]
C=[]
D=[]
F=[]
for i in stu_list:
    if 100>=i[1]>=90:
        A.append(i)
    elif 90>i[1]>=80:
        B.append(i)
    elif 80>i[1]>=70:
        C.append(i)
    elif 70>i[1]>=60:
        D.append(i)
    else:
        F.append(i)

congree=[A,B,C,D,F]
print(congree)

mes = {
 "alex": [23, "CEO", 66000],
 "⿊姑娘": [24, "⾏政", 4000],
}

mes["陈添"]=[23,"CEO",1000000]


mes.pop("alex")
print(mes)
#字典不能切片，不能查value

mes.keys

t=mes.items()
for k,v in t:   ##返回⼀个包含所有（键，值）元组的列表 对于元组中的元素可以直接循环两种变量
    print(v)

for k in mes:  #推荐用这种小效率最高
    print(k,mes[k])






