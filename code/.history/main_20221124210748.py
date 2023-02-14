# 2022-10-16 18:01:09 识别到insta就结束, 卡顿之后一直卡在下一页, 加上下一页识别, 所有识别降低图片精确度

import copy
import os
import re
import random
import threading
import traceback

import win32api
import ctypes
import ctypes.wintypes

from settings_file.autogame import *
from settings_file.path import *
from settings_file.chains_map import *
from settings_file.collect import *
# from settings_file.position_map import *
from settings_file.yoursettings import *
import pynput.mouse as pm
# import ctypes
# import time

pyautogui.FAILSAFE = False

# start 常量区

# end 常量区

def exec_chains(new_chains, qi=None):
    # 这个是单独计算的时间轴, 执行完pre才开始的, 耗时统计在外层循环
    start_time = time.time()
    
    # is_fail = False  # 失败不应该在这里判断了, 由另一个线程判断
    print('[%s]游戏开始' % get_datetime())
    
    while True:
        
        # 2022-10-23 07:27:42 初次执行报错点
        if new_chains:
            this_chains = new_chains[0]
        
        # 如果没有动作链了再取值就报错了, 这里就该break结束了
        else:
            break
        
        if this_chains[0] == 'pre':
            # 表示这个是前置动作
            exec(this_chains[1])
            
            # 执行完要修改动作链, 删除执行过的
            new_chains = new_chains[1:]
            time.sleep(0.5)
            start_time = time.time()  # 执行完重新开始算时间
            continue
        
        # 乘以 小数 的原因是想时间轴提前一点, 虽然屏幕占用会高一点, 感觉放的有点不及时
        if (time.time() - start_time) > (this_chains[0] * 0.5):
            
            # 到达时间戳了就执行动作
            exec(this_chains[1])
            
            # 执行完要修改动作链, 删除执行过的
            new_chains = new_chains[1:]
            time.sleep(1)
            continue
        
    
    print('[%s] 动作链执行完毕' % get_datetime())
    return
    
    



# 按键函数

def on_press(key):
    global signal_blocking
    if str(key) == r"'\x02'":
        
        # Ctrl+B  暂停脚本
        print('[%s] 检测到按键 Ctrl + B, 停止脚本' % (get_datetime()))
        signal_blocking.clear()
        signal_blocking.append(time.time())
        
    
    if str(key) ==r"'\x04'":
        # Ctrl+D  恢复阻塞, 虽然不会立刻就恢复
        print('[%s] 检测到按键 Ctrl + D, 继续脚本' % get_datetime())
        signal_blocking.clear()
        signal_blocking.append(0)
    
    if str(key) == r"'\r'":
        # Ctrl+M 退出程序, 给 while True?
        print('[%s] 检测到按键 Ctrl + M, 结束程序' % get_datetime())
        os._exit(0)  # 用在fork出来的线程中, 结束整个程序


# 按键监听函数
def key_monitor():
    with Listener(on_press=on_press) as listener:
        listener.join()


def exec_imp_chain(is_activation=False, imp_map='峡谷'):
    is_activation = False
    script_mode='onecircle'
    global queue_infos
    print("========================================================\n"
          "|请先调好以下设置再运行脚本                      |\n"
          "|必要设置：以下4个设置一定要调,不然90%会出问题             |\n"
          "|1. 游戏的屏幕尺寸 1366x768 非全屏模式 调好后请重新打开游戏|\n"
          "|如果显示器不支持1366x768那就无法用这脚本，目前没有做其他分辨率适配|\n"
          "|不然会出现猴子放不准的问题，调完不重启游戏，移动窗口分辨率会变 |\n"
          "|重启游戏分辨率就会稳定                                 |\n"
          "|2. 屏幕分辨率 1920x1080  显示缩放大小最好为100%; (不能升级就调缩放)|\n"
          "|3. 游戏设置 拖放 勾上禁用微调模式, 勾上自动开始|\n"
          "|4. 游戏语言 !!简体中文!!   图片识别的是中文            |\n"
          "|==>游戏快捷键:默认是使用默认，想改可以改热键设置.ini|\n"
          "|运行中不要乱点到游戏外面                               |\n"
          "|注意：运行脚本进入地图会把之前的存档覆盖                 |\n"
          "|如果导致某个动作没放上, 请手动补上该操作               |\n"
          "|快捷键说明                                             |\n"
          "|Ctrl+B 停止脚本                                        |\n"
          "|Ctrl+D 继续运行                                        |\n"
          "|Ctrl+Q 查看日志                                        |\n"
          "|Ctrl+M 退出程序                                        |\n"
          "========================================================\n"

          "==========================\n"
          "运行脚本时，请确保游戏位于画面最前面\n"
          "请进入游戏主页再输入数字运行脚本模式\n"
          "图没解锁，请先把前面的困难替代气球打了\n"
          "温馨提示：进入地图打开相应模式也能刷\n"
          "= 输入 0 双金专家极难活动搜集    =\n"
          "= 输入 1-10 对应专家极难图      =\n"
          "= 1为双金无知识刷放气        \n"
          "= 11为无双金无知识刷放气 ←啥都没有刷这个\n"
          "= 12为无双金无知识刷简单极难\n"
          "= 13为无双金全知识刷专家极难←没双金刷这个\n"
          "= 20为刷金气球模式         \n"
          "= -10为循环自制打法模式       \n"
          "= -2为给游戏画面截图         \n"
          "= -5为自动使用技能         \n"
          "= -4为合作挂机给钱模式         \n"
          "= -9为寻找坐标模式      \n"
          "= 脚本主要由b站：无名的小族 制作，有问题请私信或联系qq1310950614\n"
          "==========================\n")


    while True:
        event = input('请输入模式:')
        try:
            event = int(event)
        except Exception as e:
            print('输入内容不是数字')

        if event in [-10,-9,-6,-5,-4,-3,-2,-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,20,30]:
            break
        
    map_hero_need=global_point_map['game_right']
    run_thread(key_monitor)# 开个线程监听组合键事件
    if event == 0:
        is_activation = True
        print('即将进入双金额外奖励搜集模式，请注意是否具备以下条件'
          "|image\n"
          "|==>知识，英雄:(无知识或英雄请走图1先刷经验或者猴钞) |\n"
          "|0. 需要双金，没有找人帮你开 或者steam买了再退款        |\n"
          "|1. 主要：更多现金                                         |\n"
          "|2. 军事：军事征兵(高级后勤可能需要)                     \n"
          "|3. 英雄：授权英雄                                      |\n"
          "|4. 力量：预先准备                            |\n"
          "|如果不想程序开箱子:                                    |\n"
          "|可以在360或者腾讯管家的网络监控下，禁止气球塔防的网络      |\n"
        
        )
        map_hero_need=global_point_map['map_etn']
    
    elif event == -1:
        print('即将进入过关测试模式')
        exec(open("打法.py",encoding='utf-8').read())
        chains = 自定义打法
        exec_chains(chains, queue_infos)
        # exec(all_chains['test'][0][0])
        sys.exit(0)

    elif event == -2:
        is_activation = False
        print('即将进入截图模式，图片保存在images/debug_imgs')
        click((), times=2)
        pyautogui.screenshot(region=[*origin, 1366, 768]).save('images/debug_imgs/游戏截图%s.png'%get_datetime().replace(':', '_').replace('-', '_')) 
        sys.exit(0)
    
    elif event == -3:
        print('即将进入测试模式2')
        sys.exit(0)

    elif event == -4:
        is_activation = False
        print('即将进入合作挂机模式')
        print('请选择给钱对象1，2，3')
        gived=input()
        time.sleep(1)
        click(global_point_map['exchange'])
        while True:
         time.sleep(3)
         click(global_point_map['givemoney%s'%gived],cd=0.2,times=5)
        
        sys.exit(0)
    elif event == -5:
        is_activation = False
        print('进入自动点击技能模式')
        print('请输入你要开启的技能数字为对应技能，a为全部')
        abilities=input()
        print('请输入一次点击的次数')
        clicktimes=input()
        click(global_point_map['game_right'], times=2)
        if abilities=="a":
          ability("0123456789")
          time.sleep(1000)
        else:
          ability(abilities,clicktimes)
          time.sleep(1000)

        sys.exit(0)
    elif event == -6:
        print('自动合作模式')
        click(global_point_map['game_right'], times=2)

    elif event == -9:
        print('找坐标模式')
        def on_click(x, y, button, pressed):
            get_origin()
            # 监听鼠标点击
            if pressed:
                # ox, oy = get_origin()
                mxy="{},{}".format(x-origin[0], y-origin[1])
                # print("([%s])"%mxy)
                print("[%s]"%mxy)
            if not pressed:
                return False
        while True:
            x, y = pyautogui.position()
            with pm.Listener(on_click=on_click) as pmlistener:
                pmlistener.join()



    elif event == -10:
        imp_map = event
        print('即将进入循环打自定义打法，确保打法.py存在，且代码格式正确')
        if 自选英雄 !="":
         map_hero_need=global_point_map['map_%s'%自选英雄]


    elif event == 20:
        is_activation = False
        script_mode='gold'
        print('即将进入刷金气球模式')
        map_hero_need=global_point_map['map_sauda']
        print('将选择英雄萨乌达')

    elif event == 30:
        print('即将进入自选模式，请输入chian名称')
        exec_chains(all_chains[input()])
        sys.exit(0)



    else:
        is_activation = False
        imp_map = event
        print('即将进入 单刷模式')
        if event in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,14,15]:
            map_hero_need=global_point_map['map_etn']
            print('将选择英雄艾蒂安')
        
        # elif event == 13:
        #     map_hero_need=global_point_map['map_psi']
        #     print('将选择英雄灵机')

        elif event ==13:
            map_hero_need=global_point_map['map_quincy']
            print('将选择英雄昆西')


    print('[%s] 脚本将在2秒后运行' % get_datetime())
    time.sleep(2)
    click([1366,768],times=1)
    click([0,768],times=1)
    print("[%s]确认原点坐标是否取游戏画面左上角，若不在游戏画面左上角，请调整画面设置"% get_datetime())
    click([0,0],times=2)
    time.sleep(3)
    click(global_point_map['map_hero'], times=1)
    print("[%s]选择英雄"% get_datetime())
    click(map_hero_need, times=1)
    click(global_point_map['map_select'], times=1)
    click(global_point_map['map_heroback'], times=1)

    exec_times = 0
    fail_times = 0
    simple_times = 0

    
    while True:
        all_start_time = datetime.now()
        
        # 2022-10-24 21:12:56 初始化queue_infos的status字段, 这个循环 在开出去线程后, 靠这个字段阻塞的
        #                     是说怎么一直执行

        queue_infos['status'] = ''
        queue_infos['mode'] = ''
        
        click(global_point_map['window_Bottom_right'], times=2)
        click(global_point_map['start'], times=1)
        click(global_point_map['s3'], times=1)
        click(global_point_map['s4'], times=1)
        
        
        chains = all_chains['黑暗城堡放气']#再执行其他chain出问题时自动跳转到执行这条chain

        
        if script_mode=="gold":
            click(global_point_map['s1'], times=1)
            is_find = False
            time.sleep(1)
            
            page = None
            # 识别页数
            signal_restart = False  # 是否需要重新执行循环
            
            for i in range(20):
                img = pyautogui.screenshot(region=[*origin, 1366, (768)])
                location_gold = pyautogui.locateOnScreen(image=path_goldbloon, confidence=0.60, grayscale=True)

                if not location_gold:
                    # 找不到就下一页, 然后再查找金气球
                    time.sleep(0.5)
                    click(global_point_map['s1'], times=1)
                    time.sleep(0.5)
                    continue
                for n in page_position:#识别页数
                    position_list = copy.deepcopy(page_position[n])
                    
                    threshold = 10  # 阈值
                    aru = (64, 159, 255)  # 浅蓝
                    pixel = img.getpixel(tuple(position_list))

                    
                    if abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold:

                        page=n
                # 找对应点

                time.sleep(3)#防止气球动画未加载完
                x, y = pyautogui.center(location_gold)
                

                # 表示在第 i 页找到了额外奖励图标
                # 获取对应的chains
    
                for m in map_position:
    
                    if int(map_position[m][0]) == int(page):
                        # 表示在这一页内
        
        
                        if map_position[m][1][0] < (x - origin[0]) < map_position[m][2][0] and map_position[m][1][1] < (y - origin[1]) < map_position[m][2][1]:
                            
                            
                            chains = copy.deepcopy(all_chains[m])
                            
            
                            # 2022-10-19 00:58:13
                            print('[%s]识别到金气球的副本,名称:%s, 坐标: %s,%s' % (get_datetime(), m, x, y))
                            click((x, y), no_origin=True)  # 这一步是点击对应的图
                            queue_infos['mode'] ='simple'
                            click(global_point_map['medium'], times=1)
                            click(global_point_map['standard'], times=1)
                            # 之后就能进到对应的图了
                            is_find = True
                            break
                            
                
                if is_find:
                    break
                    
                # 一般不会,如果30次还没找到就Esc 退出到主页面从来
                if i > 10:
                    key(Key.esc, times=12)
                    location2 = pyautogui.locateOnScreen(image=path_exit_cancel, confidence=0.8, grayscale=True)
                    if location2:
                        # 点击取消
                        click((550, 510), times=3)
                    
                    signal_restart = True
                    break

            if signal_restart:
                # 下一轮循环重新选择
                continue
                
            if not is_find:
                # 没找到就重来吧, 刷暗堡去
                print('[%s] 没有找到金气球,返回刷暗黑城堡动作' % get_datetime())
                key(Key.esc, times=4)
                click(global_point_map['window_Bottom_right'], times=2)
                click(global_point_map['start'], times=1)
                click(global_point_map['s3'], times=1)
                click(global_point_map['s4'], times=1)
                click(global_point_map['s4'], times=1)
                click(global_point_map['map_dark'], times=1)
                click(global_point_map['simple'], times=1)
                click(global_point_map['deflation'], times=1)


        elif is_activation:
            # 这里是一个找额外奖励的循环, 两轮, 找不到就刷暗堡
            
            is_find = False
            time.sleep(1)
            
            page = None
            # 识别页数
            signal_restart = False  # 是否需要重新执行循环
            
            for i in range(6):#这里是找6次没找到退出寻找
                location = pyautogui.locateOnScreen(image=path_canyon, confidence=0.8, grayscale=True)
                
                if location:
                    page = 11
                else:
                    location2 = pyautogui.locateOnScreen(image=path_dark_castle, confidence=0.8, grayscale=True)
                    if location2:
                        page = 12

                # 找对应点
                location_extra = pyautogui.locateOnScreen(image=path_extra, confidence=0.75, grayscale=True)
                
                if not location_extra:
                    # 找不到就下一页, 然后再查找额外奖励
                    time.sleep(0.5)
                    click(global_point_map['s4'], times=1)
                    time.sleep(0.5)
                    continue
                x, y = pyautogui.center(location_extra)
    
                for m in map_position:

    
                    if int(map_position[m][0]) == int(page):
                        # 表示在这一页内
        
        
                        if map_position[m][1][0] < (x - origin[0]) < map_position[m][2][0] and \
                                map_position[m][1][1] < (y - origin[1]) < map_position[m][2][1]:
                            
                            chains = copy.deepcopy(all_chains[m])
                            
            
                            # 2022-10-19 00:58:13
                            print('[%s]识别到额外奖励的副本,名称:%s, 坐标: %s,%s' % (get_datetime(), m, x, y))
                            # 避难所的点击顺序不一样,要判断一下
                            click((x, y), no_origin=True)  # 这一步是点击对应的图
            
                            if m == '避难所':
                                click(global_point_map['simple'], times=1)
                                click(global_point_map['standard'], times=1)
                                queue_infos['mode'] ='simple'
            
                            else:
                                queue_infos['mode'] ='imp'
                                click(global_point_map['difficulty'], times=1)
                                click(global_point_map['imp'], times=1)
            
                            # 之后就能进到对应的图了
                            is_find = True
                            break
                            
                    if is_find:  # 找到了就退出循环
                        break
                
                if is_find:
                    break
                    
                # 一般不会,如果30次还没找到就Esc 退出到主页面从来
                # 可以加一个长时间不执行动作是 执行“重开”游戏和脚本 利用key.esc，和失败点击esc时出现的内容，来防止死循环 
                if i > 6:
                    key(Key.esc, times=12)
                    location2 = pyautogui.locateOnScreen(image=path_exit_cancel, confidence=0.8, grayscale=True)
                    if location2:
                        # 点击取消
                        click((550, 510), times=3)
                    
                    signal_restart = True
                    break
            
            if signal_restart:
                # 下一轮循环重新选择
                continue
                
            if not is_find:
                # 没找到就重来吧, 刷暗堡去
                print('[%s] 没有找到额外奖励图标,返回刷暗黑城堡动作' % get_datetime())
                key(Key.esc, times=4)
                click(global_point_map['window_Bottom_right'], times=2)
                click(global_point_map['start'], times=1)
                click(global_point_map['s3'], times=1)
                click(global_point_map['s4'], times=1)
                click(global_point_map['s4'], times=1)
                click(global_point_map['map_dark'], times=1)
                click(global_point_map['simple'], times=1)
                click(global_point_map['deflation'], times=1)
        elif event==-10:
                exec(open("打法.py",encoding='utf-8').read())
                chains = 自定义打法

        else:
            def enter(imp_map,map_level,map_level_times,map_postion,gamelevel,mode):
                nonlocal chains
                click(global_point_map[map_level], times=map_level_times)
                click(global_point_map[map_postion], times=1)
                click(global_point_map[gamelevel], times=1)
                click(global_point_map[mode], times=1)
                chains = all_chains[imp_map]
            

            if str(imp_map) == '1':
                enter('避难所放气',"game_right",1,'map_1','simple','deflation')
            elif str(imp_map) == '2':
                enter('峡谷',"game_right",1,'map_2','difficulty','imp')
            elif str(imp_map) == '3':
                enter('水淹山谷',"game_right",1,'map_3','difficulty','imp')
            elif str(imp_map) == '4':
                enter('炼狱',"game_right",1,'map_4','difficulty','imp')
            elif str(imp_map) == '5':
                enter('血腥水坑',"game_right",1,'map_5','difficulty','imp')
            elif str(imp_map) == '6':
                enter('工坊',"game_right",1,'map_6','difficulty','imp')
            elif str(imp_map) == '7':
                enter('方院','s4',1,'map_1','difficulty','imp')
            elif str(imp_map) == '8':
                enter('黑暗城堡','s4',1,'map_2','difficulty','imp')
            elif str(imp_map) == '9':
                enter('泥泞的水坑','s4',1,'map_3','difficulty','imp')
            elif str(imp_map) == '10':
                enter('哎哟','s4',1,'map_4','difficulty','imp')
            elif str(imp_map) == '11':
                enter('黑暗城堡放气','s4',1,'map_2','simple','deflation')
            elif str(imp_map) == '12':
                enter('溜冰鞋单金','s1',2,'map_1','difficulty','imp')
            elif str(imp_map) == '13':
                enter('炼狱极难单金','game_right',1,'map_4','difficulty','imp')
            elif str(imp_map) == '14':
                enter('避难所','game_right',1,'map_1','simple','standard')
            elif str(imp_map) == '15':
                enter('度假胜地点击','s1',1,'map_6','difficulty','chimps')


        
        time.sleep(1)
        
        # 到这里应该是进入到对应图了
        
        try:
            location = pyautogui.locateOnScreen(image=path_cover, confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]识别到覆盖存档确认框,点击' % get_datetime())
            time.sleep(1)
            click(global_point_map['cover'])
        
        except Exception as e:
            pass
        
        time.sleep(4)
        click(global_point_map['yes1'], times=1)
        time.sleep(1)
        
        # 开始执行chains
        try:
            queue_infos['thread_exec'].raise_exception()
        except Exception as e:
            pass
            # print('[%s] 开始前尝试销毁执行线程异常, %s' % (get_datetime(), e))
            
        try:
            queue_infos['thread_monitor'].raise_exception()
        except Exception as e:
            pass
            # print('[%s] 开始前尝试销毁监听线程异常, %s' % (get_datetime(), e))
            
        queue_infos['status'] = ''  # 再初始化, 虽然没啥意义
        
        queue_infos['thread_exec'] = thread_with_exception(exec_chains,
                                                           (chains, queue_infos),
                                                           'thread_exec',
                                                           True)
        queue_infos['thread_exec'].start()
        
        queue_infos['thread_monitor'] = thread_with_exception(monitor,
                                                              (queue_infos,  ),
                                                              'thread_monitor',
                                                              True)
        queue_infos['thread_monitor'].start()
        #改进版本但无法同时中断
        # run_thread(exec_chains,(chains, queue_infos),'thread_exec',True)
        # run_thread(monitor,(queue_infos,  ),'thread_monitor',True)

        # 线程都开出去了,这里要阻塞
        
        while True:
            if queue_infos.get('status', '') in ['success', 'fail']:
                break
                
            # 3秒一次影响也不大, 别让CPU太累
            time.sleep(3)
        
        
        # 到此应该回到主页了
        time.sleep(3)#等待操作结束simple_times

        
        

        # start 活动 识别方案 
        if is_activation:
         collect_chain()
        
        time.sleep(0.5)
        click(global_point_map['game_right'], times=2, cd=1)  # 点击页面空白处
        
        exec_times += 1
        if queue_infos['status'] == 'fail':#监测失败次数
            fail_times += 1
        if queue_infos['mode'] == 'simple':#监测放气次数
            simple_times += 1
        end_time = datetime.now()
        
        print('[%s]已进行%2d轮, 耗时: %s秒, 本轮开始时间: %s' % (
                get_datetime(),
                exec_times,
                int((end_time - all_start_time).total_seconds()),
                datetime.strftime(all_start_time, '%Y-%m-%d %H:%M:%S'),
                    )
              )
        if is_activation:
            print('[%s]其中避难所简单轮数：%s' % (get_datetime(), simple_times))
        print('[%s]累计失败次数: %s' % (get_datetime(), fail_times))
        time.sleep(2)
        click(global_point_map['window_Bottom_right'])#此时完全进入主页


# end 函数区

get_origin()  # 先运行一次设置值
queue_infos = dict()


if __name__ == '__main__':
    
    # 闭环测试 识别流程
    exec_imp_chain(is_activation=True)
