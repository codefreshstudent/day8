# 一付扑克牌，去掉大小王，每个玩家发3张牌，最后比大小，看谁赢。
#
# 有以下几种牌：
#
# 豹子：三张一样的牌，如3张6.
#
# 顺金：又称同花顺，即3张同样花色的顺子， 如红桃 5、6、7
#
# 顺子：又称拖拉机，花色不同，但是顺子，如红桃5、方片6、黑桃7，组成的顺子
#
# 对子：2张牌一样
#
# 单张：单张最大的是A
#
# 这几种牌的大小顺序为， **豹子>顺金>同花>顺子>对子>单张**


# 1， 单牌之间如何比大小
# A： 红桃J 红桃K 黑桃A  11 + 130 + 1400 = 1541
#
# B： 方片2 方片2 梅花3  2 + 20 + 300 = 322 * 10 = 3220

# 2， 不同牌型之间如何比大小
# 3， 如何判断玩家是什么牌  （不同牌型有不同的判断方法） 高内聚 低耦合
# 把不同的功能 定义成单独的函数


# 1， 生成牌
import random


def generate_pokes():
    poke_type = ["♥", "♠", "♣", "♦"]
    poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    poke_list = []

    for p_type in poke_type:
        count = 2
        for p_num in poke_nums:
            card = [f"{p_type}{p_num}", count]
            count += 1
            poke_list.append(card)
    return poke_list


poke_list = generate_pokes()
random.shuffle(poke_list)
print(poke_list)

players = ["old_shang", "alex", "peiqi", "black_girl", "小芸"]


# 2， 发牌
def issue_cards(players, poke_list):
    player_dic = {}
    for p_name in players:
        p_cards = random.sample(poke_list, 3)
        for card in p_cards:
            poke_list.remove(card)
        player_dic[p_name] = p_cards
        print(f"为玩家{p_name}生成了牌", p_cards)
    return player_dic


player_dic = issue_cards(players, poke_list)


# 3， 写好每种牌型的判断规则函数
def sortlist(lis):
    l = len(lis)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if lis[j][1] > lis[j + 1][1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
    return lis


# 单牌
def calculate_single(p_cards, score):
    p_cards = sortlist(p_cards)
    # p_cards = sorted(p_cards, key=lambda li : li[1])
    weight_val = [0.1, 1, 10]
    count = 0
    for card in p_cards:
        score += card[1] * weight_val[count]
        count += 1
    print(f"计算单牌", p_cards, score)
    return score


# 对子
def calculate_pair(p_cards, score):
    p_cards = sortlist(p_cards)
    card_val = [i[1] for i in p_cards]
    if len(set(card_val)) == 2:
        if card_val[0] == card_val[1]:
            score = (card_val[0] + card_val[1]) * 50 + card_val[2]
        else:
            score = (card_val[2] + card_val[1]) * 50 + card_val[0]
    print(f"计算对子", p_cards, score)
    return score


# 顺子
def calculate_straight(p_cards, score):
    p_cards = sortlist(p_cards)
    card_val = [i[1] for i in p_cards]
    a, b, c = card_val
    if (b - a == 1 and c - b == 1) or card_val == [2, 3, 14]:
        score *= 100
    print(f"计算顺子", p_cards, score)
    return score


# 同花
def calculate_same_color(p_cards, score):
    color_set = {i[0][0] for i in p_cards}
    if len(color_set) == 1:
        score *= 1000
    print(f"计算同花", p_cards, score)
    return score

# 同花顺
def calculate_same_color_straight(p_cards, score):
    p_cards = sortlist(p_cards)
    card_val = [i[1] for i in p_cards]
    a, b, c = card_val
    if (b - a == 1 and c - b == 1) or card_val == [2, 3, 14]:
        color_set = {i[0][0] for i in p_cards}
        if len(color_set) == 1:
            score *= 0.1
    print(f"计算同花顺", p_cards, score)
    return score

# 豹子
def calculate_leopard(p_cards, score):
    card_val = {i[1] for i in p_cards}
    if len(card_val) == 1:
        score *= 100000
    print(f"计算豹子", p_cards, score)
    return score

# 4， 对比
calc_func_orders = [
    calculate_single,
    calculate_pair,
    calculate_straight,
    calculate_same_color,
    calculate_same_color_straight,
    calculate_leopard
]

performance = []

for p_name, p_cards in player_dic.items():
    print(f"开始计算玩家{p_name}的牌")
    score = 0
    for calc_func in calc_func_orders:
        score = calc_func(p_cards, score)
    performance.append([p_name, score])

winner = sortlist(performance)[-1]
for i in performance:
    if i[1] == winner[1]:
        print("赢家是", i)