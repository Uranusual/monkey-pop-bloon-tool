
from basic import *
from chains_map import *
pyautogui.FAILSAFE = False

# start 常量区
# end 常量区
# #start 变量定义区
# end 变量定义区


def exec_imp_chain():
    script_mode = 'onecircle'
    global queue_infos
    print("========================================================\n"
          "|请先调好以下设置再运行脚本，为了保证脚本点击时不受鼠标干扰请使用管理员模式运行脚本|\n"
          "|必要设置：以下4个设置一定要调,不然90%会出问题             |\n"
          "|1. 游戏的屏幕尺寸 1366x768,1280x720,1600x900非全屏模式|\n"
          "|游戏尺寸不对会闪退|\n"
          "|不然会出现猴子放不准的问题，调完不重启游戏，移动窗口分辨率会变 |\n"
          "|出现坐标偏差,请更换应用缩放，重新启动电脑|\n"
        #   "| 系统显示设置的应用缩放大小为100%|\n"
        #   "|2. 屏幕分辨率不用动，用原系统的分辨率，也是就你屏幕最大的分辨率|\n"
          
           "|坐标不对，就调完应用缩放重新启动游戏或者电脑|\n"
           "|如果有修复应用缩放的选项且开启了的，请关闭后试一试，|\n如果使用的显示器分辨率不是最大的请设为最大|\n"
          "|3. 游戏设置 拖放 打开‘禁用微调模式’, 打开‘自动开始’|\n"
          "|4. 游戏语言 !!简体中文!!   图片识别的是中文            |\n"
          "|==>游戏快捷键:默认是使用默认，想改可以改热键设置.ini|\n"
          "|运行中不要乱点到游戏外面                               |\n"
          "|注意：运行脚本进入地图会把之前的存档覆盖                 |\n"
          "|左键点击脚本会暂停，要继续请右键一下脚本  |\n"
          "|如果导致某个动作没放上, 请手动补上该操作               |\n"
          "|快捷键说明                                             |\n"
          "|Ctrl+B 停止脚本                                        |\n"
          "|Ctrl+D 继续运行                                        |\n"
          "|Ctrl+滑动滚轮可以缩放脚本               |\n"
          "|Ctrl+M 退出程序                                        |\n"
          "========================================================\n"

          "==========================\n"
          "运行脚本时，请确保游戏位于画面最前面\n"
          "请进入游戏主页再输入数字运行脚本模式\n"
          "图没解锁，请先把图解锁,刷图前注意是否有重要地图存档，脚本刷到改图会覆盖存档\n"
          "温馨提示：进入地图打开相应模式也能刷\n"
          "=实用模式区：    =\n"
          "= 0为输入地图及难度进入循环刷单图,重新开始刷单图得不到收集材料    =\n"
          "= 1为无双金无知识刷黑暗城堡放气 ←啥都没有的新号刷这个\n"
          "= 2为黑暗城堡点击 ←啥都没有的新号刷这个\n"
          "= 3为无双金全知识/双金无知识刷专家炼狱极难 ←有双金的新号,有知识优先刷这个\n"
          "= 4双金专家极难活动收集    =\n"
          "= 5无双金专家简单活动收集    =\n"
          "=实用功能：\n"
          "=11为合作挂机给钱模式\n"
          "=12为自动使用技能 \n"
          #   "=\n"
          #   "=\n"
          #   "=\n"
          "= 14为自动开箱子模式，请在开箱子界面运行   =\n"
          #   "= 12为无双金无知识刷简单极难 ←移动堡垒，小气球成就刷这个\n"
          #   "= 13为无双金全知识/双金无知识刷专家极难←刷经验猴币首选）\n"
          #   "= 17为中级双金极难\n"
          '=成就区：(目前只开通部分，请使用-模式手输进入地图\n'
          #   "= 15为度假胜地点击，完成2tc成就\n"
          #   "= 16为玉米的点击，完成颗粒无收\n"
          #   "= 16为黑暗城堡的点击，完成希尔的常数\n"
          "= 20为刷金气球击破数成就模式         \n"
          "= 21为解锁小猴子塔成就         \n"
          "= 其他成就自己猜打哪个图，伸手拿的，我就懒得给你单独弄了 \n"
          '=开发区：\n'
          "= -1为循环运行打法.py文件(目前不循环点击)         \n"
          "= -2寻找坐标模式\n"
          "= -3猴子坐标测试(测试打法中猴子能不能放准)\n"
          #   "= -2为给游戏画面截图         \n"
          "= 脚本主要由b站：无名的小族 制作，有问题请入q群709918803询问\n"
          "= 想体验更多功能，请上传打法，获得限免版的权限\n"
          "==========================\n")

    while True:
        event = input('请输入模式:')#可以开快捷键回到这里
        try:
            event = int(event)
        except Exception as e:
            print('输入内容不是数字')

        if event in [-12, -11, -10, -9, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]:
            break
        if event == 100:
            exec(open("自定义代码.py", encoding='utf-8').read())
            print("引入自定义代码成功")

    get_origin()  # 先运行一次设置值
    run_thread(key_monitor,type="script_thread")  # 开个线程监听组合键事件
    
    # 点击游戏界面

    if event == -1:
        print('即将执行打法')
        # exec(open("自定义代码.py",encoding='utf-8').read())
        # print('自定义代码执行完毕，将继续执行脚本')
        variable_list['chain'] = open("打法.py", encoding='utf-8').read()
        variable_list['script_mode'] = 'cricleone'
        variable_list['mode'] = ''
        # input('继续脚本？')

    elif event == -2:
        print('找坐标模式,最好使用1366来获取')
        # get_position1()
        while True:
            block()
            print(get_position())

    elif event == -3:
        print('放置坐标测试模式')
        print('将跳过打法中的升级操作执行打法.py,而且修改文件够可直接回车重新运行')
        # get_position1()
        variable_list['position_test']=True
        while True:
            exec(open("打法.py",encoding='utf-8').read())
            input('回车,重新测试坐标')
    if event == -4:
        print('即将进入编辑器测试打法模式')
        exec(open("打法.py",encoding='utf-8').read())
        print('自定义代码执行完毕，将继续执行脚本')
        # variable_list['chain'] = open("打法.py", encoding='utf-8').read()
        # variable_list['script_mode'] = 'cricleone'
        input('继续脚本？')

    elif event == -7:  # 测试模式
        print('自动获取猴子堆叠坐标')
        depolyedmonkey = input('请输入你要放置的猴子的快捷键')
        mposition = [1144, 745]  # 毛毛右下[1146,748]毛毛左上[42,18] 横向可以24只毛毛
        while True:

            testposition(depolyedmonkey, mposition,
                         validation=True, show_log=False)
            mposition[0] -= 47

    elif event == -4:
        print('即将进入截图模式，图片保存在images/debug_imgs')
        click([1366, 768], times=3)
        pyautogui.screenshot(region=[origin[0], origin[1], w_h]).save(
            'images/debug_imgs/游戏截图%s.png' % get_datetime().replace(':', '_').replace('-', '_'))
        sys.exit(0)

    elif event == -3:
        print('自动获取猴子堆叠坐标')
        depolyedmonkey = input('请输入你要放置的猴子的快捷键')
        mposition = [42, 748]  # 毛毛右下[1146,748]毛毛左上[42,18] 毛毛极限可以放24x17个
        while True:
            testposition(depolyedmonkey, mposition,
                         validation=True, show_log=False)
            mposition[0] += 4

    elif event == 10:
        powerused = input('你要实用的力量:')
        times = input('你要实用的次数')
        power(powerused, times=times)
        sys.exit(0)

    elif event == 11:
        print('即将进入合作挂机模式')
        print('请选择给钱对象1，2，3')
        gived = input()
        time.sleep(1)
        click(global_point_map['exchange'])

        threshold = 10  # 阈值
        aru = (112, 232, 0)  # 浅绿(80, 202, 0)
        point2 = global_point_map['givemoney%s' % gived][0]*variable_list['width'] / \
            1366, global_point_map['givemoney%s' %
                                   gived][1]*variable_list['width']/1366

        # img.save('images/debug_imgs/游戏截图%s.png'%get_datetime().replace(':', '_').replace('-', '_'))
        while True:
            time.sleep(2)
            block()
            # 根据像素判断被给钱的是否掉线
            img = pyautogui.screenshot(region=[*origin, 1600, 900])
            pixel = img.getpixel(tuple(point2))
            # print(point2)
            # print(pixel)
            if abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold and abs(pixel[0] - aru[0]) < threshold:
                click(global_point_map['givemoney%s' %
                      gived], cd=0.1, times=10)
            else:
                print('[%s] 未检测到绿色，将停止点击' % get_datetime())

        sys.exit(0)
    elif event == 12:
        print('进入自动点击技能模式')
        print('请输入你要开启的技能数字为对应技能，a为全部')
        abil = input()
        print('请输入一次点击的次数')
        clicktimes = input()
        click(global_point_map['game_right'], times=2)
        if abil == "a":
            abilities("0123456789")
        # elif abilities=="a"
        else:
            abilities(abil, clicktimes)
    elif event == 13:
        # depolyedmonkey=input('请输入你要放置的猴子的快捷键：')
        print('自动献祭升猴子模式,请点击初始猴子的位置')
        # mposition=[42,748]#毛毛右下[1146,748]毛毛左上[42,18] 毛毛极限可以放24x17个
        献祭猴子(input('请输入你要放置的猴子的快捷键：'), get_position())

        sys.exit(0)

    elif event == 14:
        print('自动收集模式')
        collect_chain()
        sys.exit(0)

    elif event == 15:
        print('即将进入循环打自定义打法，确保打法.py存在，且代码格式正确')
        variable_list['chain'] = eval(open("打法.py", encoding='utf-8').read())

        # exec_chains(chains, queue_infos)
        # input('再次执行')

    elif event == 0:
        while True:
            needmap = input('请输入你要循环刷的图：')
            if needmap in all_chains:
                needmode = input('请输入地图模式：')
                if needmode in all_chains[needmap]:
                    break
            print('你输入的名称有误，或者脚本未收录对应打法')

    elif event == 1:
        print('即将循环刷专家放气，只要黑暗城堡放气解锁即可')

    elif event == 2:
        print('即将循环刷专家点击，解锁灵机和黑暗城堡点击即可')
    elif event == 3:
        print('即将循环刷专家极难，需要解锁炼狱极难，双金或部分知识可过')

    elif event == 4:  # 后面为直接运行的程序
        variable_list['script_mode'] = '双金收集'
        print('即将进入双金额外奖励搜集模式，请注意是否具备以下条件'
              #   "|image/instawanted为你想要选的insta猴子\n"
              "|该模式循环打专家极难，避难所是打简单，确保相关图解锁|\n"
              "|==>知识，英雄:(无知识或英雄请走图1先刷经验或者猴钞) |\n"
              "|0. 需要双金，没有找人帮你开 或者steam买了再退款        |\n"
              "|1. 主要：更多现金                                         |\n"
              "|2. 军事：军事征兵(高级后勤可能需要)                     \n"
              "|3. 英雄：英雄授权（猴多力量大可能要）              |\n"
              "|4. 力量：预先准备                            |\n"
              "|4. 支援：可能需要老兵猴训练                         |\n"
              "|英雄需要有：艾迪安                        |\n"
              "|如果不想程序开箱子:                                    |\n"
              "|可以在360或者腾讯管家的网络监控下，禁止气球塔防的网络|\n"
              #   "|或者steam在左上角打开离线模式，再打开游戏|\n"
              )

    elif event == 5:
        variable_list['script_mode'] = '单金收集'
        print('即将进入单金额外奖励搜集模式，请注意是否具备以下条件'
              "| 英雄需要有灵机                                \n"
              "| 知识：要法力盾，更多现金                             \n"
              "|可以在360或者腾讯管家的网络监控下，禁止气球塔防的网络\n"

              )

    elif event == 20:
        variable_list['script_mode'] = '刷金气球'
        print('即将进入刷金气球模式')
        print('将选择英雄萨乌达')

    elif event == 30:
        print('即将进入自选模式，请输入chian名称')
        exec_chains(all_chains[input()])
        sys.exit(0)
    elif event == 21:  # 小猴塔成就
        print("正在完成小猴塔成就")
        click(global_point_map['window_Bottom_right'], times=2)
        click(global_point_map['start'], times=1)
        # click(global_point_map['s3'], times=1)
        click(global_point_map['s1'], times=2)
        # click(global_point_map['map_3'], times=1)
        # click(global_point_map['simple'], times=1)
        # click(global_point_map['standard'], times=1)
        entermap('糖果瀑布', '简单')
        print('请确认之前的存档是否清除')
        time.sleep(2)
        click([1109, 126])
        click([786, 172])
        click([509, 38])
        click([88, 83])
        click([694, 517])
        click([1112, 727])
        click([657, 150])
        click([80, 724])
        key(Key.esc)
        time.sleep(2)
        click(global_point_map['setting_home'], times=1)
        print("小猴塔成就已完成")
        input()

    # else:
    #     pass

    # 在主页继续进入选图页面
    # click(global_point_map['window_Bottom_right'], times=2)#
    click([-1, -1], times=1)
    # click([0, -1], times=1)
    click([1366, 768], times=1)
    click([0, 768], times=1)
    click(global_point_map['start'], times=1)
    exec_times = 0
    fail_times = 0
    simple_times = 0
    # queue_infos['rest']='0'
    while True:
        all_start_time = datetime.now()
        queue_infos['status'] = ''
        queue_infos['mode'] = ''
        queue_infos['insta'] = ''

        # 开始分模式循环运行
        if variable_list['script_mode'] == '刷金气球':
            click(global_point_map['window_Bottom_right'], times=2)  # 不一定要
            click(global_point_map['start'], times=1)  # 不一定要
            selecthero('萨乌达')
            click(global_point_map['s1'], times=1)

            is_find = False
            time.sleep(1)

            # page = None
            page = 0
            # 识别页数
            signal_restart = False  # 是否需要重新执行循环

            for i in range(8):
                # img = pyautogui.screenshot(region=[*origin, 1366, (768)])
                location_gold = pyautogui.locateOnScreen(
                    image=image_path['goldbloon'], confidence=0.60, grayscale=True)

                if not location_gold:
                    # 找不到就下一页, 然后再查找金气球
                    time.sleep(0.5)

                    click(global_point_map['s1'], times=1)
                    time.sleep(3)
                    continue
                page = get_page()
                # 找对应点

                x, y = pyautogui.center(location_gold)

                # 表示在第 i 页找到了额外奖励图标
                # 获取对应的chains

                for m in map_info:

                    if int(map_info[m][0]) == int(page):
                        # 表示在这一页内

                        if map_area[map_info[m][1]][0][0] < (x - origin[0])*1366/variable_list['width'] < map_area[map_info[m][1]][1][0] and map_area[map_info[m][1]][0][1] < (y - origin[1])*1366/variable_list['width'] < map_area[map_info[m][1]][1][1]:

                            variable_list['chain'] = copy.deepcopy(
                                all_chains[m]['中级'][1])
                            click((x, y), no_origin=True)  # 这一步是点击对应的图
                            # 2022-10-19 00:58:13
                            print('[%s]识别到金气球的副本,名称:%s' % (get_datetime(), m))

                            queue_infos['mode'] = 'simple'
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
                    location2 = pyautogui.locateOnScreen(
                        image=image_path['exit_cancel'], confidence=0.8, grayscale=True)
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
                click(global_point_map['s4'], times=2)
                click(global_point_map['map_2'], times=1)
                click(global_point_map['simple'], times=1)
                click(global_point_map['deflation'], times=1)
                variable_list['chain'] = all_chains['黑暗城堡']['放气'][1]

        elif variable_list['script_mode'] == '单金收集':
            click(global_point_map['start'], times=1)
            selecthero('灵机')
            click(global_point_map['s4'], times=1)
            is_find = False
            time.sleep(1)

            # page = None
            page = 0
            # 识别页数
            signal_restart = False  # 是否需要重新执行循环

            for i in range(6):
                img = pyautogui.screenshot(region=[*origin, 1366, (768)])
                location_extra = pyautogui.locateOnScreen(
                    image=image_path['extra'], confidence=0.60, grayscale=True)

                if not location_extra:
                    # 找不到就下一页, 然后再查找额外奖励
                    time.sleep(0.5)
                    click(global_point_map['s4'], times=1)
                    time.sleep(0.5)
                    continue
                # 找对应点
                page = get_page()
                x, y = pyautogui.center(location_extra)

                # 表示在第 i 页找到了额外奖励图标
                # 获取对应的chains

                for m in map_info:

                    if int(map_info[m][0]) == int(page):

                        # 表示在这一页内

                        if map_area[map_info[m][1]][0][0] < (x - origin[0])*1366/variable_list['width'] < map_area[map_info[m][1]][1][0] and map_area[map_info[m][1]][0][1] < (y - origin[1])*1366/variable_list['width'] < map_area[map_info[m][1]][1][1]:

                            variable_list['chain'] = copy.deepcopy(
                                all_chains[m]['简单'][1])

                            # 2022-10-19 00:58:13
                            print('[%s]识别到额外奖励的副本,名称:%s' % (get_datetime(), m))
                            # 避难所的点击顺序不一样,要判断一下
                            click((x, y), no_origin=True)  # 这一步是点击对应的图

                            click(global_point_map['simple'], times=1)
                            click(global_point_map['standard'], times=1)
                            queue_infos['mode'] = 'simple'

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
                    location2 = pyautogui.locateOnScreen(
                        image=image_path['exit_cancel'], confidence=0.8, grayscale=True)
                    if location2:
                        # 点击取消
                        click((550, 510), times=3)

                    signal_restart = True
                    break

            if signal_restart:
                # 下一轮循环重新选择
                continue

            if not is_find:
                # 需要改进，把点击进入地图的部分写入字典的值中
                # 没找到就重来吧, 刷暗堡去
                print('[%s] 没有找到额外奖励图标,返回刷暗黑城堡动作' % get_datetime())
                key(Key.esc, times=4)
                time.sleep(1)
                click(global_point_map['start'], times=1)
                click(global_point_map['s3'], times=1)
                click(global_point_map['s4'], times=2)
                click(global_point_map['map_2'], times=1)
                click(global_point_map['simple'], times=1)
                click(global_point_map['deflation'], times=1)
                variable_list['chain'] = all_chains['黑暗城堡']['放气'][1]
                

        elif variable_list['script_mode'] == '双金收集':
            click(global_point_map['start'], times=1)
            selecthero('艾蒂安')
            click(global_point_map['s4'], times=1)
            is_find = False
            time.sleep(1)

            # page = None
            page = 0
            # 识别页数
            signal_restart = False  # 是否需要重新执行循环
            for i in range(6):
                location_extra = pyautogui.locateOnScreen(
                    image=image_path['extra'], confidence=0.60, grayscale=True)

                if not location_extra:
                    # 找不到就下一页, 然后再查找额外奖励
                    time.sleep(0.5)
                    click(global_point_map['s4'], times=1)
                    time.sleep(3)
                    continue
                # else:
                #     print('识别到额外奖励')
                page = get_page()

                x, y = pyautogui.center(location_extra)

                for m in map_info:

                    if int(map_info[m][0]) == int(page):
                        # 表示在这一页内

                        if map_area[map_info[m][1]][0][0] < (x - origin[0])*1366/variable_list['width'] < map_area[map_info[m][1]][1][0] and map_area[map_info[m][1]][0][1] < (y - origin[1])*1366/variable_list['width'] < map_area[map_info[m][1]][1][1]:

                            # 2022-10-19 00:58:13
                            print('[%s]识别到额外奖励的副本,名称:%s' % (get_datetime(), m))
                            # 避难所的点击顺序不一样,要判断一下
                            click((x, y), no_origin=True)  # 这一步是点击对应的图

                            # if m == '避难所':
                            #     variable_list['chain']= copy.deepcopy(all_chains[m]['简单'][1])
                            #     click(global_point_map['simple'], times=1)
                            #     click(global_point_map['standard'], times=1)
                            #     queue_infos['mode'] ='simple'

                            # else:
                            variable_list['chain'] = copy.deepcopy(
                                all_chains[m]['极难'][1])
                            queue_infos['mode'] = 'imp'
                            click(global_point_map['difficulty'], times=1)
                            click(global_point_map['imp'], times=1)

                            # 之后就能进到对应的图了
                            is_find = True
                            break

                if is_find:
                    break

                # 一般不会,如果30次还没找到就Esc 退出到主页面从来
                # 可以加一个长时间不执行动作是 执行“重开”游戏和脚本 利用key.esc，和失败点击esc时出现的内容，来防止死循环
                if i > 10:
                    key(Key.esc, times=12)
                    location2 = pyautogui.locateOnScreen(
                        image=image_path['exit_cancel'],     confidence=0.8, grayscale=True)
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
                click(global_point_map['start'], times=1)
                click(global_point_map['s3'], times=1)
                click(global_point_map['s4'], times=1)
                click(global_point_map['s4'], times=1)
                click(global_point_map['map_2'], times=1)
                click(global_point_map['simple'], times=1)
                click(global_point_map['deflation'], times=1)
                variable_list['chain'] = all_chains['黑暗城堡']['放气'][1]

        else:
            if event == 0:
                cricle_onemap(needmap, needmode)
            elif event == -1:
                pass
            elif event == 1:
                cricle_onemap('黑暗城堡', '放气')
            elif event == 2:
                cricle_onemap('黑暗城堡', '点击')
            elif event == 3:
                cricle_onemap('炼狱', '极难')
            else:
                cricle_onemap('黑暗城堡', '放气')

        # time.sleep(1)
        # if variable_list['chain']!='':
        #     chains=variable_list['chain']
        # 到这里应该是进入到对应图了

        try:
            location = pyautogui.locateOnScreen(
                image=image_path['cover'], confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]识别到覆盖存档确认框,点击' % get_datetime())
            time.sleep(1)
            click(global_point_map['cover'])

        except Exception as e:
            pass
            # 到这里应该是进入到对应图了
        # if variable_list['restart']!='1':#第一次跑执行以下操作
        #     time.sleep(4)
        #     click(global_point_map['yes1'], times=1)
        #     # time.sleep(1)

        # 开始执行chains
        # try:
        #     queue_infos['thread_exec'].raise_exception()
        # except Exception as e:
        #     pass

        # try:
        #     queue_infos['thread_monitor'].raise_exception()
        # except Exception as e:
        #     pass

        # queue_infos['status'] = ''  # 再初始化, 虽然没啥意义
        # queue_infos['thread_exec'] = thread_with_exception(exec_chains,
        #                                                    (variable_list['chain'],
        #                                                     queue_infos),
        #                                                    'thread_exec',
        #                                                    True)

        # queue_infos['thread_exec'].start()

        # queue_infos['thread_monitor'] = thread_with_exception(monitor,
        #                                                       (queue_infos,),
        #                                                       'thread_monitor',
        #                                                       True)
        # queue_infos['thread_monitor'].start()
        run_thread(exec_chains,(variable_list['chain'],queue_infos),'thread_exec',True)
        run_thread(monitor,(queue_infos,),'thread_monitor',True)
        while True:  # 线程都开出去了,这里要阻塞后续进程
            time.sleep(3)  # 3秒一次影响也不大, 别让CPU太累
            if queue_infos.get('status', '') in ['success', 'fail']:
                end_thread(abilities)
                end_thread(cricle_ability)#以后遍历执行终止game_thread
                end_thread(monitor)
                end_thread(exec_chains)
                # try:  # 终止监视线程
                #     thread = queue_infos.get('thread_monitor', '')
                #     if thread != '':
                #         thread.raise_exception()
                        

                #     # else:
                #     #     print('游戏结束')

                # except Exception as e:
                #     print('[%s]终结线程失败,%s' % (get_datetime(), e))
                #     pass
                break

        # 到此就完成了一轮操作

        # start 活动 识别方案
        if variable_list['script_mode'] == '双金收集' or variable_list['script_mode'] == '单金收集':
            collect_chain()

        exec_times += 1
        if queue_infos['status'] == 'fail':  # 监测失败次数
            fail_times += 1
        if queue_infos['mode'] == 'simple':  # 监测放气次数
            simple_times += 1
        end_time = datetime.now()

        print('[%s]已进行%2d轮, 耗时: %s秒, 本轮开始时间: %s' % (
            get_datetime(),
            exec_times,
            int((end_time - all_start_time).total_seconds()),
            datetime.strftime(all_start_time, '%Y-%m-%d %H:%M:%S'),
        )
        )
        if variable_list['script_mode'] == '双金收集' or variable_list['script_mode'] == '单金收集':
            print("[%s]获得的5阶insta数量为:%s个" %
                  (get_datetime(), variable_list['5阶insta数']))
        print('[%s]累计失败次数: %s' % (get_datetime(), fail_times))
        # time.sleep(2)
        # click(global_point_map['window_Bottom_right'])#此时完全进入主页
        variable_list['restart'] = '1'  # 用于给循环单图判断过了一次图

# end 函数区


queue_infos = dict()


if __name__ == '__main__':

    # 闭环测试 识别流程
    exec_imp_chain()
