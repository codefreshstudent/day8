# ----encoding='utf-8'-----
#   Chentian's code paradise

import requests
import bs4
import re

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
page_obj=requests.get("https://www.douban.com/group/topic/199847619/?_dtcc=1&_i=2985152Uk-a_oU",headers=headers)

bs4_obj=bs4.BeautifulSoup(page_obj.text,"html.parser")

comment_date=bs4_obj.find_all("div",attrs={"class":"reply-doc"}) #find_all返回列表元素
print(len(comment_date))
mail_list=[]
for i in comment_date:
    comment_ele=i.find('p',attrs={"class":"reply-content"})
    # print(comment_ele.text)
    email_adr=re.search(r'(\w)+@(\w)+.\w+', str(comment_ele),flags=re.A)
    if email_adr:
        pub_time=i.find("span",attrs={'class':"pubtime"})
        # print(email_adr.group(),pub_time.text)
        mail_list.append([email_adr.group(),pub_time.text])

print(mail_list)