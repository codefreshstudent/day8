# ----encoding='utf-8'-----
#   Chentian's code paradise
import smtplib
import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

mail_host="smtp.163.com"
mail_sender="chentstudent@163.com"
mail_slience=""
mail_receivers=["2627601379@qq.com"]

mm=MIMEMultipart('related')

subject_content="""python邮件测试"""
mm["From"]="sender_name<chentstudent@163.com>"
mm["to"]="receiver_name<2627601379@qq.com>"

mm["subiect"]=Header(subject_content,"utf-8")

body_content="""你好，这是一个测试邮件，来自于陈添"""

message_text=MIMEMultipart(body_content,"plian","utf=8")

mm.attach(message_text)

imagine_data=open("FILE-20150725-1818LV48VS71BW2J.jpg","rb")

message_imagine=MIMEImage(imagine_data.read())

imagine_data.close()

mm.attach(message_imagine)

exc=MIMEText(open("大唐建设集团-2022年5月工资.xlsx","rb").read(),'base64','utf-8')

exc["Content-Disposition"]='attachment;filename="sample.xlex"'

mm.attach(exc)

stp=smtplib.SMTP()

stp.connect(mail_host,25)

stp.set_debuglevel(1)

stp.login(mail_sender,mail_license)

stp.sendmail(mail_sender, mail_receivers, mm.as_string())
print("邮件发送成功")
stp.quit()



