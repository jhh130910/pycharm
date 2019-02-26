# coding: utf-8
# change world by programming
#  伪代码

interval = 0

while True:
    if 点击退出:
        exit()

    interval += 1
    if interval ==50：
        interval = 0
        小飞机诞生

    # 防止卡顿
    小飞机移动一个位置
    屏幕刷新

    if 用户鼠标移动：
        飞机位置 = 用户鼠标位置
        屏幕刷新

    if 发生冲突：
        挂掉，撞击音乐
        挂掉图形刷新
        打印"游戏结束"
        停止音乐，淡出

