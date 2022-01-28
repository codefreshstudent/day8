
def input_in():
    x=["python","Linux","网络安全","前端","数据分析"]
    a1="----------------------"
    a_name=input("请输入您的姓名:")
    a_age=input("请输入您的年龄：")
    a_phone=input("请输入您的手机号：")
    a_id=input("请输入您的身份证号：")
    a_course=input("输入您选的课程：")
    a3="-------------------------"
    f = open("学员信息", "a+", encoding="utf-8")
    if a_course not in x:
        print("您选择的课程不合法")
    else:
        data=[a1,a_name,a_age,a_phone,a_id,a_course,a3]
        for i in data:
            f.write(f"{i}\n")
    f.close()




while True:
    input_in()

