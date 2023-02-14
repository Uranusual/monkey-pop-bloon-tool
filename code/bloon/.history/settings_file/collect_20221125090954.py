from .autogame import *

def collect_chain():
    # start 活动 识别方案

    queue_infos[''] == ''
    print('[%s]活动阶段代码开始执行' % get_datetime())
    time.sleep(8)
    for i in range(1000):
        # # 刚返回的时候, 在主页面的, 要稍等一会才加载活动页面, 不用了上面有睡眠
        
        if i > 15:
            click(global_point_map['home_empty4'], times=2, cd=2)

        try:
            location = pyautogui.locateOnScreen(image=path_collected,confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            time.sleep(2)
            print('[%s]识别到开始, 奖励搜集完毕' % get_datetime())
            click(global_point_map['return'], times=1)
            break
        except Exception as e:
            pass


        try:
            location = pyautogui.locateOnScreen(image=path_instawanted, confidence=0.8, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]识别想开的猴子，点击该insta' % get_datetime())
            click((x, y), cd=1, no_origin=True)
            time.sleep(1)
            continue
        except Exception as e:
            pass


        try:
            location_button = pyautogui.locateOnScreen(image=path_collection_button, confidence=0.8, grayscale=True)
            if location_button:
                print('[%s]识别到搜集按钮, 继续开箱子' % get_datetime())
                click(global_point_map['collection'], times=1, cd=1)
                time.sleep(2)
                continue
        except Exception as e:
            pass

        try:
            location = pyautogui.locateOnScreen(image=path_social, confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]识别到开局页面,退出盲盒点击阶段' % get_datetime())
            break
        except Exception as e:
            pass
        
        try:
            location = pyautogui.locateOnScreen(image=path_social_full, confidence=0.85, grayscale=True)
            x, y = pyautogui.center(location)
            print('[%s]识别到开局页面的整体猴子图标,退出盲盒点击阶段' % get_datetime())
            break
        except Exception as e:
            pass
        

        

        
        try:
            location = pyautogui.locateOnScreen(image=path_blue, confidence=0.8, grayscale=True)
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
            location4 = pyautogui.locateOnScreen(image=path_insta_4, confidence=0.8, grayscale=True)
            # if location4:
            #     need_save = True
            
            # 识别五阶
            location5 = pyautogui.locateOnScreen(image=path_insta_5, confidence=0.8, grayscale=True)
            if location5:
                a = 5
                need_save = True
                
            
            if need_save:
                # 目前失效，需要改改
                print("恭喜你获得一个5阶insta，可以在image/insta中查看")
                im = pyautogui.screenshot(region=[*origin,1366, 768])
                
                img_path = 'images/insta'
                # 路径不存在时创建
                if not os.path.exists(img_path):
                    os.makedirs(img_path)
                t = get_datetime()
                t = t.replace(':', '_')
                t = t.replace('-', '_')
                
                im.save('%s/%s %s阶.png' % (img_path, t, str(a)))
            
            # 点击第二次确认, 回到开箱页面继续开箱, 多点击几次,最后一次能回到活动页面
            click((x, y), times=2, cd=1, no_origin=True)
            time.sleep(2)
            
            # 不用break, 识别到一个点一个, 直到点完之后到活动主页面, 识别到主页面就退出循环了
        
        except Exception as e:
            pass

    print('[%s]活动阶段代码执行完毕' % get_datetime())

    # end 活动 识别方案