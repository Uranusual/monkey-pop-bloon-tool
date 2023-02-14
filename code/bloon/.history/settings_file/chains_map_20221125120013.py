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
# #   394<x<1128猴村/1133/1147 26<y<728  2个大猴子相差86 中猴子要隔开47(中猴子体积23)


all_chains = {

'避难所':[#全知识单金初级
['pre',
'''
hero=[英雄,[633, 181]]
sniper=[狙击手猴,[579, 180]]
fz_(*sniper)
fz_(*hero)
key(Key.space)
time.sleep(1)
key(Key.space)
up205(*sniper)
''']
],
    
    '峡谷': [
        ['pre', '''
# 前置
hero([287, 525])
sniper([68, 706-32])
dart([517, 577])
dart([517, 577],'020')
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
'''],[24, '''
dart([517, 609-32],'022')
'''],[49, '''
dart([517, 609-32],'023')
'''],[61, '''
sniper([68, 674],'102')
'''],[118, '''
ace([203, 567])
ace([203, 567],'003')
ace([203, 567],'203')
'''],[180, '''
alchemist([233, 515])
alchemist([233, 515],'401')
'''],
[245, '''
village([243, 642])
village([243, 642],'200')
village([243, 642],'202')
ace([138, 628])
ace([138, 628],'003')
ace([138, 628],'203')
'''],[340, '''
village([243, 642],'203')
'''],[410, '''
ace([203, 567],'204')
'''],[415, '''
sniper([68, 674],'402')
'''],[625, '''
spike([291, 575])
spike([291, 575],'250')
ace([203, 567],'205')
'''],[675, '''
ace([153, 692])
ace([153, 692],'502')
'''],[750, '''
pilot([376, 587])
pilot([376, 587],'502')
'''],[760, '''
alchemist([233, 515],'501')
'''],

],
    
    # 水淹山谷
    '水淹山谷': [
        ['pre', '''
# 前置
hero([511, 283])
sub([733, 155])
sub([733, 559])
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
         '''],
    
        [40, '''
sub([733, 559],'031')
sub([733, 155],'204')
buccaneer([790, 200])
buccaneer([790, 200], '020')
buccaneer([790, 200], '520')
ice([792, 93])
ice([792, 93], '041')
village([865, 70])
village([865, 70],'203')
ace([916, 165])
ace([916, 165], '205')
tack([663, 110])
tack([663, 110],'520')
sub([666, 44])
sub([666, 44],'250')
sniper([947, 92])
sniper([947, 92],'502')
alchemist([794, 151])
alchemist([794, 151],'205')
        '''],
        
    ],
    
    # 炼狱
    '炼狱': [
        ['pre', '''
# 前置
hero([598, 262])
sniper([1101, 468])
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)

        '''],
    
    [10, '''
sniper([1101, 468], '022')
        '''],

        
        [150, '''
sniper([1101, 468], '023')
        '''],
        
        [220, '''
alchemist([1143, 493])
alchemist([1143, 493], '401')
        '''],
        
        [205, '''
sniper([1101, 468], '024')
        '''],
        
        [250, '''
village([1122, 350])
village([1122, 350], '203')
        '''],
        [340, '''
ace([1112, 418])
ace([1112, 418], '205')
        '''],
        [840, '''
pilot([77, 414])
pilot([77, 414], '502')
        '''],
        
        [860, '''
buccaneer([328, 603-32])
buccaneer([328, 603-32], '502')
        '''],
        
        [900, '''
sniper([861, 637-32])
sniper([861, 637-32], '502')
        '''],
        
        [920, '''
pilot([337, 191-32])
pilot([337, 191-32], '205')
        '''],
        
    ],
    
    # 血腥水坑
    '血腥水坑': [
        
        ['pre', '''
        # 前置
hero([352, 343])
dart([869, 553])
sniper([494, 90])
sniper([506, 170])
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
        '''],
        
        [15, '''
sniper([506, 170], '022')
        '''],
        
        [80, '''
sub([849, 140-32])
sub([849, 140-32], '202')
        '''],
        
        [125, '''
sniper([494, 90], '102')
        '''],
        
        [160, '''
village([426, 170])
village([426, 170], '002')
        '''],
        
        [185, '''
sniper([506, 170], '024')
alchemist([566, 251])
alchemist([566, 251], '401')
        '''],
        
        [238, '''
ace([716, 244])
ace([716, 244], '203')
        '''],
        
        [305, '''
village([426, 170], '203')
        '''],
        [380, '''
druid([375, 106])
druid([375, 106], '051')
        '''],
        
        [470, '''
ace([716, 244], '204')
        '''],
        
        [675, '''
ace([716, 244], '205')
        '''],
        
        [700, '''
sniper([494, 90], '502')
        '''],
        [790, '''
ace([320, 271])
ace([320, 271], '502')
        '''],
    
        [825, '''
alchemist([300, 200])
alchemist([300, 200],'205')
        '''],
        
        [905, '''
buccaneer([430, 470])
buccaneer([430, 470], '520')
        '''],
        
        [960, '''
sub([157, 298])
sub([157, 298], '250')
        '''],
        
    ],
    
    # 工坊
    '工坊': [
        ['pre', '''
# 前置
hero([722, 380-32])
dart([1069, 445])
sniper([729, 300])
print('[%s] 狙击手 修改强力模式, !!用于顶住MOBA,不然就打小气球身上了!!' % get_datetime())
# click([729, 300])
key(Key.tab, times=3)
click(global_point_map['game_rightdown'], times=2, cd=0.1)
wizard([650, 344])
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
        '''],
        [20, '''
wizard([650, 344], '020')
        '''],
        [80, '''
spike([1130, 501])
spike([1130, 501], '002')

        '''],
        [105, '''
sniper([729, 300], '102')
        '''],
        [120, '''
spike([1130, 501], '203')
        '''],
        [190, '''
alchemist([1025, 585])
alchemist([1025, 585],'201')
        '''],
        [256, '''
village([692, 458])
village([692, 458], '102')
spike([1130, 501], '204')
tab(刺钉工厂,[1130, 501],3)
        '''],
        [300, '''
sniper([729, 300], '402')
        '''],
        [285, '''
village([692, 458], '203')
        '''],
        [325, '''
druid([633, 297])
druid([633, 297], '040')

        '''],
        
        [400, '''
spike([1130, 501], '205')
ace([748, 542])
druid([633, 297], '050')
        '''],
        
        [445, '''

ace([748, 542], '204')
        '''],
        
        [675, '''
ace([748, 542], '205')
        '''],
        
        [760, '''
sniper([729, 300], '502')
alchemist([1025, 585],'205')
        '''],
    ],
    
    # 方院
    '方院': [
        ['pre', '''
hero([738, 348])
dart([611, 223-32])  
dart([575, 629-32])
dart([291, 417-32])
sniper([732, 659])
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
# sub2([569, 468-32])
# wizard([671, 566])
# pilot([626, 609-32])
# buccaneer([634, 464-32])
        '''],
        [31, '''
sub([685, 424-32])
sub([685, 424-32], '202')
        '''],
        
        [120, '''
# end_time = time.time()
# if (end_time - start_time) < 90:
#     time.sleep(90 - (end_time - start_time)) # 阻塞差值秒数
ace([798, 410])
ace([798, 410], '103')
        '''],
        
        [156, '''
alchemist([769, 473])
alchemist([769, 473], '201')
ace([798, 410], '203')
sniper([732, 659], '102')
print('[%s] 狙击手 修改强力模式, !!用于破铅气球!!' % get_datetime())
click([732, 659])
key(Key.tab, times=3)
click(global_point_map['game_rightdown'], times=2, cd=0.5)
alchemist([769, 473], '401')
        '''],
        
        [240, '''
village([706, 513])
village([706, 513], '203')
        '''],
        [270, '''
druid([620, 531])
druid([620, 531], '050')
        '''],
        
        [480, '''
ace([893, 541])
ace([893, 541], '502')
        '''],
        
        [600, '''
# alchemist([769, 473], '205')

        '''],
        
        [780, '''
ace([798, 410], '205')
# 拆树, 全部
print('[%s]拆树' % get_datetime())
click(global_point_map['game_rightdown'], times=2)
time.sleep(1)
click([595, 180-32]) 
click(global_point_map['demolish'])
click([1046, 431-32])
click(global_point_map['demolish'])
click([596, 664-32])
click(global_point_map['demolish'])
click([107, 415-32])
click(global_point_map['demolish'])
spike([816, 626-32])
spike([816, 626-32], '250')
胶水=[胶水炮手,[442,250]]
fz_(*胶水)
up520(*胶水)
        '''],
        
    ],
    
    # 黑暗城堡
    '黑暗城堡': [
        ['pre', '''
hero([718, 300])
sub([791, 325-32])
sub([791, 325-32], '001')
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)

        '''],
        
        [40, '''
ace([544, 220-32])
ace([544, 220-32], '002')
        '''],
        
        [120, '''
ace([544, 220-32], '203')
        '''],
    
        [160, '''
alchemist([591, 258])
alchemist([591, 258], '200')
        '''],
        
        [182, '''
village([658, 235])
village([658, 235], '002')
        '''],
        
        [200, '''
pilot([665, 140])
time.sleep(5)
# 拆树
time.sleep(20)  
click(global_point_map['game_rightdown'], times=2, cd=0.2)

print('[%s] 拆1路树' % get_datetime())
click([176, 139-32])
click(global_point_map['demolish'])
pilot([665, 140], '302')
        '''],
        [280, '''
alchemist([591, 258], '400')
        '''],
        
        [330, '''
village([658, 235], '203')
        '''],
        
        [398, '''
# 拆三树
print('[%s] 拆下三路树' % get_datetime())
click(global_point_map['game_rightdown'], times=2, cd=0.2)
click([168, 316-32])
click(global_point_map['demolish'])
click([125, 513-32])
click(global_point_map['demolish'])
click([135, 675-32])
click(global_point_map['demolish'])
        '''],
        [410, '''
pilot([665, 140], '502')
        '''],
        
        [540, '''
ace([544, 220-32], '204')
        '''],
        
        [760, '''
ace([544, 220-32], '205')
        '''],
        
        [840, '''
alchemist([591, 258], '500')
        '''],
        [901, '''
alchemist([546, 311])
alchemist([546, 311],'205')
        '''],
    ],
    
    # 泥泞的水坑

    
    '泥泞的水坑': [
        ['pre', '''
hero([727, 331])
dart([352, 230])
sniper ([828, 532])
sniper([828, 532], '001')
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
        '''],
        
        [0, '''
sniper([828, 532], '022')
# print('[%s] 狙击手1 升级至002' % get_datetime())

        '''],
    
        [100, '''
sniper([828, 532], '023')
sniper([856, 586])
sniper([856, 586], '102')
# 修改强力模式

print('[%s] 狙击手2 修改强力模式, !!用于破铅气球!!' % get_datetime())
click([856, 586])
key(Key.tab, times=3)
click(global_point_map['game_rightdown'], times=2, cd=0.1)
alchemist([827, 498-32])
alchemist([827, 498-32], '201')
sniper([828, 532], '024')
        '''],
        
        [219, '''
village([846, 434-32])
village([846, 434-32], '202')
        '''],
        
        [230, '''
alchemist([827, 498-32], '401')
        '''],
        
        [320, '''
village([846, 434-32], '203')
        '''],
        
        [340, '''
pilot([747, 505-32])
pilot([747, 505-32], '402')
        '''],
        
        [470, '''
pilot([747, 505-32], '502')
        '''],
        
        [495, '''
ace([969, 508-32])
ace([969, 508-32], '204')
        '''],
        
        [780, '''
ace([969, 508-32], '205')
        '''],
        
        [785, '''
sub([889, 360-32])
sub([889, 360-32], '240')
        '''],
        
        [840, '''
sub([889, 360-32], '250')
        '''],
        
        [900, '''
alchemist([827, 498-32], '501')
        '''],
        
        [930, '''
sniper([676, 402-32])
sniper([676, 402-32], '502')
        '''],
        [960, '''
alchemist([778, 579-32])
alchemist([778, 579-32], '205')
        '''],

    ],
    
    # 哎哟
    '哎哟': [
        ['pre', '''
hero([483, 327-32])
sniper([486, 505-32])
sub([694, 420-32])
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
        '''],
        
        [36, '''
sub([694, 420-32], '202')
        '''],
        [115, '''
sniper([486, 505-32], '102')
        '''],
        [170, '''
village([382, 419-32])
village([382, 419-32], '102')
        '''],
        [170, '''
buccaneer([553, 415-32])
buccaneer([553, 415-32], '320')
        '''],
        [280, '''
village([382, 419-32], '203')
        '''],
        [305, '''
sniper([486, 505-32], '302')
        '''],
        [325, '''
ace([364, 342-32])
ace([364, 342-32], '203')
        '''],
        [347, '''
buccaneer([553, 415-32], '520')
        '''],
        [457, '''
druid([379, 492-32])
druid([379, 492-32], '050')
        '''],
        [535, '''
ace([364, 342-32], '204')
        '''],
        [735, '''
ace([364, 342-32], '205')
        '''],
        [802, '''
sub([553, 469-32])
sub([553, 469-32], '250')
        '''],
        [890, '''
alchemist([492, 350-32])
alchemist([492, 350-32], '420')
        '''],
        
        [926, '''
alchemist([492, 350-32], '520')
village([382, 419-32], '204')
        '''],
        
        [890, '''
spike([497, 249-32])
spike([497, 249-32], '250')
        '''],
    ],

'黑暗城堡放气': [
        ['pre', 
'''
village([719,224])
village([719, 224],'002')
# village([719,224], '203')
# village([719,224],'002')
village([634,220])
village([634, 220],'102')
# village([634,220],'102')
hero([676,307])
sub([774,294])
sub([774,294],'203')
sub([790,219])
sub([790,219],'203')
wizard([554,314])
wizard([554,314],'023')
alchemist([619,311])
alchemist([619,311],'401')
click([634,220])
key(Key.backspace)
click([719,224])
key(Key.backspace)
sub([790,219],'204')
sub([774,294],'204')
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
        ''']
        
    ],
'避难所放气': [
        ['pre', '''
sniper([579, 180])
sniper([579, 180],'025')
alchemist([633, 181])
alchemist([633, 181],'420')
village([596, 116])
village([596, 116],'230')
# 放置完毕开始
key(Key.space)
time.sleep(1)
key(Key.space)
        ''']
        
    ],
    'test': [
[
'''
# if map== '小木屋':
#  sawuda=[英雄,[410,37]]
#  dart=[飞镖猴,[770,79]]
#  tack=[图钉塔,[470,101]]
#  ice=[冰猴,[490,618]]
#  alchemist=[炼金术士,[394,152]]
#  village=[猴子村,[469,171]]

# ice=[冰猴,[]]
# dart=[飞镖猴,[]]
# sawuda=[英雄,[]]
# tack=[图钉塔,[]]
# alchemist=[炼金术士,[]]
# village=[猴子村,[]]

# # 猴子草荀
# dart=[飞镖猴,[171,280]]
# sawuda=[英雄,[346,366]]
# tack=[图钉塔,[472,271]]
# ice=[冰猴,[751,491]]
# alchemist=[炼金术士,[354,283]]
# village=[猴子村,[459,368]]

# # 树桩
# dart=[飞镖猴,[209,200]]
# sawuda=[英雄,[371,181]]
# tack=[图钉塔,[329,87]]
# ice=[冰猴,[1007,433]]
# alchemist=[炼金术士,[313,223]]
# village=[猴子村,[278,135]]

# # 旅游胜地
# ice=[冰猴,[252,534]]
# dart=[飞镖猴,[242,139]]
# sawuda=[英雄,[916,138]]
# tack=[图钉塔,[922,181]]
# alchemist=[炼金术士,[965,47]]
# village=[猴子村,[1059,166]]

# # 溜冰场
# ice=[冰猴,[932,651]]
# dart=[飞镖猴,[398,541]]
# sawuda=[英雄,[199,221]]
# tack=[图钉塔,[249,222]]
# alchemist=[炼金术士,[229,180]]
# village=[猴子村,[220,312]]

# # 莲花岛
# ice=[冰猴,[855,114]]
# dart=[飞镖猴,[921,716]]
# sawuda=[英雄,[625,659]]
# tack=[图钉塔,[676,649]]
# alchemist=[炼金术士,[723,631]]
# village=[猴子村,[699,563]]

# # 糖果瀑布
# ice=[冰猴,[985,199]]
# dart=[飞镖猴,[279,249]]
# sawuda=[英雄,[218,654]]
# tack=[图钉塔,[276,664]]
# alchemist=[炼金术士,[166,638]]
# village=[猴子村,[293,565]]

# # 冬季花园
# ice=[冰猴,[880,209]]
# dart=[飞镖猴,[880,567]]
# sawuda=[英雄,[301,197]]
# tack=[图钉塔,[250,192]]
# alchemist=[炼金术士,[300,149]]
# village=[猴子村,[285,280]]

# 鬼脸南瓜
ice=[冰猴,[778,156]]
dart=[飞镖猴,[303,250]]
sawuda=[英雄,[529,486]]
tack=[图钉塔,[597,473]]
alchemist=[炼金术士,[601,529]]
village=[猴子村,[568,385]]

# # 公园路径
# ice=[冰猴,[1064,358]]
# dart=[飞镖猴,[613,240]]
# sawuda=[英雄,[798,577]]
# tack=[图钉塔,[754,604]]
# alchemist=[炼金术士,[700,526]]
# village=[猴子村,[748,482]]



# 高山路径
# ice=[冰猴,[952,264]]
# dart=[飞镖猴,[516,78]]
# sawuda=[英雄,[394,449]]
# tack=[图钉塔,[341,426]]
# alchemist=[炼金术士,[348,482]]
# village=[猴子村,[397,334]]

# # 冰冻三尺
# ice=[冰猴,[992,349]]
# dart=[飞镖猴,[82,655]]
# sawuda=[英雄,[367,610]]
# tack=[图钉塔,[356,658]]
# alchemist=[炼金术士,[461,583]]
# village=[猴子村,[300,549]]

# # 循环
# ice=[冰猴,[407,209]]
# dart=[飞镖猴,[358,591]]
# sawuda=[英雄,[825,521]]
# tack=[图钉塔,[765,530]]
# alchemist=[炼金术士,[800,480]]
# village=[猴子村,[727,475]]

# # 立体主义
# ice=[冰猴,[986,498]]
# dart=[飞镖猴,[78,206]]
# sawuda=[英雄,[664,488]]
# tack=[图钉塔,[607,451]]
# alchemist=[炼金术士,[655,436]]
# village=[猴子村,[594,525]]


# 树篱
# ice=[冰猴,[1062,398]]
# dart=[飞镖猴,[499,214]]
# sawuda=[英雄,[123,403]]
# tack=[图钉塔,[227,401]]
# alchemist=[炼金术士,[224,450]]
# village=[猴子村,[119,474]]



# # 四个圈子
# ice=[冰猴,[563,655]]
# dart=[飞镖猴,[766,67]]
# sawuda=[英雄,[622,389]]
# tack=[图钉塔,[579,358]]
# alchemist=[炼金术士,[581,415]]
# village=[猴子村,[662,319]]

# 路的尽头
# ice=[冰猴,[1028,440]]
# dart=[飞镖猴,[190,428]]
# sawuda=[英雄,[158,330]]
# tack=[图钉塔,[297,276]]
# alchemist=[炼金术士,[162,216]]
# village=[猴子村,[280,373]]


# # 原木
# ice=[冰猴,[841,505]]
# dart=[飞镖猴,[238,201]]
# sawuda=[英雄,[351,496]]
# tack=[图钉塔,[419,501]]
# alchemist=[炼金术士,[344,415]]
# village=[猴子村,[415,395]]

# # 废料场
# ice=[冰猴,[1032,659]]
# dart=[飞镖猴,[161,601]]
# sawuda=[英雄,[483,440]]
# tack=[图钉塔,[477,483]]
# alchemist=[炼金术士,[481,395]]
# village=[猴子村,[582,473]]






# # 市中心
# dart=[飞镖猴,[296,610]]
# sawuda=[英雄,[407,322]]
# tack=[图钉塔,[413,233]]
# ice=[冰猴,[865,331]]
# alchemist=[炼金术士,[354,232]]
# village=[猴子村,[338,339]]







# # 小木屋
# sawuda=[英雄,[410,37]]
# dart=[飞镖猴,[770,79]]
# tack=[图钉塔,[470,101]]
# ice=[冰猴,[490,618]]
# alchemist=[炼金术士,[394,152]]
# village=[猴子村,[469,171]]


fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)

up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)

# 自动点击技能
# while True:
#  key("1")
#  time.sleep(1)
#  click([136,345])
#  time.sleep(1)
#  click([255,359])
#  time.sleep(2)
#  key("1")
#  time.sleep(1)
#  click([255,359])
#  time.sleep(1)
#  click([136,345])
''']]
    ,
'水淹山谷单金极难':[
'''
# 单金失败版本
sub([686,127])
key(Key.space)
time.sleep(1)
key(Key.space)
sub([732,558])
hero([264,580])
sub([686,127],'001')
sub([732,558],'001')
sub([686,127],'201')
sub([732,558],'201')
sniper([175,527])
click([175,527])
key(Key.tab, times=3)
sniper([175,527],'100')
# tab([],3)
sub([732,558],'202')
sniper([209,572])
sniper([209,572],'020')
sub([686,127],'202')
sniper([209,572],'022')
sniper([175,527],'102')
village([240,521])
village([240,521],'002')
sniper([175,527],'203')
sub([686,127],'402')
sniper([209,572],'032')
alchemist([191,481])
alchemist([191,481],'300')
village([240,521],'003')
village([240,521],'203')
sniper([175,527],'204')#又一g点
alchemist([191,481],'400')
sniper([209,572],'042')
sniper([128,536])
click([128,536])
key(Key.tab, times=3)
sniper([128,536],'020')
sniper([128,536],'420')#一g点
sniper([209,572],'052')
click([209,572])
key(Key.tab, times=1)
sub([732,558],'302')
sniper([175,527],'205')
click([175,527])
key(Key.tab, times=2)
alchemist([191,481],'500')
sniper([162,581])
sniper([162,581],'032')
sniper([115,586])
sniper([115,586],'032')
ace([278,430])
ace([278,430],'502')
'''
    ],
'炼狱极难单金':[
        ['pre','''
kunxi=[英雄,[600,501]]
sub=[猴子潜艇,[856,174]]
dart=[飞镖猴,[338,192]]
sniper2=[狙击手猴,[1100,424]]
sniper3=[狙击手猴,[1147,402]]
sniper1=[狙击手猴,[1083,383]]
sniper4=[狙击手猴,[1100,471]]
sniper5=[狙击手猴,[1147,496]]
alchemist=[炼金术士,[1147,449]]
vallage=[猴子村,[1128,341]]
fz_(*kunxi)
key(Key.space)
time.sleep(1)
key(Key.space)

fz_(*dart)
fz_(*sniper1)
tab(*sniper1,3)
up100(*sniper1)
fz_(*sub)
up202(*sub)
fz_(*vallage)
up002(*vallage)
fz_(*sniper2)
up002(*sniper2)
up032(*sniper2)
up102(*vallage)
up220(*sniper1)
fz_(*alchemist)
up401(*alchemist)
up203(*vallage)
up052(*sniper2)
tab(*sniper2,1)
up420(*sniper1)
# g点
up501(*alchemist)
fz_(*sniper3)
up005(*sniper3)
up025(*sniper3)
fz_(*sniper4)
up204(*sniper4)
fz_(*sniper5)
up022(*sniper5)
up520(*sniper1)


'''
]



    ],

'猴子草荀':['''

'''],
'猴子草荀':['''

'''],
'猴子草荀':['''

'''],
'猴子草荀':['''

'''],
'溜冰鞋单金':[['pre','''
buccaneer([561,429])
key(Key.space)
time.sleep(1)
key(Key.space)
buccaneer([624,387])
hero([530,513])
dart([110,264])
buccaneer([561,429],'022')
buccaneer([561,429],'023')
buccaneer([624,387],'023')
sniper([486,619])
sniper([486,619],'024')
buccaneer([683,339])
buccaneer([683,339],'023')
buccaneer([709,283])
buccaneer([709,283],'022')
buccaneer([712,205])
buccaneer([712,205],'022')
buccaneer([712,205],'024')
buccaneer([709,283],'024')
buccaneer([561,429],'024')
buccaneer([655,151])
buccaneer([581,168])
buccaneer([541,213])
buccaneer([559,342])
buccaneer([605,266])
buccaneer([624,387],'024')

# 升级024
buccaneer([683,339],'024')
buccaneer([709,283],'024')
buccaneer([655,151],'024')
pilot([750,536])
pilot([750,536],'230')
pilot([1003,711])
pilot([1003,711],'203')

buccaneer([581,168],'024')
buccaneer([541,213],'024')
buccaneer([559,342],'024')
sniper([486,619],'025')
pilot([1003,711],'204')
buccaneer([605,266],'025')
alchemist([226,214])
alchemist([224,320])
alchemist([239,382])
alchemist([275,455])
alchemist([342,499])
alchemist([345,423])
alchemist([330,351])
# 升级302
alchemist([226,214],'005')
alchemist([224,320],'032')
alchemist([239,382],'032')
alchemist([275,455],'032')
alchemist([342,499],'032')
alchemist([345,423],'032')
alchemist([330,351],'032')
village([348,246])
village([348,246],'230')
pilot([1003,711],'205')
spike([1109,575])
spike([1109,575],'205')
pilot([750,536],'240')
pilot([133,95])
pilot([133,95],'240')
# s=刷飞机
while True:
 key("3")
 time.sleep(2)
 click([110,264])
 time.sleep(2)
 click([68,300])
 time.sleep(2)
 key("3")
 time.sleep(2)
 click([68,300])
 time.sleep(2)
 click([110,264])
 time.sleep(2)
''']],
# #刷金气球打新手中级（标准）
'猴子草荀':[
['pre','''
dart=[飞镖猴,[171,280]]
sawuda=[英雄,[346,366]]
tack=[图钉塔,[472,271]]
ice=[冰猴,[751,491]]
alchemist=[炼金术士,[354,283]]
village=[猴子村,[459,368]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],


'树桩':[
['pre','''
dart=[飞镖猴,[209,200]]
sawuda=[英雄,[371,181]]
tack=[图钉塔,[329,87]]
ice=[冰猴,[1007,433]]
alchemist=[炼金术士,[313,223]]
village=[猴子村,[278,135]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'市中心':[
['pre','''
dart=[飞镖猴,[296,610]]
sawuda=[英雄,[407,322]]
tack=[图钉塔,[413,233]]
ice=[冰猴,[865,331]]
alchemist=[炼金术士,[354,232]]
village=[猴子村,[338,339]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'废料场':[
['pre','''
ice=[冰猴,[1032,659]]
dart=[飞镖猴,[161,601]]
sawuda=[英雄,[483,440]]
tack=[图钉塔,[477,483]]
alchemist=[炼金术士,[481,395]]
village=[猴子村,[582,473]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],

'小木屋':[
['pre','''
sawuda=[英雄,[410,37]]
dart=[飞镖猴,[770,79]]
tack=[图钉塔,[470,101]]
ice=[冰猴,[490,618]]
alchemist=[炼金术士,[394,152]]
village=[猴子村,[469,171]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],

'度假胜地':[
['pre','''
ice=[冰猴,[252,534]]
dart=[飞镖猴,[242,139]]
sawuda=[英雄,[916,138]]
tack=[图钉塔,[922,181]]
alchemist=[炼金术士,[965,47]]
village=[猴子村,[1059,166]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'度假胜地点击':[
['pre','''
tack=[图钉塔,[938,159]]
startgame(2)
spike=[刺钉工厂,[1100,142]]
fz_(*tack)
up101(*tack)
fz_(*spike)
up002(*spike)
tab(*spike,3)
up202(*tack)
up103(*spike)
up302(*tack)
up204(*spike)
up402(*tack)
up205(*spike)
up502(*tack)
tab(*tack,3)
''']],

'溜冰鞋':[
['pre','''
ice=[冰猴,[932,651]]
dart=[飞镖猴,[398,541]]
sawuda=[英雄,[199,221]]
tack=[图钉塔,[249,222]]
alchemist=[炼金术士,[229,180]]
village=[猴子村,[220,312]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'莲花岛':[
['pre','''
ice=[冰猴,[855,114]]
dart=[飞镖猴,[921,716]]
sawuda=[英雄,[625,659]]
tack=[图钉塔,[676,649]]
alchemist=[炼金术士,[723,631]]
village=[猴子村,[699,563]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'糖果瀑布':[
['pre','''

ice=[冰猴,[985,199]]
dart=[飞镖猴,[279,249]]
sawuda=[英雄,[218,654]]
tack=[图钉塔,[276,664]]
alchemist=[炼金术士,[166,638]]
village=[猴子村,[293,565]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'冬季公园':[
['pre','''
ice=[冰猴,[880,209]]
dart=[飞镖猴,[880,567]]
sawuda=[英雄,[301,197]]
tack=[图钉塔,[250,192]]
alchemist=[炼金术士,[300,149]]
village=[猴子村,[285,280]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'鬼脸南瓜':[
['pre','''
ice=[冰猴,[778,156]]
dart=[飞镖猴,[303,250]]
sawuda=[英雄,[529,486]]
tack=[图钉塔,[597,473]]
alchemist=[炼金术士,[601,529]]
village=[猴子村,[568,385]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'公园路径':[
['pre','''
ice=[冰猴,[1064,358]]
dart=[飞镖猴,[613,240]]
sawuda=[英雄,[798,577]]
tack=[图钉塔,[754,604]]
alchemist=[炼金术士,[700,526]]
village=[猴子村,[748,482]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'高山竞速':[
['pre','''
ice=[冰猴,[952,264]]
dart=[飞镖猴,[516,78]]
sawuda=[英雄,[394,449]]
tack=[图钉塔,[341,426]]
alchemist=[炼金术士,[348,482]]
village=[猴子村,[397,334]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'冰冻三尺':[
['pre','''
ice=[冰猴,[992,349]]
dart=[飞镖猴,[82,655]]
sawuda=[英雄,[367,610]]
tack=[图钉塔,[356,658]]
alchemist=[炼金术士,[461,583]]
village=[猴子村,[300,549]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'循环':[
['pre','''
ice=[冰猴,[407,209]]
dart=[飞镖猴,[358,591]]
sawuda=[英雄,[825,521]]
tack=[图钉塔,[765,530]]
alchemist=[炼金术士,[800,480]]
village=[猴子村,[727,475]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'立体主义':[
['pre','''
ice=[冰猴,[986,498]]
dart=[飞镖猴,[78,206]]
sawuda=[英雄,[664,488]]
tack=[图钉塔,[607,451]]
alchemist=[炼金术士,[655,436]]
village=[猴子村,[594,525]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'树篱':[
['pre','''
ice=[冰猴,[1062,398]]
dart=[飞镖猴,[499,214]]
sawuda=[英雄,[123,403]]
tack=[图钉塔,[227,401]]
alchemist=[炼金术士,[224,450]]
village=[猴子村,[119,474]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'四个圈子':[
['pre','''
ice=[冰猴,[563,655]]
dart=[飞镖猴,[766,67]]
sawuda=[英雄,[622,389]]
tack=[图钉塔,[579,358]]
alchemist=[炼金术士,[581,415]]
village=[猴子村,[662,319]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'路的尽头':[
['pre','''
ice=[冰猴,[1028,440]]
dart=[飞镖猴,[190,428]]
sawuda=[英雄,[158,330]]
tack=[图钉塔,[297,276]]
alchemist=[炼金术士,[162,216]]
village=[猴子村,[280,373]]

fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],
'原木':[
['pre','''
ice=[冰猴,[841,505]]
dart=[飞镖猴,[238,201]]
sawuda=[英雄,[351,496]]
tack=[图钉塔,[419,501]]
alchemist=[炼金术士,[344,415]]
village=[猴子村,[415,395]]


fz_(*sawuda)
startgame()
fz_(*dart)
fz_(*tack)
fz_(*ice)
up002(*ice)
fz_(*alchemist)
up201(*alchemist)
up204(*tack)
up203(*ice)
up401(*alchemist)
up205(*tack)
fz_(*village)
up030(*village)
''']],


}
