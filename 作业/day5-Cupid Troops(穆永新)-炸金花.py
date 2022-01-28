import random

suit = ["梅花", "方片", "红桃", "黑桃"]
number = ['A', "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
all = []
for i in range(4):
    for j in range(12):
        all.append(suit[i] + number[j])
print(all)
result = {}


def fapai(all, *args):
    random.shuffle(all)
    k = 0
    p = 3
    if len(args) > 17:
        print("玩家数量太多！最多十七人玩！")
    else:
        for j in args:
            result[j] = all[k:p]
            k = k + 3
            p = p + 3
        return result


print(fapai(all, "alex", "chentian", "dgwigdiu"))
