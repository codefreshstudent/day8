# ----encoding='utf-8'-----
#   Chentian's code paradise
import requests
import re
import bs4

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
    }
page_obj=requests.get("https://www.douban.com/group/topic/39910632/?_i=3022755Uk-a_oU,3025296Uk-a_oU",headers=headers)

bs4_obj=bs4.BeautifulSoup(page_obj.text,"html.parser")
'''
find与find_all方法的不同是find_all返回的是文档中所有符合要求的标签列表形式，
find是直接返回结果

'''
comment_obj=bs4_obj.find_all("div",attrs={"class":"reply-doc"})


page_obj=bs4_obj.find("div",attrs={"class":"paginator"})
for j in page_obj.find_all("a"):
    page_num=j.attrs.get("href")
    print(j)


print(len(comment_obj))
mail_list=[]
for i in comment_obj:
    mail_adr=i.find("p",attrs={"class":"reply-content"})
    # print(mail_adr.text)
    mail_num=re.search(r'(\w)+@(\w)+.\w+',str(mail_adr),flags=re.A)
    if mail_num:
        pub_tim=i.find("span",attrs={"class":"pubtime"})
        mail_list.append([mail_num.group(),pub_tim.text])
print(mail_list)





