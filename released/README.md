</div>

# 目录

<!-- 1. [下载](#一-下载)
2. [使用准备](#二-使用准备)
   2. 1. [游戏设置](#1-游戏设置)
   2. 2. [系统设置](#2-系统设置)
3.  [使用方法及功能](#三-使用方法及功能)<!-- $~~~~$[2.系统设置](#2-系统设置) -->

<!-- 4. [设置](#四-设置)
5. [注意事项](#五-注意事项)
5. [疑惑解答](#五-)
[1.兼容性](#兼容性) -->

<!-- [TOC] -->

<!-- 前面这个可以用来自动生成目录 -->

<!-- 下面时系统插件自动强制生成的目录 -->

- [目录](#目录)
- [一-下载](#一-下载)
- [二-使用准备](#二-使用准备)
  - [1-游戏设置](#1-游戏设置)
  - [2-系统设置](#2-系统设置)
- [三-使用方法及功能](#三-使用方法及功能)
  - [1-使用方法：](#1-使用方法)
  - [2-功能及使用说明：](#2-功能及使用说明)
- [四-设置](#四-设置)
- [五-注意事项](#五-注意事项)
- [六-疑惑解答](#六-疑惑解答)
  - [1-运行出错解答](#1-运行出错解答)
    - [其他小问题](#其他小问题)
  - [2-兼容性](#2-兼容性)
- [七-自定义打法](#七-自定义打法)
- [八-版本历史与更新日志](#八-版本历史与更新日志)
- [九-隐私声明](#九-隐私声明)

# 一-下载

| 免费版                                                           | vip版 (q群更新)  | svip版 (开发中) |
| ---------------------------------------------------------------- | ---------------- | --------------- |
| [下载](https://github.com/Uranusual/monkey-pop-bloon-tool/releases) | 贡献后入主群获取 | 暂无            |

> q群709918803-[【猴子打气球6脚本子群】](https://jq.qq.com/?_wv=1027&k=Z9kt5FSw)

# 二-使用准备

### 1-游戏设置

1.在游戏中点击设置选项
[![游戏设置1](instruction/images/gamesetting1.png "第一步")](https://markdown.com.cn) `<!-- [![图片未加载显示的名字](图片路径 "悬浮到图片显示的信息")](图片在线地址)-->`
2.将游戏尺寸设置为脚本可以用的3中游戏尺寸中的一种，并取消全屏的勾选，1366x768,1280x720,1600x900中的一种，优先使用1366x768
[![游戏设置1](instruction/images/gamesetting1.png "第一步")](https://markdown.com.cn)

<!-- [![游戏设置2](\instruction\images\gamesetting2.png "第二步")](https://markdown.com.cn) -->

<!-- 上面那个(\开头的和\路径的")格式有些markdown软件或在github不显示 -->

3.对游戏进行设置，确保脚本的游戏操作正常运行
[![游戏设置3](instruction/images/gamesetting3.png "第三步")](https://markdown.com.cn)
4.对游戏热键进行设置，确保脚本的按键操作有效，最好是用恢复默认
[![游戏设置4](instruction/images/gamesetting4.png "第四步")](https://markdown.com.cn)

### 2-系统设置

[![系统设置1](instruction/images/systemsetting1.png "第一步")](https://markdown.com.cn)
[![系统设置2](instruction/images/systemsetting2.png "第二步")](https://markdown.com.cn)
[![系统设置3](instruction/images/systemsetting3.png "特殊设置")](https://markdown.com.cn)
这些设置改动后最好是重新启动一下电脑
游戏尺寸和系统设置不对，打开脚本识别的游戏尺寸不对，脚本会闪退

# 三-使用方法及功能

### 1-使用方法：

- 在打开游戏主页情况下（一些是在游戏中（地图界面）或者特定的界面）,打开脚本，终端（脚本界面）点击输入相应的数字模式
- 脚本界面都对功能、设置等等进行了说明,用新功能或出问题了可以直接看看启动时提供的信息

### 2-功能及使用说明：

- 循环重新开始刷一个图：大部分模式如0，1，2，3等都是这种形式：可用于刷（猴子/账号）经验、猴币、0-4阶insta猴,但是**不能用来刷收集材料**，重新开始的模式只有第一次会获取收集材料
- 模式0的使用方法

  > 0
  > 地图名称
  > 模式名称
  >

  例如

  > 0
  > 鬼屋
  > 极难
  >
- 自动识别额外奖励并刷取：用于收集金气球,收集材料
- 自动按顺序推图（svip的功能）：从你选的的地图开始，识别你未刷的图，如果有打法就进入模式刷，刷完重新刷这个图未刷的图，如果未刷的图没有打法将跳过，如果某个地图模式失败3次也会跳过，这个图能刷都刷完的话将刷下一个地图。如果脚本不出意外的话，将一直刷到最后一张图结束为止后自动关闭
  使用方法

  > 8
  > 地图名称
  >
- 合作挂机给钱：在联机合作中打开,只要你打开游戏右侧的给钱的界面，脚本会在你可以给钱的时候没隔1秒自动给钱，当被给钱的掉线了或者关闭给钱界面，脚本会暂停给钱
  ，打开给钱会继续自动给钱
- 自动使用技能：脚本作者经常玩游戏也没怎么用过，懒得说明
- -1运行打法.py文件模式：开启-1，脚本将 运行脚本文件相同目录下的 打法.py 中的内容，如果没有则会生成示例
- 

# 四-设置

设置脚本使用的热键：

1. 脚本运行-11生成配置文件
2. 打开生成的'热键设置.ini'文件进行编写

```javascript
[skill]
; top = Key.f1 ;如果用f1快捷键就用这个格式
top = ","
middle = '.'
buttom = '/'
[monkey]
飞镖猴='q'
回旋镖猴='w'
大炮='e'
图钉塔='r'
冰猴='t'
胶水炮手='y'
狙击手猴='z'
猴子潜艇='x'
海盗猴='c'
皇家飞行员='v'
直升机飞行员='b'
迫击炮猴='n'
机枪猴='m'
法师猴='a'
超猴侠='s'
忍者猴='d'
炼金术士='f'
德鲁伊='g'
香蕉农场='h'
工程师猴='l'
刺钉工厂='j'
猴子村='k'
英雄='u'
```

# 五-注意事项

- 显示器分辨率必须有1280x720,1366x768,1600x900分辨率中的一种.基础坐标为1366x768,其他分辨率下的坐标为转化坐标，会有偏差，导致位置不准，猴子放不下，**请优先使用1366x768**
  m默认不带任何具体功能, 需要在按[设置](#设置)中的说明添加感兴趣的功能.
- 默认不对未登录的状态做适配.
- 新版本一旦正式发布, 就不再对旧版本做任何技术支持.

# 六-疑惑解答

### 1-运行出错解答

- 脚本能点到正确位置：说明游戏尺寸和系统设置都没问题，反之则是这2个地方中的一个设置出了问题
- 猴子放置成功但不执行后续操作,(之前：没和其他突然文件放一起。现在：图片文件已经打包进exe，不需要一同放置了)
- 某个猴子放不上去：该游戏尺寸的坐标有偏差，正好偏差到不能放的位置;请尽量使用1366x768的游戏尺寸
- 猴子位置乱放：禁用微调没打开，请打开

##### 其他小问题

- vip版中避难所某些难度放不上一开始的猴子：因为不同难度初始回合不同，平台位置不同，但打法目前都套用点击，所以前面的几回合请自己先过一下再继续脚本

### 2-兼容性

- 支持win7,win10,win11版本的epic和steam版本
- 不支持mac,android,ios

目前只有windows端的exe运行程序，系统暂时无脚本程序c

# 七-自定义打法

1. 运行-1将生成以下的示范打法，在加密-沙盒中运行便可以看到示例打法的效果

```python
print('将运行示范打法，请打开加密地图的沙盒模式再运行')
# 这是猴子名对应的英文
# dart飞镖猴q
# boomerang回旋镖猴w
# bomb大炮e
# tack图钉塔r
# ice冰猴t
# glue胶水炮手y
# sniper狙击手猴z
# sub猴子潜艇x
# buccaneer海盗猴c
# ace皇家飞行员v
# pilot直升机飞行员b
# mortar迫击炮猴n
# gunner机枪猴m
# wizard法师猴a
# super超猴侠s
# ninja忍者猴d
# alchemist炼金术士f
# druid德鲁伊g
# farm香蕉农场h
# engineer工程师猴l
# spike刺钉工厂j
# village猴子村k
# hero英雄u
# 加速回合(20)


直升机=[直升机飞行员,[962,297]]
迫击炮=[迫击炮猴,[953,89]]
机枪=[机枪猴,[856,50]]
法师=[法师猴,[941,191]]
# 英雄1=[超猴侠,[447,435]]
忍者=[忍者猴,[719,23]]
# 英雄1=[炼金术士,[447,435]]
# 英雄1=[德鲁伊,[447,435]]
市场=[香蕉农场,[1009,488]]
陷阱=[工程师猴,[791,32]]
超频=[工程师猴,[869,143]]
永钉=[刺钉工厂,[889,424]]
# 英雄1=[猴子村,[447,435]]
hero=[英雄,[834,290]]

# 英雄1=[飞镖猴,[447,435]]
# 英雄1=[回旋镖猴,[447,435]]
# 英雄1=[海盗船,[447,435]]
# 英雄1=[皇家飞行员,[447,435]]
# 英雄1=[忍者猴,[447,435]]
# 英雄1=[工程师猴,[447,435]]

#  up010(海盗1)
# click([1,1],times=100)
dm([539, 224])
startgame()
startgame(1)
fz(hero)
uphero(15)
run_thread(abilities,('12',))
fz(忍者)
aimcamo(忍者)
fz(永钉)
up025(永钉)
tab(永钉,3)
fz(迫击炮)
aim(迫击炮,[100,100])
fz(陷阱)
up015(陷阱)
aimtool(陷阱,[814,140])
fz(法师)
up220(法师)
aimtool(法师,[814,140])
fz(机枪)
tab(机枪)
aimtool(机枪,[100,100])
fz(直升机)
tab(直升机)
up040(直升机)
tab(直升机)
aimtool(直升机,[337,0],[337,200])


fz(超频)
up050(超频)
msale(机枪)
time.sleep(4)
ability('1')
ability('4',[941,191],[585, 286])
ability('6',[719,23])
fz(市场)
cricle_moveto([1009,488],cd=2,times=2)#或者下面这个 市场[1] 表示市场的第2个信息，即是[1009,488]
#cricle_moveto(市场[1],cd=2,times=2
up025(市场)
after_round(18)#不放有概率g
print('[%s]到18回合了' % get_datetime())
ability('3')
# #仅初级
print('使用杰哥的道具，只有用杰哥的时候才能正常运行')
tool('14')
tool('1',[581,482])
input()
```

2. 编写好脚本后，再运行-1，则可以用你编写的脚本，如果脚本报错或闪退，就是打法代码中有些内容格式不对

# 八-版本历史与更新日志

# 九-隐私声明

本脚本以及本仓库中提供的组件

/插件, 是完全匿名的. 用户数据的使用均在本地完成, 不会存储到任何服务器, 也不会有所谓的"用户体验改善计划"来收集统计数据.

但是, 任何组件/插件都对用户数据有着完全的访问能力, 对于其他来源(非本仓库提供)的组件/插件, 请自行甄别其安全性.

<!-- # 开源许可

见 [LICENCE.md](./LICENCE.md). -->
