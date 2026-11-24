from basic_oerations import *
from herbsearch import *

import pydirectinput as p
import time

# 所有炼金配方对应的操作

def lethean_water(k=1): # 冥河之水

    for i in range(k):
        herb_search('wormwood', 'belladona', 'nightshade')

        add_liquid(4)
        get_drug(3, 2)
        get_drug(3, 3)
        mortar_to_other(1, True)

        get_drug(2, 1)
        pot_down()

        time.sleep(25)
        pot_up()

        get_drug(1, 1)
        pot_to_other(3)
        into_bottle(2)

        p.press('esc')

def nighthawk(k=1): # 夜鹰药剂

    for i in range(k):

        herb_search('eyewort', 'belladona', 'chamomile')

        add_liquid(1)
        get_drug(3, 2)
        get_drug(3, 3)
        mortar_to_other(1, True)

        get_drug(2, 1)
        pot_down()

        get_drug(1, 3)
        mortar_down()
        mortar_to_other(1)
        time.sleep(10)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)

        pot_to_other(3)
        into_bottle(1)

        p.press('esc')

def hair_o_the_dog(k=1): # 解酒药剂

    for i in range(k):

        herb_search('salvia', 'hypericum', 'mint')

        add_liquid(1)
        get_drug(3, 1)
        get_drug(2, 1)
        pot_down()

        get_drug(1, 3)
        mortar_down()
        mortar_to_other(1)
        time.sleep(7)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)
        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def artemisia(k=1): # 艾蒿药剂

    for i in range(k):

        herb_search('wormwood', 'salvia')

        add_liquid(4)
        get_drug(2, 1)
        pot_down()

        get_drug(3, 2)
        mortar_to_other(1)
        time.sleep(1)
        pot_up()

        get_drug(3, 3)
        mortar_to_other(1, True)
        pot_down()
        time.sleep(15)

        pot_up()
        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def aesop(k=1): # 伊索药剂
    for i in range(k):

        # 选取草药
        herb_search('belladona', 'teethBoar', 'comfrey')

        # 操作

        add_liquid(4)

        get_drug(2,2)
        get_drug(2,3)
        mortar_to_other(1, True)

        get_drug(6, 1)
        pot_down()

        get_drug(3,3)
        mortar_down()

        mortar_to_other(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)

        pot_to_other(3)
        into_bottle(2)

        p.press('esc')

def cockerel(k=1): # 公鸡药剂

    for i in range(k):

        herb_search('valerian', 'mint')

        add_liquid(4)

        get_drug(2, 2)
        get_drug(2, 3)
        mortar_to_other(1, True)
        pot_down()

        time.sleep(5)
        get_drug(3, 1)
        time.sleep(15)
        pot_up()

        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def embrocation(k=1):
    # 活络擦剂

    for i in range(k):

        herb_search('eyewort', 'poppy', 'valerian', 'teethBoar')

        add_liquid(3)
        get_drug(2, 1)
        get_drug(1, 1)
        pot_down()

        get_drug(3, 3)
        mortar_down()
        mortar_to_other(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)
        get_drug(6, 1)
        pot_down()
        time.sleep(7)
        pot_up()

        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def bucks_block(k=1):
    # 雄鹿之血药剂

    for i in range(k):

        herb_search('hypericum', 'dandelion', 'comfrey')

        add_liquid(3)
        get_drug(3, 3)
        mortar_to_other(1, True)

        get_drug(1, 1)
        pot_down()

        time.sleep(3)
        get_drug(2, 1)
        blow(12)
        time.sleep(2)
        pot_up()

        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def quickfinger_option(k=1): # 巧手药剂

    for i in range(k):

        herb_search('eyewort', 'valerian', 'cobweb')

        add_liquid(1)
        get_drug(6, 1)
        get_drug(3, 1)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 2)
        get_drug(2, 3)
        time.sleep(10)
        mortar_to_other(1, True)

        time.sleep(5)
        pot_up()
        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def painkiller_option(k=1): # 止痛药剂

    for i in range(k):

        herb_search('poppy', 'comfrey', 'marigold')

        add_liquid(4)
        get_drug(3, 2)
        get_drug(3, 2)
        get_drug(3, 3)
        mortar_to_other(1, True)

        get_drug(1, 1)
        pot_down()
        blow(12)
        time.sleep(2)
        pot_up()

        get_drug(2, 1)
        pot_down()
        time.sleep(17)
        pot_up()

        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def aqua_vitalist(k=1): # 生命之水

    for i in range(k):

        herb_search('dandelion', 'marigold')

        add_liquid(1)
        get_drug(3, 1)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 2)
        mortar_down()
        mortar_to_other(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_grind()
        mortar_to_other(1, True)
        pot_down()
        time.sleep(17)

        pot_up()
        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def fox(k=1): # 狐狸药剂

    for i in range(k):

        herb_search('urticaria', 'hypericum', 'belladona', 'charcoal')

        add_liquid(3)
        get_drug(2, 2)
        get_drug(3, 3)
        mortar_to_other(1, True)
        pot_down()

        get_drug(6, 3)
        mortar_to_other(1)
        pot_up()
        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)

        get_drug(1, 1)
        pot_down()
        time.sleep(8)
        pot_up()
        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def bowmans_brew(k=1):
    # 射手药剂

    for i in range(k):

        herb_search('eyewort', 'hypericum')

        add_liquid(4)

        get_drug(3, 1)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 3)
        time.sleep(10)
        mortar_to_other(1, True)

        blow(12)
        time.sleep(2)
        pot_up()

        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def marigold_decoction(k=1): # 金盏花药剂

    for i in range(k):

        herb_search('urticaria', 'marigold')

        add_liquid(1)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 2)
        get_drug(2, 3)
        mortar_down()
        mortar_to_other(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)

        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def saviour_schnapps(k=1): # 救世干酒

    for i in range(k):

        herb_search('urticaria', 'belladona')

        add_liquid(2)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 2)
        get_drug(2, 3)
        mortar_to_other(1, True)

        time.sleep(4)
        pot_up()
        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def digestive_potion(k=1): # 消化药剂

    for i in range(k):

        herb_search('urticaria', 'thistle', 'charcoal')

        add_liquid(1)

        get_drug(2, 1)
        get_drug(2, 1)
        pot_down()

        get_drug(3, 3)
        mortar_to_other(1, True)

        get_drug(6, 2)

        mortar_to_other(1)
        time.sleep(4)
        pot_up()

        pot_to_other(2)
        mortar_grind()
        mortar_to_other(1, True)

        pot_to_other(3)
        into_bottle(1)

        p.press('esc')

def anti_plague_potion(k=1): # 圣罗科药剂

    for i in range(k):

        herb_search('hypericum', 'ginger', 'chamomile')
        add_liquid(2)

        get_drug(3, 2)
        get_drug(3, 3)
        mortar_to_other(1, True)
        pot_down()

        time.sleep(8)
        pot_up()

        get_drug(1, 1)
        get_drug(1, 1)
        pot_down()

        get_drug(2, 3)
        mortar_to_other(1, True)
        blow(12)
        time.sleep(2)
        pot_up()

        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def anti_iflammatory_potion(k=1): # 抗炎药剂
    for i in range(k):

        herb_search('urticaria', 'valerian', 'ginger')

        add_liquid(1)
        get_drug(3, 3)
        mortar_to_other(1, True)
        pot_down()

        blow(12)
        time.sleep(2)
        pot_up()

        get_drug(2, 1)
        get_drug(2, 1)
        pot_down()

        get_drug(1, 3)
        mortar_down()
        mortar_to_other(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)
        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def mandrake_decoction(k=1): # 曼德拉草药剂

    for i in range(k):

        herb_search('mandrakeRoot', 'salvia', 'freshwaterPearl')

        add_liquid(2)
        get_drug(6, 1)
        pot_down()

        get_drug(5, 2)
        mortar_to_other(1)
        time.sleep(3)
        pot_up()

        pot_to_other(2)
        mortar_grind()
        mortar_to_other(1, True)
        pot_down()
        time.sleep(7)
        pot_up()

        get_drug(3, 2)
        get_drug(3, 3)
        mortar_to_other(1, True)

        pot_down()
        blow(12)
        time.sleep(2)
        pot_up()

        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def chamomile_brew(k=1): # 甘菊药剂

    for i in range(k):

        herb_search('chamomile', 'salvia')

        add_liquid(2)
        get_drug(3, 1)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 2)
        mortar_down()
        mortar_to_other(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_grind()
        mortar_to_other(1, True)

        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def moonshine(k=1): # 私酒
    for i in range(k):

        herb_search('mint', 'wormwood')

        add_liquid(4)
        get_drug(2, 1)
        get_drug(2, 1)
        pot_down()

        get_drug(3, 2)
        get_drug(3, 3)
        mortar_to_other(1, True)

        time.sleep(4)
        pot_up()
        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def essential_oil(k=1): # 精油

    for i in range(k):

        herb_search('chamomile', 'salvia', 'valerian')

        add_liquid(3)
        get_drug(3, 1)
        get_drug(3, 1)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 3)
        time.sleep(10)
        mortar_to_other(1, True)

        get_drug(1, 2)
        mortar_down()
        mortar_to_other(1)
        time.sleep(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_grind()
        mortar_to_other(1, True)

        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def mintha_perfume(k=1): # 薄荷香水
    for i in range(k):

        herb_search('dandelion', 'marigold', 'mint')

        add_liquid(2)
        get_drug(3, 2)
        get_drug(3, 2)
        get_drug(3, 2)
        get_drug(1, 3)
        mortar_to_other(1, True)
        pot_down()

        time.sleep(15)
        get_drug(2, 1)
        blow(12)
        time.sleep(2)
        pot_up()

        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def lion_perfume(k=1): # 雄狮香水

    for i in range(k):

        herb_search('salvia', 'mint')

        add_liquid(4)
        get_drug(3, 1)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 2)
        get_drug(2, 3)
        mortar_down()
        mortar_to_other(1)
        pot_up()

        pot_to_other(2)
        mortar_up()
        mortar_to_other(1, True)
        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def bane_poison(k=1): # 祸根毒药

    for i in range(k):

        herb_search('wormwood', 'belladona', 'mushroomAmanita')

        add_liquid(2)
        get_drug(3, 1)
        pot_down()

        get_drug(2, 2)
        get_drug(2, 3)
        mortar_to_other(1, True)
        blow(12)
        time.sleep(2)
        pot_up()

        get_drug(6, 1)
        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def dollmaker_poison(k=1): # 玩偶毒药

    for i in range(k):

        herb_search('valerian', 'paris')

        add_liquid(4)
        get_drug(2, 1)
        get_drug(2, 1)
        pot_down()

        get_drug(3, 3)
        time.sleep(3)
        mortar_to_other(1, True)

        time.sleep(15)
        pot_up()
        pot_to_other(3)
        into_bottle(2)
        p.press('esc')

def lullaby_potion(k=1): # 安眠毒药

    for i in range(k):

        herb_search('poppy', 'paris', 'thistle')

        add_liquid(3)
        get_drug(3, 1)
        pot_down()
        time.sleep(3)

        get_drug(1, 1)
        time.sleep(6)
        pot_up()

        get_drug(2, 3)
        mortar_to_other(1, True)
        pot_to_other(3)
        into_bottle(1)
        p.press('esc')

def lead_ball(k=1): # 铅弹

    for i in range(k):

        herb_search('sulfur', 'saltpeter', 'charcoal')

        add_liquid(1)
        get_drug(6, 2)
        get_drug(5, 3)
        mortar_to_other(1, True)
        pot_down()

        get_drug(4, 3)
        time.sleep(3)
        mortar_to_other(1, True)

        time.sleep(15)
        pot_up()
        pot_to_other(2)
        grind()
        p.press('esc')

def scattershot(k=1): # 霰弹

    for i in range(k):

        herb_search('sulfur', 'saltpeter', 'charcoalImproved')

        add_liquid(1)
        get_drug(6, 2)
        get_drug(5, 3)
        mortar_to_other(1, True)
        pot_down()

        get_drug(4, 3)
        time.sleep(10)
        mortar_to_other(1, True)

        time.sleep(6)
        pot_up()
        pot_to_other(2)
        grind()
        p.press('esc')