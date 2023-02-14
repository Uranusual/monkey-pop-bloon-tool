# click(global_point_map[自选地图难度], times=点击地图次数)
# click(global_point_map[自选地图位置], times=1)
# click(global_point_map[自选游戏难度], times=1)
# click(global_point_map[自选游戏模式], times=1)
click(global_point_map['s1'], times=1)
click(global_point_map['map_6'], times=1)
click(global_point_map['difficulty'], times=1)
click(global_point_map['chimps'], times=1)
# 点击进入地图
global 自定义打法
# 下面打法gon
自定义打法 =[['pre','''
# 猴子1名字=[猴子中文名,[猴子1的坐标]]
tack=[图钉塔,[938,159]]#为猴子命名并确立塔型和坐标
startgame(2)#点击游戏并点击空格2次
spike=[刺钉工厂,[1100,142]]
# fz_(*猴子1名字)
fz_(*tack)#放置猴子1
up101(*tack)#升级猴子1为101
fz_(*spike)
up002(*spike)
tab(*spike,3)#切换猴子2的攻击对象3次
up202(*tack)
up103(*spike)
up302(*tack)
up204(*spike)
up402(*tack)
up205(*spike)
up502(*tack)
tab(*tack,3)
''']]
# ＝后面的内容是你游戏的打法


自定义打法=[[







]]