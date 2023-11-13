import ctypes#C语言类型
import sys
def is_admin():#win7兼容性版本，管理员模式运行会有生成临时文件，结束程序却没有删除的bug，放在开始可以提高运行效率
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    print("已使用管理员权限运行脚本，使用win7版会出现生成临时文件，程序结束却没删除的bug")
    # 将要运行的代码加到这里
else:
    print("未使用管理员权限运行脚本，保证点击时不被自己鼠标干扰请获取权限")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit(0)

# 存储初始化变量
signal_blocking = [] 
signal_blocking_thread = [] 
blocking_time = 25
origin = [0, 0]
w_h = [0, 0]  # 宽高.

# 关键地图点位
global_point_map = {
    'cancel': [554,514],
    'home_hero':[433,702-32],#主页英雄
    'map_hero':[77,704],

    'map_etn':[291,603-32],
    'map_psi':[182,684],
    'map_quincy':[77,159],
    'map_select':[800,471-32],
    'map_sauda':[77,701],
    '任意英雄':[1364, 406],
    '昆西':[77,159],
    '格温多琳':[175,154],
    '琼斯':[291,154],

    '奥本':[73, 291],
    '丘吉尔':[175,291],
    '本杰明':[291,291],

    '艾泽里':[77,427],  
    '帕特':[175,427],
    '阿拉多':[286,427],

    '布里克尔':[77,573],   
    '艾蒂安':[179,603-32],
    '萨乌达':[291,573],

    '灵机':[77,701],
    '杰拉尔多':[175,701],

    'map_select':[800,471-32],
    'map_heroback':[53,71-32],
    'start': [583, 683-32],

    's1': [412,689],#以后弃了
    's2': [598,698],
    's3': [765, 712-32],
    's4': [944, 711-32],

    'beginner': [412,689],
    'intermediate': [598,698],
    'advanced': [765, 680],
    'expert': [944, 680],

    'map_1': [391, 221-32],
    'map_2': [688, 214-32],
    'map_3': [987, 221-32],
    'map_4': [388, 441-32],
    'map_5': [687, 432-32],
    'map_6': [988, 444-32],

    'simple': [447, 317-32],  # 以后弃了
    'easy': [447, 285],
    'medium':[687,365],
    'difficulty': [921, 324-32],#以后弃了
    'hard': [921, 292],

    'standard':[449,408],
    'deflation': [916, 313],  # 放气
    'imp': [909, 559-32],#以后弃了
    'impoppable': [909, 527],
    'chimps':[1150,520],

    'cover': [801, 547-32],
    'yes1': [679, 566-32],  # 开始之后的提示 好的
    'setting_home': [601, 602], #暂停时出现的回到主页
    'back_home': [600, 600],  # 打完之后战绩表 下一页
    'next_page': [677, 671-32],  # 打完之后战绩表 下一页
    'over_home': [496, 630-32],
    # 'fail_home': [597, 557], #失败时回到主页的位置
    'fail_home': [401, 557], #失败时回到主页的位置
    'fail_home_chimps':[501,577],#点击失败回到主页的位置

    #循环单图的点位：
    'fail_restart': [591,557],#失败重新开始
    'fail_restart_chimps': [671,557],#最低636
    'restart_confirm':[816,518],
    'free_game':[866,600],#直接重新开始的操作
    # 'free_game':[866,597],#直接重新开始的操作
    'setting':[1142,32],
    'setting_restart':[761,600],

    'window_Bottom_right': [1366, 768],#窗口最右下角
    'home_empty1': [184, 533-32],  # 左边偏下角
    'home_empty2': [538, 552-32],  # 开始左上方点
    'home_empty3': [1003, 737-32],  # 页面右下角空白处
    'home_empty4': [238, 537-32],  # 页面猴子上面空白处
    'game_empty1': [985, 650-32],
    'game_empty2': [612, 650-32],
    'game_rightdown': [1161, 741],  # 游戏页面右边下面空白处
    'game_right': [1364, 406], #猴子页面右边边上空白处
    'game_center':[611,416],

    'demolish': [657, 420],#拆除障碍物
    'upgrade':[661,348],#升级和知识点的的位置
    'use':[448,555],#号在其他地方被登自动点左边的本地存档
    'collection': [675, 506-32],
    'left_': [572, 395-32],
    'right_': [784, 382-32],
    'return': [49, 64-32],
    'fail_check_map': [775, 604-32],  # 查看地图
    'fail_checkmap_chimps':[867,580],#点击失败回到主页的位置
    'fail_check_map_right': [1258, 682],  # 右下角地图图标
    # 合作模式挂机

    'play_social':[772,660],
    'quick_match':[253,318],
    'any_game':[448,255],
    'go!':[694,715],
    'exchange':[1123,150],
    'givemoney1':[1123,200],
    'givemoney2':[1123,334],
    'givemoney3':[1123,458],
    #竞速模式：发送下一回合快捷键为Shift
}
page_position={#地图页数点位
'1':[526,538],
'2':[552,538],
'3':[578,538],
'4':[604,538],
'5':[630,538],
'6':[656,538],
'7':[682,538],
'8':[708,538],
'9':[734,538],
'10':[760,538],
'11':[786,538],
'12':[812,538],
'13':[838,538],
}
page_click={#地图页数点位
'1':['beginner',1],
'2':['beginner',2],
'3':['beginner',3],
'4':['beginner',4],
'5':['intermediate',1],
'6':['intermediate',2],
'7':['intermediate',3],
'8':['intermediate',4],
'9':['advanced',1],
'10':['advanced',2],
'11':['advanced',3],
'12':['expert',1],
'13':['expert',2],
}

mode_click={#难度点位
'简单':['simple','standard'],
'仅初级':['easy',538],
'放气':['easy','deflation'],
'中级':['medium','standard'],
'仅限军事':[812,538],
'天启':[838,538],
'相反':[838,538],
'困难':[838,538],
'只限魔法猴':[838,538],
'双倍生命MOAB':[838,538],
'一半现金':[838,538],
'替代气球回合':[838,538],
'困难':['hard','standard'],
'极难':['hard','impoppable'],
'点击':['hard','chimps'],

}
# 打算存储地图的坐标信息，识别更加坐标的位置，再设立一个函数读取地图的坐标信息，进行点击
map_area={#地图页数点位
'map_1':[[288, 98], [531, 281]],
'map_2':[[594, 98], [830, 281]],
'map_3':[[895, 130-32], [1137, 313]],
'map_4':[[290, 352-32], [528, 540]],
'map_5':[[597, 349-32], [831, 540]],
'map_6':[[891, 349-32], [1135, 540]],
}


map_info={
    '猴子草甸': ['1', 'map_1',],
    '循环': ['1', 'map_2',],
    '道路中间': ['1', 'map_3',],
    '树桩': ['1', 'map_4',],
    '市中心': ['1', 'map_5',],
    '一二三': ['1', 'map_6',],
    
    '废料场': ['2', 'map_1',],
    '小木屋': ['2', 'map_2',],
    '度假胜地': ['2', 'map_3',],
    '溜冰鞋': ['2', 'map_4',],
    '莲花岛': ['2', 'map_5',],
    '糖果瀑布': ['2', 'map_6',],

    '冬季公园': ['3', 'map_1',],
    '鬼脸南瓜': ['3', 'map_2',],
    '公园路径': ['3', 'map_3',],
    '高山竞速': ['3', 'map_4',],
    '冰冻三尺': ['3', 'map_5',],
    '立体主义': ['3', 'map_6',],

    '四个圈子': ['4', 'map_1',],
    '树篱': ['4', 'map_2',],
    '路的尽头': ['4', 'map_3',],
    '原木': ['4', 'map_4',],

    #中级图
    '水上乐园': ['5', 'map_1',],
    '独眼巨人': ['5', 'map_2',],
    '隐蔽的花园': ['5', 'map_3',],
    '采石场': ['5', 'map_4',],
    '静谧街道': ['5', 'map_5',],
    '布隆纳留斯精英': ['5', 'map_6',],

    '平衡': ['6', 'map_1',],
    '已加密': ['6', 'map_2',],
    '集市': ['6', 'map_3',],
    '阿多拉神庙': ['6', 'map_4',],
    '复活节春天': ['6', 'map_5',],
    '飞镖卡丁车': ['6', 'map_6',],

    '登月': ['7', 'map_1',],
    '鬼屋': ['7', 'map_2',],
    '顺流而下': ['7', 'map_3',],
    '靶场': ['7', 'map_4',],
    '龟裂之地': ['7', 'map_5',],
    '河床': ['7', 'map_6',],

    '滑槽': ['8', 'map_1',],
    '耙': ['8', 'map_2',],
    '香料群岛': ['8', 'map_3',],
    #高级图
    '黑暗之径': ['9', 'map_1',],
    '侵蚀': ['9', 'map_2',],
    '午夜豪宅': ['9', 'map_3',],
    '凹陷的柱子': ['9', 'map_4',],
    'x因子': ['9', 'map_5',],
    '梅萨': ['9', 'map_6',],

    '齿轮传动': ['10', 'map_1',],
    '泄洪道': ['10', 'map_2',],
    '货运': ['10', 'map_3',],
    '帕特的池塘': ['10', 'map_4',],
    '半岛': ['10', 'map_5',],
    '高级金融': ['10', 'map_6',],

    '另一块砖': ['11', 'map_1',],
    '海岸': ['11', 'map_2',],
    '玉米地': ['11', 'map_3',],
    '地下': ['11', 'map_4',],

    '黑暗地下城': ['12', 'map_1',],
    '避难所': ['12', 'map_2',],
    '峡谷': ['12', 'map_3',],
    '水淹山谷': ['12', 'map_4',],
    '炼狱': ['12', 'map_5',],
    '血腥水坑': ['12', 'map_6',],
    
    '工坊': ['13', 'map_1',],
    '方院': ['13', 'map_2',],
    '黑暗城堡': ['13', 'map_3',],
    '泥泞的水坑': ['13', 'map_4',],
    '#哎哟': ['13', 'map_5',],
}




threadlist={
'game_thread':{#创建一个字典存储游戏各线程信息，用于游戏结束一次性终止

},
'script_thread':{'key_monitor':'',}
}


variable_list={#初始化变量
'chain':'',
'mode':'',
'selectedhero':'',
'width':'',
'script_mode':'',
'restart':'0',
'getedposition':[-1,-1],
'5阶insta数':0,
'position_test':False,
'getmouse':True
}

image_path={
}

image_originpath=['unclear','home','cancel','upgrade','monkey_book','local_record','fail','restart','continue','insta','restart','continue','insta','next_page','cover','freegame','collected','collection_button','social','social_full','box','instawanted','instawanted2','instawanted3','extra','goldbloon','sale','exit_cancel','insta_4','insta_5','confirm','tab_button',
                  
                  ]#以后打算自动获取

def get_resource_path(relative_path):#
    '''访问生成的临时文件夹的文件'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

import cv2

def cv_imread(file_path):#用此方法来读取带中文路径的图片
    root_dir, file_name = os.path.split(file_path)
    pwd = os.getcwd()
    if root_dir:
        os.chdir(root_dir)
    cv_img = cv2.imread(file_name)
    os.chdir(pwd)
    return cv_img

# def refresh_images_path():
#     def defimages_path(path):
#         image_path[path]=cv_imread(get_resource_path('src\images\%s\%s.png'%(variable_list['width'],path)))
#         # print(cv_imread(get_resource_path('src\images\%s\%s.png'%(variable_list['width'],path))))
#     for path in image_originpath:
#         defimages_path(path)
def refresh_images_path():
    try:
        def defimages_path(path):
                # image_path[path]=get_resource_path('src\images\%s\%s.png'%(variable_list['width'],path))
                image_path[path]=cv_imread(get_resource_path('src\images\%s\%s.png'%(variable_list['width'],path)))
                # image_path[path]='src\images\%s\%s.png'%(variable_list['width'],path)
            # print(cv_imread(get_resource_path('src\images\%s\%s.png'%(variable_list['width'],path))))
        for path in image_originpath:
            defimages_path(path)
    except Exception as e:
            print('检测到的游戏宽度为：%s,脚本未对该游戏尺寸做匹配,请调整游戏尺寸'%variable_list['width'])
            time.sleep(10)



# 存储需要用的模块
# import ctypes#C语言类型
import win32gui#界面
import ctypes.wintypes
user32=ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
dc = user32.GetDC(None)
variable_list['scale']=width = gdi32.GetDeviceCaps(dc, 118)/gdi32.GetDeviceCaps(dc, 8)

import time
import math
import os
import copy
import configparser
import sys
from pynput.keyboard import Key, Controller, Listener
import pynput.mouse as pm
from datetime import datetime
from ctypes import *
import threading
from chains_map import *
import pyautogui#这个库会影响到获取应用缩放

# import pymem
import win32con




keyboard = Controller()
# 信息存储
queue_infos = {
    'exec_times': 0,
    'fail_times': 0,
    'rest':0,
    'script_start_time': datetime.now(),
    
    'level_point_position_left': {
    
    },
    
    'level_point_position_right': {
    
    },
    
    # 技能点三十个点的坐标, 实在找不到就用default了
    'level_point_position_left_default': {
        'top': [[40, 313], [40, 330], [40, 347], [40, 366], [40, 383]],
        'middle': [[40, 419], [40, 436], [40, 453], [40, 472], [40, 489]],
        'bottom': [[40, 525], [40, 542], [40, 559], [40, 578], [40, 595]]
    },
    
    'level_point_position_right_default': {
        'top': [[908, 313], [908, 330], [908, 347], [908, 366], [908, 383]],
        'middle': [[908, 419], [908, 436], [908, 453], [908, 472], [908, 489]],
        'bottom': [[908, 525], [908, 542], [908, 559], [908, 578], [908, 595]]}
    }
level_status_position = {
    'skill1': [
        [195, 346], [1062, 346]
    ],

    'skill2': [
        [195, 452], [1062, 452],
    ],
    'skill3': [
        [195, 559], [1062, 559]
    ]
                # 左右2差969
    

}


# 获取自定义变量

skill1 = ','
skill2 = '.'
skill3 = '/'
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
BASE_DIR=os.path.dirname(os.path.realpath(sys.argv[0]))
sys.path.append(BASE_DIR)
# 还需要添加外加py外加
# if not os.exists(extension):
#                 os.makedirs(extension)
# from extension import *
# curpath = os.path.dirname(os.path.realpath(__file__))
settings = os.path.join(BASE_DIR, "热键设置.ini")
# 还需要添加文件不存在时添加配置好的ini文件
# 创建管理对象
try:
# 创建管理对象
    conf = configparser.ConfigParser()
    conf.add_section("monkoy")
    conf.add_section("skill")
    conf.set("","","")
    # 读ini文件
    conf.read(settings, encoding="utf-8")

    skill1=eval(conf.get("skill","top"))
    skill2=eval(conf.get("skill","middle"))
    skill3=eval(conf.get("skill","buttom"))
    #需要补充
    英雄=eval(conf.get("monkey","英雄"))

    飞镖猴=eval(conf.get("monkey","飞镖猴"))
    回旋镖猴=eval(conf.get("monkey","回旋镖猴"))
    大炮=eval(conf.get("monkey","大炮"))
    图钉塔=eval(conf.get("monkey","图钉塔"))
    冰猴=eval(conf.get("monkey","冰猴"))
    胶水炮手=eval(conf.get("monkey","胶水炮手"))

    狙击手猴=eval(conf.get("monkey","狙击手猴"))
    猴子潜艇=eval(conf.get("monkey","猴子潜艇"))
    海盗猴=eval(conf.get("monkey","海盗猴"))
    皇家飞行员=eval(conf.get("monkey","皇家飞行员"))
    直升机飞行员=eval(conf.get("monkey","直升机飞行员"))
    迫击炮猴=eval(conf.get("monkey","迫击炮猴"))
    机枪猴=eval(conf.get("monkey","机枪猴"))

    法师猴=eval(conf.get("monkey","法师猴"))
    超猴侠=eval(conf.get("monkey","超猴侠"))
    忍者猴=eval(conf.get("monkey","忍者猴"))
    炼金术士=eval(conf.get("monkey","炼金术士"))
    德鲁伊=eval(conf.get("monkey","格鲁伊"))
    
    香蕉农场=eval(conf.get("monkey","香蕉农场"))
    工程师猴=eval(conf.get("monkey","工程师猴"))
    刺钉工厂=eval(conf.get("monkey","刺钉工厂"))
    猴子村=eval(conf.get("monkey","猴子村"))
except Exception as e:#这个和excpt是有区别的 用except会出问题
    pass




# 定义函数
class thread_with_exception(threading.Thread):
    def __init__(self, func, args=(), name='', deamon=True):
        threading.Thread.__init__(self)
        self.daemon = deamon
        self.name = name
        self.func = func
        self.args = args
    
    def run(self):
        self.func(*self.args)

    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
    
    def raise_exception(self):
        thread_id = self.get_id()
        # print('[%s]线程中止: %s, 名称: %s' % (get_datetime(), thread_id, self.name))
        # 精髓就是这句话，给线程发过去一个exceptions，线程就那边响应完就停了
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
            print('res')
        






def test(n=1):#定义debug代码
    print('test%s'%n)

def is_admin():#win7兼容性版本，管理员模式运行会有生成临时文件，结束程序却没有删除的bug
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    print("已使用管理员权限运行脚本，使用win7版会出现生成临时文件，程序结束却没删除的bug")
    # 将要运行的代码加到这里
else:
    print("未使用管理员权限运行脚本，保证点击时不被自己鼠标干扰请获取权限")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit(0)





def run_thread(function,fucpara='',name='', deamon=True,type="game_thread"):#定义用线程运行功能的函数

    try:#同名的线程同时运行2个 ，当前情况，前一个线程不知道怎么终止
        threadlist[type][var_name(function)].raise_exception()
    except Exception as e:
            pass

    threadlist[type][var_name(function)] = thread_with_exception(function,fucpara,name,deamon)
    threadlist[type][var_name(function)].start()



def end_thread(function,type="game_thread"):#终止线程
    # while True:
        try:
            thread=threadlist[type][var_name(function)]
            if thread != '':
                thread.raise_exception()
            # print("线程结束")
            # if thread:
            #     break

        except Exception as e:
            # print('[%s]终结线程失败,%s' % (get_datetime(), e))
            pass


# 按键监听函数
def key_monitor():
    with Listener(on_press=on_press) as listener:
        listener.join()


def on_press(key):
    global signal_blocking
    if str(key) == r"'\x02'":
        
        # Ctrl+B  暂停脚本
        print('[%s] 检测到按键 Ctrl + B, 停止脚本' % (get_datetime()))
        signal_blocking.clear()
        signal_blocking.append(time.time())
        
    
    if str(key) ==r"'\x04'":
        # Ctrl+D  继续脚本
        print('[%s] 检测到按键 Ctrl + D, 继续脚本' % get_datetime())
        signal_blocking.clear()
        signal_blocking.append(0)
        #防止恢复失败
        time.sleep(2)
        signal_blocking.clear()
        signal_blocking.append(0)
        time.sleep(2)
        signal_blocking.clear()
        signal_blocking.append(0)
    if str(key) == r"'\r'":
        # Ctrl+M 退出程序, 给 while True?
        print('[%s] 检测到按键 Ctrl + M, 结束程序' % get_datetime())
        os._exit(0)  # 用在fork出来的线程中, 结束整个程序

def timesleep(ctime):#停止脚本所有进程
    print('[%s] 停止脚本%s秒' % (get_datetime(),ctime))
    signal_blocking.clear()
    signal_blocking.append(time.time()-999999+ctime)

def block(ctime=999999):#判断并执行阻塞的函数ctime为停止的时长
    if signal_blocking[:1]:
        blk = math.ceil(time.time() - signal_blocking[0])#时间差
        
        if blk < ctime:
            while True:
                # time.sleep(1)
                
                # 没有值或者等于0的时候
                if not signal_blocking or signal_blocking[0] == 0:
                    break
                    
                blk = math.ceil(time.time() - signal_blocking[0])
                if blk >= ctime:
                    break

def blockthread(ctime=999999):#判断并执行阻塞的函数ctime为停止的时长
    if signal_blocking_thread[:1]:
        blk = math.ceil(time.time() - signal_blocking_thread[0])#时间差
        
        if blk < ctime:
            while True:
                # time.sleep(1)
                
                # 没有值或者等于0的时候
                if not signal_blocking_thread or signal_blocking_thread[0] == 0:
                    break
                    
                blk = math.ceil(time.time() - signal_blocking_thread[0])
                if blk >= ctime:
                    break

def get_datetime():
    return datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
def var_name(var,all_var=locals()):
    return [var_name for var_name in all_var if all_var[var_name] is var][0]



# def get_origin(is_init=False):
#     global origin
#     scale=variable_list['scale']
#     # print(scale)
#     if scale==1:
#         p=8
#     elif scale==1.25:
#         p=9
#     elif scale==1.5:
#         p=11
#     elif scale==1.75:
#         p=12
#     elif scale==2.25:
#         p=14
#     else:
#         p=int(5+scale*4)
#         print('你当前电脑的应用缩放，脚本未做匹配可能会出现问题，请使用常规的应用缩放')
#     # print(p)
#     while True:
#         if win32gui.FindWindow(None, "BloonsTD6")==0 and win32gui.FindWindow(None, "BloonsTD6-Epic")==0:
#             l, t, r, b =0,0,0,0
#         elif win32gui.FindWindow(None, "BloonsTD6-Epic")!=0:
#             l, t, r, b = win32gui.GetWindowRect(win32gui.FindWindow(None, "BloonsTD6-Epic"))
#         else:
#             l, t, r, b = win32gui.GetWindowRect(win32gui.FindWindow(None, "BloonsTD6"))


#         variable_list['width']=r-l-2*p
#         if variable_list['width']==1366:
#             coordinates = [l+p, b - 768-p] #之前的坐标都少往左边偏，这是1920*1080 100%缩放
#         else:
#             coordinates = [l+p, b - variable_list['width']*9/16-p]


#         if coordinates[0] <10 and coordinates[1] < 0:
#             print('[%s]获取原点坐标失败,可能是窗口最小化,请打开游戏窗口' % get_datetime())
#             # time.sleep(1)
#             # # 暂停脚本
#             # signal_blocking.clear()
#             # signal_blocking.append(time.time())
#             if not is_init:
#                 break

#         else:
#             # if is_init:
#             #     print('[%s]获取原点坐标成功: %s' % (get_datetime(), coordinates))
#             # else:
#             #     if coordinates[0] != origin[0] or coordinates[1] != origin[1]:
#             #         # print('[%s]检测到窗口移动,更新游戏画面原点坐标: %s, 窗口边框高度: %s' % (get_datetime(), coordinates, int(deviation)))
#             #         print("[%s]检验的游戏画面宽度为: %s"% (get_datetime(),variable_list['width']),
#             #         # '如果不是1366*768的游戏尺寸,请更换图片或游戏尺寸',
#             #         '如果不是游戏的尺寸，则修改显示器分辨率或者应用缩放'
#             #         )

#             origin.clear()
#             origin.extend(coordinates)
    
#             break

def get_origin(is_init=False):#初始化不要了
    global origin
    # scale=variable_list['scale']##老旧坐标获取（弃了）
    # # print(scale)

    # if scale==1:#根据应用缩放偏移坐标#这个目前没问题
    #     p=8
    # elif scale==1.25:
    #     p=9
    # elif scale==1.5:#貌似这个有问题
    #     p=11
    # elif scale==1.75:
    #     p=12
    # elif scale==2.25:
    #     p=14
    # else:
    #     p=int(5+scale*4)
    #     print('你当前电脑的应用缩放，脚本未做匹配可能会出现问题，请使用常规的应用缩放')
    if win32gui.FindWindow(None, "BloonsTD6")==0 and win32gui.FindWindow(None, "BloonsTD6-Epic")==0:
        # print('未检测到游戏窗口，请打开游戏')
        l, t, r, b =0,0,0,0
        variable_list['hwnd']=False
        print('[%s] 游戏未打开，请打开游戏后，按ctrl+d继续脚本' % get_datetime())
        signal_blocking.clear()
        signal_blocking.append(time.time())
    elif win32gui.FindWindow(None, "BloonsTD6-Epic")!=0:
        variable_list['hwnd'] = win32gui.FindWindow(None, "BloonsTD6-Epic")
        l, t, r, b = win32gui.GetWindowRect(win32gui.FindWindow(None, "BloonsTD6-Epic"))
    else:
        variable_list['hwnd'] = win32gui.FindWindow(None, "BloonsTD6")
        l, t, r, b = win32gui.GetWindowRect(win32gui.FindWindow(None, "BloonsTD6"))
    win32gui.ShowWindow(variable_list['hwnd'], win32con.SW_SHOWNORMAL)#打开游戏窗口


    
    if r-l>=1362 and r-l<=1500:
        variable_list['width']=1366
        coordinates = [l+(r-l-1366)/2, b - 768-(r-l-1366)/2]
    elif r-l>=1270 and r-l<1400:
        variable_list['width']=1280
        coordinates = [l+(r-l-1280)/2, b - variable_list['width']*9/16-(r-l-1280)/2]
    elif r-l>=1590 and r-l<=1800:
        variable_list['width']=1600
        coordinates = [l+(r-l-1600)/2, b - variable_list['width']*9/16-(r-l-1600)/2]
    else:
        # print('[%s]检测到你的游戏宽度为%s 脚本未适配你使用的游戏尺寸' % (get_datetime(),r-l))
        variable_list['width']=r-l-2*8
        coordinates = [l+8, b - variable_list['width']*9/16-8]
    # variable_list['width']=r-l-2*p##老旧坐标获取（弃了）
    # if variable_list['width']==1366:
    #     coordinates = [l+p, b - 768-p] #之前的坐标都少往左边偏，这是1920*1080 100%缩放
    # else:
    #     coordinates = [l+p, b - variable_list['width']*9/16-p]

    origin.clear()
    origin.extend(coordinates)



def tranposition(x,y,no_origin=False):#转化坐标单独弄出来，因为不只点击需要用到想到坐标
    if not no_origin:
        
        refresh_images_path()
        if variable_list['width'] ==1366:
            x = origin[0] + round(x)
            y = origin[1] + round(y)#防止去负数时的逆向取整
        elif variable_list['width'] ==1280:#版本2
            x = origin[0] + x*0.938-0.35#0.937<k<0.939 #  小于绝对是对的，大
            y = origin[1] + y*0.937-0.1#+0.3101#y*0.9374+0.3101#0.9374<k<0.938#y轴不会自动匹配可用点还是0.941偏小 0.941<k<0.943 大 357偏大
        elif variable_list['width'] ==1600:
            # x = origin[0] + ((x-18)*1347/1149)+21 #
            x = origin[0] + (x*1.174)-1  #1600/1369
            y = origin[1] + (y)*1.173
        # print(x,y)
        return round(x),round(y)#x,y
    
    elif no_origin==True:
        return round(x),round(y)#x,y
    else:#以x，y为原点
        if variable_list['width'] ==1366:
            x = no_origin[0] + x
            y = no_origin[1] + y
        elif variable_list['width'] ==1280:#版本2
            x = x + (no_origin[0]*1280/1364) #1280/1364<k<1280/1364
            y = y + (no_origin[1]*(720)/769)+1 #750/770<k<720/769 #偏小
        elif variable_list['width'] ==1600:
            # x = origin[0] + ((x-18)*1347/1149)+21 #
            x = x + (no_origin[0]*1600/1370)+3  #1600/1369
            y = y + (no_origin[1])*899/767
            # print(x,y)
        return round(x),round(y)#x,y

def recordmouse():#这对函数组合防止坐标错乱，必须在返回后再记录
    if variable_list['getmouse']:
        variable_list['mouse_positon']= pyautogui.position()
        variable_list['getmouse']=False
def backmouse():
    pyautogui.moveTo(variable_list['mouse_positon'])
    variable_list['getmouse']=True
    


def click(coordinates, times=1, cd=0.5, dbl=False, no_origin=False,no_return=False):
    # 点击函数
    global signal_blocking
    
    block()
    if variable_list['getmouse']:
        variable_list['mouse_positon']= pyautogui.position()#存储原来的位置,换为字典存储
    variable_list['getmouse']=True
    if isinstance(coordinates[1], str):
        coordinates = coordinates[0]
    
    # 传入坐标元组 (x,y)
    x, y = coordinates
    
    # if not no_origin:
    #     # 点击之前检测一次窗口坐标
    #     get_origin()
    #     refresh_images_path()
    #     if variable_list['width'] ==1366:
    #         x = origin[0] + x
    #         y = origin[1] + y
    #     elif variable_list['width'] ==1280:#版本2
    #         x = origin[0] + (x*1280/1365) #1280/1364<k<1280/1364
    #         y = origin[1] + (y*(720)/770)+1 #750/770<k<720/769
    #     elif variable_list['width'] ==1600:
    #         # x = origin[0] + ((x-18)*1347/1149)+21 #
    #         x = origin[0] + (x*1600/1370)+3  #1600/1369
    #         y = origin[1] + (y)*899/767
    
    # elif no_origin==True:
    #     pass
    # else:#以x，y为原点
    #     if variable_list['width'] ==1366:
    #         x = no_origin[0] + x
    #         y = no_origin[1] + y
    #     elif variable_list['width'] ==1280:#版本2
    #         x = x + (no_origin[0]*1280/1365) #1280/1364<k<1280/1364
    #         y = y + (no_origin[1]*(720)/770)+1 #750/770<k<720/769
    #     elif variable_list['width'] ==1600:
    #         # x = origin[0] + ((x-18)*1347/1149)+21 #
    #         x = x + (no_origin[0]*1600/1370)+3  #1600/1369
    #         y = y + (no_origin[1])*899/767
    get_origin()
    x,y=tranposition(x,y,no_origin=no_origin)#改版
    for i in range(times):
        
        t = 2 if dbl else 1
        windll.LoadLibrary("C:\\Windows\\System32\\user32.dll").BlockInput(1)#屏蔽鼠标键盘操作
        pyautogui.click(x=x, y=y, clicks=t, button='left')
        time.sleep(0.01)
        windll.LoadLibrary("C:\\Windows\\System32\\user32.dll").BlockInput(0)#开启鼠标键盘操作#会导致继续要开2次，按键才生效
        #这个用的是向小取整，所以变化的坐标偶尔会往左上偏
        
        time.sleep(cd)
    if no_return==False:
        pyautogui.moveTo(variable_list['mouse_positon'])#返回原来的位置，还是有几率错位
    else:
        variable_list['getmouse']=False

def staymouse(coordinates, ctime=1):#悬停鼠标
    global signal_blocking
    print('鼠标在%s悬停%s秒'%(coordinates,ctime))
    block()
    (x0, y0) = pyautogui.position()#存储原来的位置
    if isinstance(coordinates[1], str):
        coordinates = coordinates[0]
    
    # 传入坐标元组 (x,y)
    x, y = coordinates
    
    # 点击之前检测一次窗口坐标
    get_origin()
    refresh_images_path()
    if variable_list['width'] ==1366:
        x = origin[0] + x
        y = origin[1] + y
    elif variable_list['width'] ==1280:#版本2
        x = origin[0] + (x*1280/1365) #1280/1364<k<1280/1364
        y = origin[1] + (y*(720)/770)+1 #750/770<k<720/769
    elif variable_list['width'] ==1600:
        # x = origin[0] + ((x-18)*1347/1149)+21 #
        x = origin[0] + (x*1600/1370)+3  #1600/1369
        y = origin[1] + (y)*899/767
    pyautogui.moveTo(x, y)
    time.sleep(ctime)
    pyautogui.moveTo(x0, y0)#返回原来的位置，还是有几率错位

def get_position():#为下一次点击时的坐标，可直接作为函数变量
    def on_click(x, y, button, pressed):#被实施的函数
        get_origin()
        # 监听鼠标点击

        if pressed:
            if variable_list['width']==1366:
                x=x-origin[0]
                y=y-origin[1]
            elif variable_list['width']==1280:
                x=(x-origin[0])*1365/1280
                y=(y-origin[1]-1)*770/720
            elif variable_list['width']==1600:
                x=(x-origin[0]-3)*1370/1600
                y=(y-origin[1])*767/899
            variable_list['getedposition']=eval("[%s]"%("{},{}".format(math.ceil(x), math.ceil(y))))

        if not pressed:
            return False

    with pm.Listener(on_click=on_click) as pmlistener:#监测点击
        pmlistener.join()

    return variable_list['getedposition']



def selecthero(hero='任意英雄'):#新版带判断是否选英雄
    if variable_list["selectedhero"]!=hero:
        click(global_point_map['map_hero'])
        print("[%s]选择英雄：%s"% (get_datetime(),hero))
        click(global_point_map[hero])
        click(global_point_map['map_select'])
        click(global_point_map['cancel'])
        click(global_point_map['map_heroback'])
    variable_list["selectedhero"]=hero

def selectmode(mode='简单'):
    click(global_point_map[mode_click[mode][0]])
    click(global_point_map[mode_click[mode][1]])






def key(key, times=1, cd=0.1):
    # global signal_blocking
    block()
    
    # 模拟按键动作
    for i in range(times):
        keyboard.press(key)  # 按键按下
        # time.sleep(0.2)
        keyboard.release(key)  # 按键抬起
        time.sleep(cd)


def combokey(hotkey,key, times=1, cd=0.1):
    # global signal_blocking
    # block()
    
    # 模拟按键动作
    keyboard.press(hotkey)
    for i in range(times):
            keyboard.press(key)  # 按键按下
            keyboard.release(key)  # 按键抬起
            time.sleep(cd)
    keyboard.release(hotkey)

def entermap(map='猴子草甸',mode='简单'):#这个函数目前只是进入地图并运行打法
    if variable_list["selectedhero"]!=all_chains[map][mode][0]:#判刑这次用到的英雄是否与上次相同
        selecthero(all_chains[map][mode][0])
    click(global_point_map[map_info[map][1]])#点击地图位置
    selectmode(mode)
    variable_list['chain'] = all_chains[map][mode][1]
    variable_list["selectedhero"]=all_chains[map][mode][0]
    variable_list['mode']=mode


def cricle_onemap(map,mode):
    variable_list['script_mode']='cricleone'
    if variable_list['restart']!='1':#第一次跑执行以下操作
        click(global_point_map['advanced'], times=1)
        click(global_point_map['expert'], times=2)#重置地图
        click(global_point_map[page_click[map_info[map][0]][0]],page_click[map_info[map][0]][1])#点击地图对应的页数

        entermap(map,mode)




def exec_chains(chain, qi=None):
    print('[%s]游戏开始' % get_datetime())
    exec(chain)
    print('[%s] 动作链执行完毕' % get_datetime())
    return


def monitor(queue_infos=None):#游戏进程监视
    # queue_infos是肯定有的,
    if not queue_infos:
        queue_infos = {
        
        }
    
    while True:
        block()
        time.sleep(3)#给监测开个休息




        try:
            location = pyautogui.locateOnScreen(image=image_path['insta'], confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]识别到Insta图标,游戏结束.' % get_datetime())

            
            # 终结线程
            end_thread(exec_chains)
            # thread = queue_infos.get('thread_exec', '')
            # if thread != '':
            #     thread.raise_exception()
            
            time.sleep(1)
            click((x, y), no_origin=True)
            
            time.sleep(2)
            # 点击下一页
            click(global_point_map['next_page'])
            time.sleep(2)
            time.sleep(1)#防止有些人电脑卡没点到

            if variable_list['script_mode']=='cricleone':
                click(global_point_map['free_game'])
                time.sleep(1)
                click(global_point_map['free_game'])
                time.sleep(1)#防止有些人电脑卡没点到
                click(global_point_map['setting'])
                click(global_point_map['setting_restart'])
                click(global_point_map['restart_confirm'])
            else:
            # 点击回到主页
                click(global_point_map['over_home'])
                time.sleep(1)
            queue_infos['status'] = 'success'
            break
        
        except Exception as e:
            pass
        
        # 防止一直卡在结束页面
        # if (time.time() - start_time) > 1200:
        try:
            location = pyautogui.locateOnScreen(image=image_path['next_page'], confidence=0.85, grayscale=True)
            # location = pyautogui.locateOnScreen(image=image_path['continue, confidence=0.85, grayscale=True)#不确定可不可行
            x, y = pyautogui.center(location)
            
            print('[%s]识别到结算页面,点击下一页' % get_datetime())

            # 待设置


            # 好像有动作链没执行完的bug,要终结线程
            end_thread(exec_chains)
            # thread = queue_infos.get('thread_exec', '')
            # if thread != '':
            #     thread.raise_exception()
            click((x, y), no_origin=True)
            # 和上面不一样啊, 这里点了下一页, 没有点over_home啊
            # 加上的
            time.sleep(1)
            if variable_list['script_mode']=='cricleone':
                click(global_point_map['free_game'],times=2)
                time.sleep(1)
                click(global_point_map['setting'])
                click(global_point_map['setting_restart'])
                click(global_point_map['restart_confirm'])
            else:
            # 点击回到主页
                click(global_point_map['over_home'])
                time.sleep(1)
            queue_infos['status'] = 'success'#用于结束monitor，chain和继续猴子操作
            
            break
            
        except Exception as e:
            pass
    
        try:
            location_fail = pyautogui.locateOnScreen(image=image_path['fail'], confidence=0.85, grayscale=True)
            location_continue = pyautogui.locateOnScreen(image=image_path['continue'], confidence=0.85, grayscale=True)
            if location_fail or location_continue:
                print('[%s]检测到失败，失败截图在fail中查看' % get_datetime())
                
                # 终结执行chains的线程
                # 这里应该先终结线程
                end_thread(exec_chains)
                # try:
                #     thread = queue_infos.get('thread_exec', '')
                #     if thread != '':
                #         thread.raise_exception()

                # except Exception as e:
                #     print('[%s]检测到失败，终结线程失败,%s' % (get_datetime(), e))
                #     pass

                time.sleep(2)
                #失败时查看截图
                # # 1. 点击地图
                # click(global_point_map['fail_check_map'])
                # click(global_point_map['fail_checkmap_chimps'])
                # 2. 截图
                im = pyautogui.screenshot()
                img_path = 'fail'
                # 路径不存在时创建
                if not os.path.exists(img_path):
                    os.makedirs(img_path)
                # :不能用作文件名
                t = get_datetime()
                t = t.replace(':', '_')
                t = t.replace('-', '_')
                im.save('%s/%s 失败截图.png' % (img_path, t))
                # # 3. 点击右下角
                # click(global_point_map['fail_check_map_right'])
                # time.sleep(1.5)
                
                # print(variable_list['script_mode'])
                if variable_list['script_mode']=='cricleone':
                    if variable_list['mode']=='点击'or variable_list['mode']=='放气':
                        click(global_point_map['fail_restart_chimps'])
                        
                    elif variable_list['mode']=='':
                        time.sleep(1)
                        try:
                            location = pyautogui.locateOnScreen(image=image_path['restart'], confidence=0.8, grayscale=True)
                            x, y = pyautogui.center(location)
                            click((x, y), no_origin=True)#加这个参数才能点到正确位置
                        except Exception as e:
                            print('[%s]未识别到重新开始' % (get_datetime()))
                            pass
                    else:
                        click(global_point_map['fail_restart'])
                    click(global_point_map['restart_confirm'])
                    print('[%s]重新开始' % get_datetime())
                else:
                    
                    click(global_point_map['fail_home'])
                    click(global_point_map['fail_home_chimps'])
                    print('[%s]回到主页' % get_datetime())
                queue_infos['status'] = 'fail'  # 设置信号, break结束,线程就结束了
                if not isinstance(queue_infos['fail_times'], int):
                    queue_infos['fail_times'] = 1
                    
                else:
                    queue_infos['fail_times'] += 1
                break
    
        except Exception as e:
            pass


        try:
            location= pyautogui.locateOnScreen(image=image_path['local_record'], confidence=0.9, grayscale=True)
            
            x, y = pyautogui.center(location)
            # time.sleep(1)#放置游戏卡住
            click((x, y), no_origin=[0,306])
            print('[%s]识别到本地存档,点击本地存档' % get_datetime())
            # timesleep(1)#防止游戏卡住
            # continue
        
        except Exception as e:
            pass
        # 防止游戏卡在其他界面
        try:#这个后面的try好像会失效
            location_upgrade = pyautogui.locateOnScreen(image=image_path['upgrade'], confidence=0.8, grayscale=True)#0,7防止鼠标挡住
            location_knowledge = pyautogui.locateOnScreen(image=image_path['monkey_book'], confidence=0.8, grayscale=True)
            if location_upgrade or location_knowledge:
                print('[%s]识别到升级图标,执行点击升级' % get_datetime())
                click(global_point_map['upgrade'],times=1, cd=0.4)
            # continue
        
        except Exception as e:
            pass



        try:
            location = pyautogui.locateOnScreen(image=image_path['blue'], confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]游戏出现意外，将重置游戏.' % get_datetime())

            # 终结线程
            end_thread(exec_chains)
            # thread = queue_infos.get('thread_exec', '')
            # if thread != '':
            #     thread.raise_exception()
            # 2. 截图
            im = pyautogui.screenshot()
            img_path = 'fail'
            # 路径不存在时创建
            if not os.path.exists(img_path):
                os.makedirs(img_path)
            # :不能用作文件名
            t = get_datetime()
            t = t.replace(':', '_')
            t = t.replace('-', '_')
            im.save('%s/%s 意外截图.png' % (img_path, t))
            queue_infos['status'] = 'fail'
            break
        
        except Exception as e:
            pass
        # print('test')






def set_level_point(position, coordinates, deviation=None):#校准升级判断
    global queue_infos
    
    # 有原点坐标直接迭代了
    if position not in ['left', 'right']:
        # 怎么也不应该报这个错
        print('[%s]设置技能点坐标时异常' % get_datetime())
        os.exit()
        
    # coordinates 是图左上角的坐标
    x, y = coordinates
    if deviation:
        x = x + deviation[0]
        y = y + deviation[1]
        
    else:
        x += 8
        y += 8
    # 现在x,y是第一个坐标
    
    tmp_dic = {#技能点像素坐标
    
    }
    
    for i in ['top', 'middle', 'bottom']:
        
        if not tmp_dic.get(i):
            tmp_dic[i] = list()
            
        for k in range(0, 5):
            # x是不变的, 都是y变
            if k < 3:
                tmp_dic[i].append([x, y + (k*17)])  # 第一个是0x17, 还是他自己
            else:
                tmp_dic[i].append([x, y + (k*17) + 2])  # 第三个就每个多加2像素吧, 不能改17, 乘法就是多6个了
            
        # 5个循环完毕, 要加一个间隔, 测出来是37px
        y += 106
        
        
    # 到此, tmp_dic应该就是正常的了
    queue_infos['level_point_position_%s' % position] = tmp_dic
    # print('[%s] 初始化计算 %s 技能点像素坐标\n%s' % (get_datetime(),
    #                                      ('左侧' if position == 'left' else '右侧'),
    #                                      tmp_dic))
    return tmp_dic

def get_page():
    for n in page_position:#识别页数
        img = pyautogui.screenshot(region=[*origin, 1600, 900])
        position_list = copy.deepcopy(page_position[n])
        
        threshold = 10  # 阈值
        aru = (64, 159, 255)  # 浅蓝
        # point2=position_list[0]*width/1366,position_list[1]*width/1366
        point2=position_list[0]*variable_list['width']/1366,position_list[1]*variable_list['width']/1366
        pixel = img.getpixel(tuple(point2))

        
        if abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold:

            return n


# def after_round(i,cd=0.5):
#     Game = pymem.Pymem("BloonsTD6") # 游戏进程
#     def Get_moduladdr(dll): # 读DLL模块基址
        
#         modules = list(Game.list_modules()) # 列出exe的全部DLL模块
#         for module in modules:
#             if module.name == dll:
#                 #print(module.name) # 模块名字
#                 #print(module.lpBaseOfDll) # 模块基址
#                 #print("找到了")
#                 Moduladdr = module.lpBaseOfDll
#         return Moduladdr
#     DLL_addr = Get_moduladdr("GameAssembly.dll") # 读DLL模块基址
#     print('[%s]等到第%s回合执行操作' % (get_datetime(),i))
#     round_BASE_addr = Game.read_longlong(DLL_addr + 0x02F794c0)
#     while True:
#         time.sleep(cd)
#         try:
#             addr1 = Game.read_longlong(round_BASE_addr+ 0xB8)
#             addr2 = Game.read_longlong(addr1 + 0x0)
#             addr3 = Game.read_longlong(addr2 + 0x110)
#             addr4 = Game.read_longlong(addr3 + 0x78)
#             addr5 = Game.read_longlong(addr4 + 0x28)
#             addr6 = Game.read_longlong(addr5 + 0x40)
#             round = Game.read_int(addr6 + 0x20)
#             # print(round)
#             if round==i:
#                 return True
#         except Exception as e:
#             print('[%s]未识别到回合数' % get_datetime())

def match_pixel(position,aru,threshold=10):#匹配判断像素点
    point2 = position[0]*variable_list['width'] / 1366, position[1]*variable_list['width']/1366
    img = pyautogui.screenshot(region=[*origin, 1600, 900])
    pixel = img.getpixel(tuple(point2))
    # print(pixel)
    if abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold:
        return True


def mupgrade(monkey,combo=False,show_log=False):
    shortcut,mposition=monkey
    if variable_list['position_test']==True:
        return
    print('[%s]升级%s为%s' % (get_datetime(),var_name(shortcut),combo))
    #以后做个自动升级的脚本
    if isinstance(mposition[1], str):
        mposition = mposition[0]
    

    # 如果技能组合一个0都没有就是非法的
    
    # 1. 识别当前技能等级
    # 2. 检测到目标等级需要的按键 最近的一个 比如F1
    # 3. 监听右边是否绿色图标, 有就执行
    # 4. 执行完检测目前等级与组合的差距, 直到和技能组合相等就退出阻塞, 执行下一条chain
    

    # 直接遍历combo
    
    if len(combo) != 3:
        combo = '000'
    
    if '0' not in combo:
        combo[-1] = '0'
    
    # 先笼统的get一次大致不就好了
    info = get_level_info(mposition)
    # current = info['level']


    for n, i in enumerate(combo):
        if show_log:
            print('[%s]当前combo: %s, 当前i:%s' % (get_datetime(), combo, i))
        
        if int(i) > 0:
            # 表示要升级,先判定下
            
            # 如果这里点开了, 后面也就不要先点击了吧
            
            
            if combo[n] == '0':
                continue
            
            if show_log:
                print('[%s]当前技能情况:%s, combo: %s' % (get_datetime(), info['level'], combo))
                print('[%s]int(current[n]) == %s,  int(combo[n]) == %s' % (get_datetime(), info['level'][n], combo[n]))
            
            if int(info['level'][n]) < int(combo[n]):
                for i in range(20):
                    try:
                        
                        # location = pyautogui.locateOnScreen(image=image_path['sale, confidence=0.7, grayscale=True)
                        # x, y = pyautogui.center(location)
                        # print('[%s]升级猴子, 识别到出售图标' % get_datetime())
                        
                        # 阻塞一直等待升级
                        # is_upgraded = False
                        for k in range(1,1001):
                            # 这一段应该要升级到指定级数才break了
                            
                            # 如果能升级了就点击
                            # time.sleep(1)
                            
                            info = get_level_info(mposition, 4)
                            
                            if show_log:
                                print('[%s]当前猴子信息:%s' % (get_datetime(), info))
                            
                            if info['skill%s' % (n + 1)] and int(info['level'][n]) < int(combo[n]):
                                # 执行升级操作
                                
                                distance = int(combo[n]) - int(info['level'][n])
                                
                                if distance >= 2:
                                    click(global_point_map['game_right'], times=1, cd=0.1)
                                    exec('key(skill%s, times=%s)' % ((n + 1), distance))
                                
                                else:
                                    click(global_point_map['game_right'], times=1, cd=0.1)
                                    exec('key(skill%s)' % (n + 1))
                                
                                # is_upgraded = True

                                info = get_level_info(mposition, 4)
                                
                                if int(info['level'][n]) >= int(combo[n]):
                                    break
                            
                            elif int(info['level'][n]) >= int(combo[n]):
                                break
                            
                            # # 根据循环次数前期等待少一点, 封顶10秒 这是脚本休息的代码
                            # stime = math.ceil(0.5 * k)
                            # if stime > 4:
                            #     stime = 4
                            # if queue_infos['rest']==1:
                            #  time.sleep(stime)#休息代码
                        
                        # if is_upgraded:
                        #     # 升级动作已经完成,退出这个技能点的升级
                        #     break # 这个break直接就升级下个技能了
                        info = get_level_info(mposition, 4)
                        
                        if int(info['level'][n]) >= int(combo[n]):
                            break
                    
                    except Exception as e:
                        click(global_point_map['game_rightdown'])
                        click(shortcut)
                    
                    # time.sleep(1)#休息一秒
                
                else:
                    print('[%s]识别出售图标失败, 退出此次升级' % (get_datetime()))
                    return
            
            else:
                '''表示当前等级已经和combo对应位置相等了'''
    click(global_point_map['game_rightdown'])
    # print("升级完成")



def fz(monkey, validation=True,slow=False):#目前有点小bug ,上面的猴子从,如果猴子放的时候钱不够且点到其他猴子,会导致判断为放置成功[617,45]附近区域会触发bug,解决方法,time.sleep使得有钱的时候再放
    shortcut,mposition=monkey
    if slow:
        time.sleep(1)
        print('[%s]减缓游戏' % (get_datetime()))
        key(Key.space)
    print('[%s]在%s放置%s' % (get_datetime(),mposition,var_name(shortcut)))
    is_deployed = False
    signal_blocking_thread.clear()
    signal_blocking_thread.append(time.time()-999999+5)
    for i in range(100):
        # 1. 点击空白处
        # click(global_point_map['game_rightdown'], times=2, cd=0.1)
        click(global_point_map['game_rightdown'], times=1, cd=0.1)
        # 2. 放置对应猴子
        key(shortcut)
        # 3. 点击放置处 停止一下其他线程，防止干扰

        click(mposition, cd=0.1)  # 第一次是放置
        # click(global_point_map['game_right'], times=2, cd=0.1)#0防止原来的位置已经被占用
        click(global_point_map['game_right'], times=1, cd=0.1)#0防止原来的位置已经被占用
        click(mposition)  # 第二次是点开猴塔
        if validation:
            # 4. 检测到出售,放置成功,退出阻塞 执行下一条chain
            try:
                # time.sleep(0.5)
                location = pyautogui.locateOnScreen(image=image_path['sale'], confidence=0.85, grayscale=True)
                x, y = pyautogui.center(location)
                # print('[%s]识别到出售图标, 猴子塔放置成功' % get_datetime())
                is_deployed = True
                break
            
            except Exception as e:
                # print('[%s]未识别到出售图标, 猴子塔放置失败' % get_datetime())
                pass
        
        else:
            # 点击空白处
            # click(global_point_map['game_right'], times=2, cd=0.1)
            return True
        
        cd = (i + 1) * 2
        if cd > 10:
            cd = 10
        if queue_infos['rest']==1:
         time.sleep(cd)#代码休息
    
    # 点击空白处
    # click(global_point_map['game_rightdown'], times=2, cd=0.1)
    click(global_point_map['game_rightdown'], times=1, cd=0.1)
    if slow:
        print('[%s]加速游戏' % (get_datetime()))
        key(Key.space)
    return is_deployed
  
def testposition(shortcut,mposition, validation=True,show_log=False):#目前有点小bug ,上面的猴子从,如果猴子放的时候钱不够且点到其他猴子,会导致判断为放置成功[617,45]附近区域会触发bug,解决方法,time.sleep使得有钱的时候再放
    print('[%s]在%s放置%s' % (get_datetime(),mposition,var_name(shortcut)))
    is_deployed = False
    for i in range(100):
        # 1. 点击空白处
        click(global_point_map['game_rightdown'], times=1, cd=0.1)
        # 2. 放置对应猴子
        key(shortcut)
        # 3. 点击放置处
        click(mposition, cd=0.1)  # 第一次是放置
        click(global_point_map['game_right'], times=1, cd=0.1)#0防止原来的位置已经被占用
        click(mposition)  # 第二次是点开猴塔
        if validation:
            # 4. 检测到出售,放置成功,退出阻塞 执行下一条chain
            try:
                # time.sleep(0.5)
                location = pyautogui.locateOnScreen(image=image_path['sale'], confidence=0.85, grayscale=True)
                x, y = pyautogui.center(location)
                # print('[%s]识别到出售图标, 猴子塔放置成功' % get_datetime())
                is_deployed = True
                break
            
            except Exception as e:
                # print('[%s]未识别到出售图标, 猴子塔放置失败' % get_datetime())
                pass
        
        else:
            # 点击空白处
            # click(global_point_map['game_right'], times=2, cd=0.1)
            return True
        
        cd = (i + 1) * 2
        if cd > 10:
            cd = 10
        if queue_infos['rest']==1:
         time.sleep(cd)#代码休息
    
    # 点击空白处
    # click(global_point_map['game_rightdown'], times=2, cd=0.1)
    click(global_point_map['game_rightdown'], times=1, cd=0.1)
    
    return is_deployed
  

def 献祭猴子(shortcut,mposition, validation=True,show_log=False):#目前有点小bug ,上面的猴子从,如果猴子放的时候钱不够且点到其他猴子,会导致判断为放置成功[617,45]附近区域会触发bug,解决方法,time.sleep使得有钱的时候再放
    print('[%s]在%s放置%s' % (get_datetime(),mposition,var_name(shortcut)))
    is_deployed = False
    click(global_point_map['game_rightdown'], times=1, cd=0.1)
    # 2. 放置对应猴子
    keyboard.press(shortcut)
    for i in range(24):
        # 1. 点击空白处

        # 3. 点击放置处
        click(mposition, cd=0.1)  # 第一次是放置
        mposition[0]+=47
    keyboard.press(shortcut)

    
    return is_deployed



def get_level_info(mposition, check_times=0):
    # 升级判断函数
    # 1. 空白点击, 点击对应猴子, 直到检测到出售, 截图到IO流
    # 2. 遍历level_info
    # 3. 返回技能组合 402
    global queue_infos
    
    if len(mposition) != 2:
        return False, '000'
    
    if not isinstance(mposition[0], int) or not isinstance(mposition[0], int):
        return False, '000'
    
    
    # 先点击下空白处
    if check_times < 2:
        click(global_point_map['game_rightdown'], times=1, cd=0.1)
        click(mposition)
          # 这是点击的相对坐标,要原点
    
    sale_position = 'left'
    
    # location = None
    for i in range(40):#识别是否点到
        
        try:
            # time.sleep(1)
            location = pyautogui.locateOnScreen(image=image_path['sale'], confidence=0.5, grayscale=True)
            
            
            if not location:
                click(global_point_map['game_rightdown'], times=1, cd=0.1)
                click(mposition)  # 要加上原点
                
                # 会不会是停顿太小, 导致点击之后马上识别, 动画效果还没加载完成
                time.sleep(0.5)
                
                continue
            
            x0, y0 = pyautogui.center(location)
            if variable_list['debug']:
                print('[%s]出售的屏幕坐标为[%s,%s]' % (get_datetime(),x0,y0))
            if x0<0:
                print('[%s]出售的屏幕坐标为[%s,%s],为负数,识图模块出错.未正确识别到位置,会导致升级出错请更换应用缩放或者显示器分辨率' % (get_datetime(),x0,y0))
            if x0>0 and y0<0:
                print('[%s]出售的屏幕坐标为[%s,%s],为负数,识图模块出错.未正确识别到位置,会导致升级出错请更换应用缩放或者显示器分辨率' % (get_datetime(),x0,y0))
            # print('[%s]获取猴子信息, 识别到出售图标' % get_datetime()
            if (x0 - origin[0]) > 600:
                # 表示出售在右边
                sale_position = 'right'
            
            break
        
        except Exception as e:
            
            # if check_times > 1:
            #     print('[%s] hahaha======> 错误行: %s, \n报错内容: %s' % (get_datetime(), traceback.print_exc(), e))
            
            click(global_point_map['game_rightdown'], times=1, cd=0.1)
            click(mposition)  
            time.sleep(1)
    
    else:
        print('[%s]点击了20次, 未能识别到出售图标,将重置游戏' % get_datetime())
        im = pyautogui.screenshot()
        img_path = 'fail'
        # 路径不存在时创建
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        # :不能用作文件名
        t = get_datetime()
        t = t.replace(':', '_')
        t = t.replace('-', '_')
        im.save('%s/%s 升级失败.png' % (img_path, t))
        key(Key.esc)
        time.sleep(1)
        click(global_point_map['setting_restart'])
        click(global_point_map['restart_confirm'])
        key(Key.space,times=2)
        
        # dic = {
        #     'level': '000',
        #     'skill1': False,
        #     'skill2': False,
        #     'skill3': False
        # }
        # return dic
    
    # 2. 保存截图
    img = pyautogui.screenshot(region=[*origin, 1366, 768])  # 分别代表：左上角坐标，宽高
    # 这里的截图是游戏的截图
    # pix = img.getpixel((x, y)) pix是一个数组
    
    level = [0, 0, 0]
    tmp_dict = {
        'top': 0,
        'middle': 1,
        'bottom': 2
    }
    
    # pixel_dict = dict() # 技能获取 调试模式

    need_save = False
    if not queue_infos.get('level_point_position_%s' % sale_position):#校准升级或进行升级
        need_save = True
        
        
        queue_infos['level_point_position_%s' % sale_position] = \
         copy.deepcopy(queue_infos['level_point_position_%s_default' % sale_position])
    
    if sale_position == 'left':
        # 获取坐标
        level_point_position = queue_infos['level_point_position_left']
        
    else:
        # 获取坐标
        level_point_position = queue_infos['level_point_position_right']
    
    for k in level_point_position:
        # k = 'top'
        
        # 倒序一下, 我要从下往上累加
        position_list = copy.deepcopy(level_point_position[k])
        position_list = position_list[::-1]
        # print('%s,%s' % (k, position_list)) # 技能获取 调试模式
        
        # 技能计数值
        tmp_count = '0'
        # print('================%s' % position_list)
        for n, point in enumerate(position_list, start=1):
            # 本可以if  ,代码要迁移修改下, 太麻烦
            
            # 像素值总有点偏差, 设置个阈值吧
            threshold = 15
            
            aru = (255, 255, 0)
            # nai = (151, 109, 59)
            # ban = (128, 74, 36)
            
            # k是top, middle, bottom
            # print('-------------i: %s' % point)
            # pixel = img.getpixel(tuple(point))
            point2=point[0]*variable_list['width']/1366,point[1]*variable_list['width']/1366
            pixel = img.getpixel(tuple(point2))
            # point = [40, 342]
                
            if need_save:
                    # print('调试模式')
                    for px in range(1, 31):
                        
                        _x, _y = (point[0] - px, point[1])
                        img.putpixel((_x, _y), (255, 0, 0))

                        _x, _y = (point[0] + px, point[1])
                        img.putpixel((_x, _y), (255, 0, 0))
            
            # 那个区间的的像素rgb在 (30-255, 200-255, 0-3)
            if (30 <= int(pixel[0]) <= 256) and \
                    (200 <= int(pixel[1]) <= 256) and \
                    (0 <= int(pixel[2]) <= 10):
                # n 是目前 top 下的第几个元素, 识别到就是对应第几级,不用累加了
                tmp_count = str(n)
                # 不能break 还要循环另一边的
                
            # else:
            
            # 上面判断了左还是右边了, 可以直接break了
            # break
            
        level[tmp_dict[k]] = tmp_count
    
    # print(pixel_dict)  # 技能获取 调试模式
    
    dic = {
        'level': ''.join(level),
        'skill1': False,
        'skill2': False,
        'skill3': False
    }
    
    # 顺带检测上中下三路可升级情况
    for s in level_status_position:
        position_list = copy.deepcopy(level_status_position[s])
        
        threshold = 10  # 阈值
        aru = (82, 222, 0)  # 可升级图标的 绿色
        
        # 在这里对i做左右处理吧
        if sale_position == 'left':
            position_list = position_list[0:1]
        else:
            position_list = position_list[1:2]
            
        for n, point in enumerate(position_list):
            # print(point)#测试

            # print(point2)
            # pixel = img.getpixel(tuple(point))
            # point2=point[0]*screen/768,point[1]*screen/768
            point2=point[0]*variable_list['width']/1366,point[1]*variable_list['width']/1366
            pixel = img.getpixel(tuple(point2))

            if need_save:
                # print('调试模式')
                for px in range(1, 31):
                    _x, _y = (point[0] - px, point[1])
                    img.putpixel((_x, _y), (255, 0, 0))
        
                    _x, _y = (point[0] + px, point[1])
                    img.putpixel((_x, _y), (255, 0, 0))
            
            if abs(pixel[0] - aru[0]) < threshold and \
                    abs(pixel[0] - aru[0]) < threshold and \
                    abs(pixel[0] - aru[0]) < threshold:
                # 不能break 还要循环另一边的 ???
                
                # 如果到这边了的话, 那另一边也就没有了,直接break吧
                dic[s] = True
                
                break


    
    # 2022-10-29 03:14:27 如果是调试模式, 要绘图保存
    # if need_save:#调试的时候开启
    #     t = get_datetime().replace(':', '_').replace('-', '_')
    #     path = 'debug_imgs'
    #     if not os.path.exists(path):
    #         os.makedirs(path)
        
    #     img.save('%s/%s_%s.png' % (path, t, sale_position))
    

    del img
    
    return dic

## start 游戏操作函数
# 以猴子名字来命名放置和升级函数
# 老版本需要删除

def run(shortcut,mposition,combo=False, validation=True,show_log=False):
    # 1. 点击空白处
    # 2. 放置对应猴子
    # 3. 点击放置处
    # 4. 检测到出售,放置成功,退出阻塞 执行下一条chain
 if combo:
    print('[%s]升级%s为%s' % (get_datetime(),var_name(shortcut),combo))
    if isinstance(mposition[1], str):
        mposition = mposition[0]
    
    
    # 如果技能组合一个0都没有就是非法的
    
    # 1. 识别当前技能等级
    # 2. 检测到目标等级需要的按键 最近的一个 比如F1
    # 3. 监听右边是否绿色图标, 有就执行
    # 4. 执行完检测目前等级与组合的差距, 直到和技能组合相等就退出阻塞, 执行下一条chain
    

    # 直接遍历combo
    
    if len(combo) != 3:
        combo = '000'
    
    if '0' not in combo:
        combo[-1] = '0'
    
    # 先笼统的get一次大致不就好了
    info = get_level_info(mposition)
    # current = info['level']
    
    for n, i in enumerate(combo):
        if show_log:
            print('[%s]当前combo: %s, 当前i:%s' % (get_datetime(), combo, i))
        
        if int(i) > 0:
            # 表示要升级,先判定下
            
            # 如果这里点开了, 后面也就不要先点击了吧
            
            # if n > 0:
            #     time.sleep(1)
            
            if combo[n] == '0':
                continue
            
            if show_log:
                print('[%s]当前技能情况:%s, combo: %s' % (get_datetime(), info['level'], combo))
                print('[%s]int(current[n]) == %s,  int(combo[n]) == %s' % (get_datetime(), info['level'][n], combo[n]))
            
            if int(info['level'][n]) < int(combo[n]):
                for i in range(20):
                    try:
                        
                        location = pyautogui.locateOnScreen(image=image_path['sale'], confidence=0.7, grayscale=True)
                        x, y = pyautogui.center(location)
                        # print('[%s]升级猴子, 识别到出售图标' % get_datetime())
                        
                        # 阻塞一直等待升级
                        # is_upgraded = False
                        for k in range(1,1001):
                            # 这一段应该要升级到指定级数才break了
                            
                            # 如果能升级了就点击
                            time.sleep(1)
                            
                            info = get_level_info(mposition, 4)
                            
                            if show_log:
                                print('[%s]当前猴子信息:%s' % (get_datetime(), info))
                            
                            if info['skill%s' % (n + 1)] and int(info['level'][n]) < int(combo[n]):
                                # 执行升级操作
                                
                                distance = int(combo[n]) - int(info['level'][n])
                                
                                if distance >= 2:
                                    click(global_point_map['game_right'], times=1, cd=0.1)
                                    exec('key(skill%s, times=%s)' % ((n + 1), distance))
                                
                                else:
                                    click(global_point_map['game_right'], times=1, cd=0.1)
                                    exec('key(skill%s)' % (n + 1))
                                
                                # is_upgraded = True

                                info = get_level_info(mposition, 4)
                                
                                if int(info['level'][n]) >= int(combo[n]):
                                    break
                            
                            elif int(info['level'][n]) >= int(combo[n]):
                                break
                            
                            # 根据循环次数前期等待少一点, 封顶10秒
                            # stime = math.ceil(0.5 * k)
                            # if stime > 4:
                            #     stime = 4

                            # time.sleep(stime)
                        
                        # if is_upgraded:
                        #     # 升级动作已经完成,退出这个技能点的升级
                        #     break # 这个break直接就升级下个技能了
                        info = get_level_info(mposition, 4)
                        
                        if int(info['level'][n]) >= int(combo[n]):
                            break
                    
                    except Exception as e:
                        click(global_point_map['game_rightdown'])
                        click(shortcut)
                    
                    time.sleep(1)
                
                else:
                    print('[%s]识别出售图标失败, 退出此次升级' % (get_datetime()))
                    return
            
            else:
                '''表示当前等级已经和combo对应位置相等了'''
    click(global_point_map['game_rightdown'])
    # print("升级完成")
 else:
    print('[%s]在%s放置%s' % (get_datetime(),mposition,var_name(shortcut)))
    is_deployed = False
    for i in range(100):
        # 1. 点击空白处
        click(global_point_map['game_rightdown'], times=2, cd=0.1)
        # 2. 放置对应猴子
        key(shortcut)
        # 3. 点击放置处
        click(mposition, cd=0.1)  # 第一次是放置
        click(global_point_map['game_right'], times=2, cd=0.1)#0防止原来的位置已经被占用
        click(mposition)  # 第二次是点开猴塔
        if validation:
            # 4. 检测到出售,放置成功,退出阻塞 执行下一条chain
            try:
                # time.sleep(0.5)
                location = pyautogui.locateOnScreen(image=image_path['sale'], confidence=0.85, grayscale=True)
                x, y = pyautogui.center(location)
                # print('[%s]识别到出售图标, 猴子塔放置成功' % get_datetime())
                is_deployed = True
                break
            
            except Exception as e:
                # print('[%s]未识别到出售图标, 猴子塔放置失败' % get_datetime())
                pass
        
        else:
            # 点击空白处
            # click(global_point_map['game_right'], times=2, cd=0.1)
            return True
    
    # 点击空白处
    click(global_point_map['game_rightdown'], times=2, cd=0.1)
    
    return is_deployed




def dart(mposition,combo=False):
    run(飞镖猴,mposition,combo)
def boomerang(mposition,combo=False):
    run(回旋镖猴,mposition,combo)
def bomb(mposition,combo=False):
    run(大炮,mposition,combo)
def tack(mposition,combo=False):
    run(图钉塔,mposition,combo)
def ice(mposition,combo=False):
    run(冰猴,mposition,combo)
def glue(mposition,combo=False):
    run(胶水炮手,mposition,combo)
def sniper(mposition,combo=False):
    run(狙击手猴,mposition,combo)
def sub(mposition,combo=False):
    run(猴子潜艇,mposition,combo)
def buccaneer(mposition,combo=False):
    run(海盗猴,mposition,combo)
def ace(mposition,combo=False):
    run(皇家飞行员,mposition,combo)
def pilot(mposition,combo=False):
    run(直升机飞行员,mposition,combo)
def mortar(mposition,combo=False):
    run(迫击炮猴,mposition,combo)
def gunner(mposition,combo=False):
    run(机枪猴,mposition,combo)
def wizard(mposition,combo=False):
    run(法师猴,mposition,combo)
def super(mposition,combo=False):
    run(超猴侠,mposition,combo)
def ninja(mposition,combo=False):
    run(忍者猴,mposition,combo)
def alchemist(mposition,combo=False):
    run(炼金术士,mposition,combo)
def druid(mposition,combo=False):
    run(德鲁伊,mposition,combo)
def farm(mposition,combo=False):
    run(香蕉农场,mposition,combo)
def engineer(mposition,combo=False):
    run(工程师猴,mposition,combo)
def spike(mposition,combo=False):
    run(刺钉工厂,mposition,combo)
def village(mposition,combo=False):
    run(猴子村,mposition,combo)
def hero(mposition,combo=False):
    run(英雄,mposition,combo)



# 新版chain的函数abilities

def tab(monkey,n=1):## 切换攻击模式
    shortcut,mposition=monkey
    '''shortcut,mpostion为你定义的猴子,n为切换的次数'''
    print("[%s]切换%s的攻击对象%s次"%(get_datetime(),var_name(shortcut),n))
    click(global_point_map['game_right'],cd=0.001)
    click(mposition)
    time.sleep(0.5)
    key(Key.tab, times=n)
    click(global_point_map['game_rightdown'], cd=0.001)



def aim(monkey,aimposition):## 切换攻击模式
    shortcut,mposition=monkey
    print("[%s]使%s瞄准%s"%(get_datetime(),var_name(shortcut),aimposition))
    click(global_point_map['game_right'], cd=0.001)
    click(mposition)
    time.sleep(0.5)
    key(Key.tab)
    click(aimposition)
    click(global_point_map['game_rightdown'], cd=0.001)

def aimtool(monkey,aimposition,aimposition2=False):## 切换位置
    shortcut,mposition=monkey
    print("[%s]使%s的技能瞄准%s"%(get_datetime(),var_name(shortcut),aimposition))
    click(global_point_map['game_right'], cd=0.001)
    click(mposition)
    # time.sleep(0.5)#识别位置
    for i in range(11):

        try:
            time.sleep(0.5)
            tab = pyautogui.locateOnScreen(image=image_path['tab_button'], confidence=0.9, grayscale=True)
            x, y = pyautogui.center(tab)
            # windll.LoadLibrary("C:\\Windows\\System32\\user32.dll").BlockInput(1)#屏蔽鼠标键盘操作
            # variable_list['blockinput']=True
            click((x,y),no_origin=[95,0],no_return=True,slow=True)
            click(aimposition,cd=0.001,no_return=True)
            if aimposition2:
                click(aimposition2,cd=0.001)
            # windll.LoadLibrary("C:\\Windows\\System32\\user32.dll").BlockInput(0)#开启鼠标键盘操作#
            # variable_list['blockinput']=False
            break
        except Exception as e:
            if i > 9:
                print('未识别到tab按钮')
                break
            pass

    click(global_point_map['game_rightdown'], cd=0.001)

def uphero(n=1):## 优先攻击迷彩
    """用于升级英雄,n为升级英雄的次数"""
    print('[%s]升级英雄%s次'%(get_datetime(),n))
    click(global_point_map['game_right'], cd=0.001)
    key('u')
    key(skill1,n)
    key('u')

def aimcamo(monkey):## 优先攻击迷彩
    shortcut,mposition=monkey
    print("[%s]切换%s为优先攻击迷彩"%(get_datetime(),var_name(shortcut)))
    click(global_point_map['game_right'], cd=0.001)
    click(mposition)
    time.sleep(0.5)
    key(Key.page_down)
    click(global_point_map['game_rightdown'], cd=0.001)

# def dm_(x):
#     print('[%s]移除位于%s的障碍物' % (get_datetime(),x))
#     click(global_point_map['game_rightdown'], times=2)
#     click(x)
#     time.sleep(1)
#     while True:
#             if pyautogui.locateOnScreen(image=image_path['confirm'], confidence=0.7, grayscale=True):
#                 while True:
#                     try:
#                         confirm = pyautogui.locateOnScreen(image=image_path['confirm'], confidence=0.9, grayscale=False)
#                         x0, y0 = pyautogui.center(confirm)
#                         click((x0, y0), no_origin=True)
#                         break
#                     except Exception as e:
#                         pass
#             break
def dm(x):
    print('[%s]移除位于%s的障碍物' % (get_datetime(),x))
    click(global_point_map['game_rightdown'], times=2)
    click(x)
    time.sleep(1)
    while True:
            if pyautogui.locateOnScreen(image=image_path['confirm'], confidence=0.8, grayscale=True):
                while True:
                    try:
                        confirm = pyautogui.locateOnScreen(image=image_path['confirm'], confidence=0.9, grayscale=False)
                        x0, y0 = pyautogui.center(confirm)
                        click((x0, y0), no_origin=True)
                        return
                    except Exception as e:
                        pass
            else:
                print('[%s]未识别到障碍物拆除' % (get_datetime()))
                break


def abilities(x,n=1,cd=4,cd2=0.2):#循环使用技能线程失效
    print('[%s]循环使用%s技能' % (get_datetime(),x))
    while True:
        block()
        for m in range(int(n)):
            for i in x:
                key(i)
                time.sleep(cd2)
        time.sleep(cd)



def ability(x,position=global_point_map['game_right'],position2=False,cd=0.01):#cd=0.1防止失效
    time.sleep(cd)
    key(x)
    print('[%s]使用%s技能' % (get_datetime(),x))
    if position2:#为飞机迁移专门设置的

        click(position,no_return=True,cd=0.5)
        click(position2)
    else:
        click(position)
def cricle_ability(x,position=global_point_map['game_right'],cd=4):
    print('[%s]循环使用%s技能' % (get_datetime(),x))
    while True:
        blockthread()
        key(x)
        click(position)
        time.sleep(cd)

def cricle_moveto(position,cd=4,times=5):
    print('[%s]循环移动到%s' % (get_datetime(),position))
    for x in range(times):
        blockthread()
        recordmouse()
        pyautogui.moveTo(tranposition(*position))
        pyautogui.moveTo(*variable_list['mouse_positon'])
        backmouse()
        time.sleep(cd)

def msale(monkey):
    shortcut,mposition=monkey
    print('[%s]出售位于%s的%s' % (get_datetime(),mposition,var_name(shortcut)))
    click(global_point_map['game_rightdown'], times=2)
    click(mposition) 
    key(Key.backspace)

def startgame(n=2):
        if n>1:
         print('[%s]回合开始' % get_datetime())
        elif n==1:
         print('[%s]切换游戏速度' % get_datetime())
        for x in range(n):
         click(global_point_map['game_right'])

         key(Key.space)
    # time.sleep(1)
    # click(global_point_map['game_right'])
    # key(Key.space)

def power(key,position=global_point_map['game_center'],times=1):
    global signal_blocking
    # click(global_point_map['game_rightdown'])
    block()
    
    # 模拟按键动作
    keyboard.press(Key.shift)
    time.sleep(0.5)
    for i in range(times):
            keyboard.press(key)  # 按键按下
            time.sleep(0.001)
            click(position,cd=0.001)
            keyboard.release(key)
    keyboard.release(Key.shift)


## start 游戏操作函数
def up001(monkey):
    mupgrade(monkey,'001')
def up002(monkey):
    mupgrade(monkey,'002')
def up003(monkey):
    mupgrade(monkey,'003')
def up004(monkey):
    mupgrade(monkey,'004')
def up005(monkey):
    mupgrade(monkey,'005')
# 第一个0
def up010(monkey):
    mupgrade(monkey,'010')
def up011(monkey):
    mupgrade(monkey,'011')
def up012(monkey):
    mupgrade(monkey,'012')
def up013(monkey):
    mupgrade(monkey,'013')
def up014(monkey):
    mupgrade(monkey,'014')
def up015(monkey):
    mupgrade(monkey,'015')

def up020(monkey):
    mupgrade(monkey,'020')
def up021(monkey):
    mupgrade(monkey,'021')
def up022(monkey):
    mupgrade(monkey,'022')
def up023(monkey):
    mupgrade(monkey,'023')
def up024(monkey):
    mupgrade(monkey,'024')
def up025(monkey):
    mupgrade(monkey,'025')
def up030(monkey):

    mupgrade(monkey,'030')
def up031(monkey):
    mupgrade(monkey,'031')
def up032(monkey):
    mupgrade(monkey,'032')
def up040(monkey):
    mupgrade(monkey,'040')
def up041(monkey):
    mupgrade(monkey,'041')
def up042(monkey):
    mupgrade(monkey,'042')
def up050(monkey):
    mupgrade(monkey,'050')
def up051(monkey):
    mupgrade(monkey,'051')
def up052(monkey):
    mupgrade(monkey,'052')

# 第2个0
def up101(monkey):
    mupgrade(monkey,'101')
def up110(monkey):
    mupgrade(monkey,'110')
def up120(monkey):
    mupgrade(monkey,'120')
def up102(monkey):
    mupgrade(monkey,'102')
def up103(monkey):
    mupgrade(monkey,'103')
def up104(monkey):
    mupgrade(monkey,'104')
def up105(monkey):
    mupgrade(monkey,'105')
def up200(monkey):
    mupgrade(monkey,'200')
def up201(monkey):
    mupgrade(monkey,'201')
def up202(monkey):
    mupgrade(monkey,'202')
def up203(monkey):
    mupgrade(monkey,'203')
def up204(monkey):
    mupgrade(monkey,'204')
def up205(monkey):
    mupgrade(monkey,'205')
    
def up301(monkey):
    mupgrade(monkey,'301')
def up302(monkey):
    mupgrade(monkey,'302')
def up401(monkey):
    mupgrade(monkey,'401')
def up402(monkey):
    mupgrade(monkey,'402')
def up501(monkey):
    mupgrade(monkey,'501')
def up502(monkey):
    mupgrade(monkey,'502')

def up101(monkey):
    mupgrade(monkey,'101')
def up100(monkey):
    mupgrade(monkey,'100')
def up220(monkey):
    mupgrade(monkey,'220')
def up420(monkey):
    mupgrade(monkey,'420')
def up520(monkey):
    mupgrade(monkey,'520')
def up230(monkey):
    mupgrade(monkey,'230')
def up240(monkey):
    mupgrade(monkey,'240')
def up250(monkey):
    mupgrade(monkey,'250')
def up320(monkey):
    mupgrade(monkey,'320')
def up510(monkey):
    mupgrade(monkey,'510')
def up500(monkey):
    mupgrade(monkey,'500')
def up150(monkey):
    mupgrade(monkey,'150')
def up300(monkey):
    mupgrade(monkey,'300')
def up400(monkey):
    mupgrade(monkey,'400')
def up410(monkey):
    mupgrade(monkey,'410')
def up130(monkey):
    mupgrade(monkey,'130')
def up140(monkey):
    mupgrade(monkey,'140')
def up210(monkey):
    mupgrade(monkey,'210')
def up000(monkey, validation=True,slow=False):
    mupgrade(monkey, validation,slow)



def collect_chain():
    instawanted=0#初始化点击想要的insta
    # start 活动 识别方案
    print('[%s]收集活动阶段开始执行' % get_datetime())
    time.sleep(6)#8
    for i in range(1000):
        # # 刚返回的时候, 在主页面的, 要稍等一会才加载活动页面, 不用了上面有睡眠
        
        if i > 15:
            click(global_point_map['home_empty4'], times=2, cd=1)



        if instawanted==0:
            try:#有bug，该功能暂时关闭
                # location_instawanted = pyautogui.locateOnScreen(image=image_path['instawanted'], confidence=0.8, grayscale=True)
                # location_instawanted2 = pyautogui.locateOnScreen(image=image_path['instawanted2'], confidence=0.8, grayscale=True)
                # location_instawanted3 = pyautogui.locateOnScreen(image=image_path['instawanted3'], confidence=0.8, grayscale=True)
                # if location_instawanted:
                #     x,y=location_instawanted
                # if location_instawanted2:
                #     x,y=location_instawanted2
                # if location_instawanted3:
                #     x,y=location_instawanted3
                # print('[%s]识别想开的猴子，点击该insta' % get_datetime())
                # click((x, y), cd=1, no_origin=True)
                # time.sleep(1)
                # instawanted=1
                # continue
                location_wanted = pyautogui.locateOnScreen(image=image_path['instawanted'], confidence=0.8, grayscale=True)
                x, y = pyautogui.center(location_wanted)
                print('[%s]识别想开的猴子，点击该insta' % get_datetime())
                click((x, y), cd=1, no_origin=True)
                time.sleep(1)
                instawanted=1
                continue
            except Exception as e:
                pass


        try:
            location = pyautogui.locateOnScreen(image=image_path['collected'],confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            time.sleep(2)
            print('[%s]识别到开始, 奖励搜集完毕' % get_datetime())
            click(global_point_map['return'], times=1)
            break
        except Exception as e:
            pass

        try:
            location_button = pyautogui.locateOnScreen(image=image_path['collection_button'], confidence=0.8, grayscale=True)
            if location_button:
                print('[%s]识别到收集按钮, 继续开箱子' % get_datetime())
                click(global_point_map['collection'], times=1, cd=1)
                time.sleep(2)
                continue
        except Exception as e:
            pass



        try:
            location = pyautogui.locateOnScreen(image=image_path['social'], confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]识别到开局页面,退出盲盒点击阶段' % get_datetime())
            break
        except Exception as e:
            pass
         
        

        

        
        try:
            location = pyautogui.locateOnScreen(image=image_path['box'], confidence=0.8, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]图片识别到 insta盲盒, 坐标: %s, %s' % (get_datetime(), x, y))
            # 点击第一次开箱
            click((x, y), cd=1, no_origin=True)
            time.sleep(2)
            
            # 2022-10-25 00:27:21 开箱之后截图保存
            # 2022-10-25 00:56:28 只保存5阶
            need_save = False
            a = 4
            # 识别四阶
            # location4 = pyautogui.locateOnScreen(image=path_insta_4, confidence=0.7, grayscale=True)
            # if location4:
            #     queue_infos['insta'] ='5'
            #     instaquantity += 1
            #     # print(instaquantity)
            #     print('[%s]获得4阶insta'%get_datetime())
            #     need_save = True
            
            # 识别五阶
            location5 = pyautogui.locateOnScreen(image=image_path['insta_5'], confidence=0.7, grayscale=True)
            if location5:
                a = 5
                need_save = True
                
            
            if need_save:
                print("[%s]恭喜你获得一个5阶insta，可以在insta中查看"%get_datetime())
                im = pyautogui.screenshot(region=[*origin,1366, 768])
                
                img_path = 'insta'
                # 路径不存在时创建
                if not os.path.exists(img_path):
                    os.makedirs(img_path)
                t = get_datetime()
                t = t.replace(':', '_')
                t = t.replace('-', '_')
                
                im.save('%s/%s %s阶.png' % (img_path, t, str(a)))
                variable_list['5阶insta数']+=1
            # 点击第二次确认, 回到开箱页面继续开箱, 多点击几次,最后一次能回到活动页面
            click((x, y), times=2, cd=1, no_origin=True)
            time.sleep(2)
            
            # 不用break, 识别到一个点一个, 直到点完之后到活动主页面, 识别到主页面就退出循环了
        
        except Exception as e:
            pass

    print('[%s]活动阶段代码执行完毕' % get_datetime())






##竞速活动函数start
def 加速回合(times=1, cd=0.001):
    global signal_blocking
    block()
    
    # 模拟按键动作
    keyboard.press(Key.shift)
    for i in range(times):
            keyboard.press(Key.space)  # 按键按下
            keyboard.release(Key.space)  # 按键抬起
            time.sleep(cd)
    keyboard.release(Key.shift)

##竞速活动函数end


