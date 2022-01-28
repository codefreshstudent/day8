# ----encoding='utf-8'-----
#   Chentian's code paradise
import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_obj=smtplib.SMTP_SSL("smtp.qq.com",465)
smtp_obj.login("2627601379@qq.com","hnzjmgwmcmoqdjec")
smtp_obj.set_debuglevel(1)
#设置邮件内容
msg=MIMEText("你好这是一封测试邮件","plain","utf-8")

msg["From"]=Header("来自陈添的问候2022","utf-8")
msg["To"]=Header("有缘人2022","utf-8")
msg["Subject"]=Header("陈添的信","utf-8")

smtp_obj.sendmail("2627601379@qq.com","chentstudent@163.com",msg.as_string())

