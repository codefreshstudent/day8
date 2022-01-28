import random

suit=["梅花","方片","红桃","黑桃"]
number=['A',"2","3","4","5","6","7","8","9","10","J","Q","K"]
all=[]
for i in range(4):
    for j in range(12):
        all.append(suit[i]+number[j])
print(all)
result={}

random.shuffle(all)
print(all)

# def fapai(a,b,c,all):
#     h=[]
#     p=[]
#     o=[]
#     result={}
#     while len(h)!=9:
#         for i in range(9):
#             p = random.randint(0, 52)
#             if p not in [h]:
#                 h.append(p)
#     for k in h:
#         o.append(all[k])
#     result[a]=o[0:3]
#     result[b]=o[3:6]
#     result[c]=o[6:9]
#     return result
#
# print(fapai("alex","muyongxin","tgwusg",all))

