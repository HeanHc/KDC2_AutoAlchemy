import time
import pydirectinput as p

# 游戏内基本操作

def reset():
    # 重置到打开草药栏的位置

    p.press('I')
    time.sleep(0.5)
    p.press('esc')
    time.sleep(0.5)

def move_to_mortar():
    # 移动到研钵位置

    reset()
    p.moveRel(9, 11, 0.1)
    time.sleep(0.1)

def move_to_plate():
    # 移动到盘子位置

    reset()
    p.moveRel(-5, 12, 0.1)
    time.sleep(0.1)

def move_to_pot():
    # 移动到大锅位置

    reset()
    p.moveRel(-10, 4, 0.1)
    time.sleep(0.1)

def add_liquid(x):
    # 将基底液体加入大锅
    # x:1 水
    #   2 葡萄酒
    #   3 油
    #   4 烈酒

    x_dis = {1: [-36, -1],
             2: [-31, -1],
             3: [-26, -1],
             4: [-21, -1]}

    p.moveRel(x_dis[x][0], x_dis[x][1], 0.1)
    time.sleep(0.5)
    p.press('e')
    time.sleep(9)

def get_drug(x=1, y=1):
    # x:1, 2, 3, 4, 5, 6 分别对应货架上从左到右 3 个、书上从左到右 3 个
    # y:1 放进大锅
    #   2 放进研钵
    #   3 放进研钵并捣碎

    x1_dis = {1: [8, 0, -16, 4],
              2: [13, 0, -21, 4],
              3: [18, 0, -26, 4],
              4: [10, 7, -17, -2],
              5: [14, 5, -22, -1],
              6: [18, 5, -26, -1]
              }
    x2_dis = {1: [1, 10],
              2: [-4, 10],
              3: [-9, 10],
              4: [-1, 4],
              5: [-5, 5],
              6: [-9, 5]
              }

    reset()

    p.moveRel(x1_dis[x][0],x1_dis[x][1], 0.1)
    time.sleep(1)
    p.press('e')
    time.sleep(2.1)
    if y == 1:
        p.moveRel(x1_dis[x][2],x1_dis[x][3], 0.1)
        time.sleep(0.5)
        p.press('e')
        time.sleep(3)
    if y == 2:
        p.moveRel(x2_dis[x][0],x2_dis[x][1], 0.1)
        time.sleep(1)
        p.press('e')
        time.sleep(2.5)
    if y == 3:
        p.moveRel(x2_dis[x][0], x2_dis[x][1], 0.1)
        time.sleep(1)
        p.press('e')
        time.sleep(2.5)
        p.press('e')
        time.sleep(9.7)

def mortar_to_other(x, put=False):
    # 从研钵位置出发操作，put 为 True 时放进去
    # x:1 放进大锅
    #   2 放进盘子

    x_dis = {1: [-17, -6],
             2: [15, 3]
             }
    x_time = {1: 7,
              2: 6.3
              }
    p.moveRel(x_dis[x][0], x_dis[x][1], 0.1)
    time.sleep(0.5)

    if put:
        p.press('e')
        time.sleep(x_time[x])

def mortar_down():
    # 放下研钵

    p.press('r')
    time.sleep(2.9)

def mortar_up():
    # 拿起研钵

    p.press('e')
    time.sleep(2.9)

def mortar_grind():
    #  研钵研磨
    p.press('e')
    time.sleep(9.7)

def plate_to_other(x, put=False):
    # 从盘子位置出发操作，put 为 True 时放进去
    # x:1 放进大锅
    #   2 放进研钵

    x_dis = {1: [-17, -6],
             2: [-4, -6]
             }
    x_time = {1: 4.7,
              2: 5
              }
    p.moveRel(x_dis[x][0], x_dis[x][1], 0.1)
    time.sleep(0.5)

    if put:
        p.press('e')
        time.sleep(x_time[x])

def plate_down():
    # 放下盘子

    p.press('r')
    time.sleep(2.0)

def plate_up():
    # 拿起盘子

    p.press('e')
    time.sleep(2.0)

def pot_to_other(x):
    # 从大锅出发操作
    # x:1 移动到盘子
    #   2 移动到研钵
    #   3 移动到瓶子

    x_dis = {1: [2, 7],
             2: [17, 6],
             3: [-21, 1]
             }
    p.moveRel(x_dis[x][0], x_dis[x][1], 0.1)
    time.sleep(0.5)

def pot_down():
    # 放下大锅

    p.press('e')
    time.sleep(3.6)

def pot_up():
    # 抬起大锅

    p.press('e')
    time.sleep(3)

def blow(x):
    p.press('q', presses=x, duration=0.5)

def into_bottle(x):
    # 装瓶
    # x:1 直接装瓶
    # x:2 蒸馏

    x_dis = {1: [21, -1],
             2: [0, 3]}
    x_time = {1: 9,
              2: 15}

    p.press('e')
    time.sleep(2.5)
    p.moveRel(x_dis[x][0], x_dis[x][1], 0.1)
    p.keyDown('e')
    time.sleep(1)
    p.keyUp('e')
    time.sleep(x_time[x])

def grind():

    p.keyDown('e')
    time.sleep(1)
    p.keyUp('e')
    time.sleep(15)