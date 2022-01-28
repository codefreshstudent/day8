# # # 集合 set  无序的， 不重复
# #
# #
# # set1 = {1, 2, 3}
# #
# # five_men_fight_bg = {"Alex", "佩奇", "村长", "pyyu", "Old Shang", "black girl"}
# # happy_day = {"唐艺昕", "李孝利", "black girl", "刘诗诗", "李沁", "柳岩", "Old Shang"}
# #
# # # 1，找出，同时参演了这两部电影的人都有谁（交集）
# # print(five_men_fight_bg.intersection(happy_day))
# # print(five_men_fight_bg & happy_day)
# #
# # # 2，这两部电影中，一共包含了有哪些演员(并集)
# # print(five_men_fight_bg.union(happy_day))
# # print(five_men_fight_bg | happy_day)
# #
# # # 3，参演了抗战片，五男大战黑姑娘的演员中，谁没有参演开心的一天
# # print(five_men_fight_bg.difference(happy_day))
# # print(five_men_fight_bg - happy_day)
# #
# # # 4，哪些演员，只参演了一部电影
# # print(five_men_fight_bg.symmetric_difference(happy_day))
# # print(five_men_fight_bg ^ happy_day)
# #
# # # print(five_men_fight_bg[0])
# # set1 = {1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 3, 3, 34, 4}
# # print(set1)
# #
# # lis1 = [23, 23, 23, 23, 3, 3, 4, 34, 3, 4]
# # lis1 = list(set(lis1))
# # print(lis1)
#
# # 流程控制结构
# # 顺序结构
# # 选择结构 分支结构 条件语句
# # 循环结构
# flag = True
# for floor in range(1, 6):
#     if flag != True:
#         break
#     if floor == 3:
#         continue
#     print(f"欢迎来到第{floor}层")
#     for room in range(1, 9):
#         print(f"{floor}0{room}")
#         if floor == 4 and room == 4:
#             print("886~")
#             # exit()
#             flag = False
#             break
#
#
#         # continue
#         # break
#
#
#
#
#
#
#

# height = 100
# distance = 0
# for i in range(10):
#     distance += height
#     height /= 2
#     if i == 9:
#         break
#     distance += height
# print(distance)

import faker  # pip install Faker

import random

alex = faker.Faker(locale="zh_CN")

staff_list = []

for i in range(1, 301):
    staff_list.append(alex.name())
print(staff_list)

level = [30, 6, 3]
for i in range(3):
    winner_list = random.sample(staff_list, level[i])
    for wc in winner_list:
        staff_list.remove(wc)
    print(f"抽中{3 - i}等奖的人是", winner_list)

