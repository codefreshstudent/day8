# ----encoding='utf-8'-----
#   Chentian's code paradise

import smtplib as smtp
from openpyxl import load_workbook
from email.mime.text import MIMEText
from email.header import Header

smtp_obj=smtp.SMTP_SSL('smtp.qq.com',465)
smtp_obj.login('2627601379@qq.com','hnzjmgwmcmoqdjec')
smtp_obj.set_debuglevel(1)

msg=MIMEText("这是您的工资条","plain","utf-8")

wb=load_workbook("大唐建设集团-2022年5月工资.xlsx",data_only=True)



msg['From']=("大唐建设集团","utf-8")
msg['To']=("")

