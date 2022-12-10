
import pyautogui
import os
# 定义函数 start_game，用于查找并点击图像
def start_game(image_files):
    # 获取当前工作目录
    current_dir = os.getcwd()
    # 循环查找图像
    loop_counter = 0
    while True:
        # 初始化标志变量
        found_all = True
        # 循环查找图像
        for image_file in image_files:
            # 获取图像文件的绝对路径
            image_path = os.path.join(current_dir, image_file)
            # 使用 locateOnScreen 函数查找图像
            position = pyautogui.locateOnScreen(image_path)
            # 如果找到了图像，点击图像
            if position is not None:
                pyautogui.click(position) 
                print("ok,game ready")
            else:
                # 如果没找到图像，标志变量置为 False
                found_all = False
        # 如果找到了所有图像，退出循环
        if found_all:
            break
        # 如果计数器达到了预定值，退出循环
        if loop_counter >= 30:
            print("ok,done")
            break
           
        # 增加计数器的值
        loop_counter += 1

# 指定图片文件的相对路径
image_files = ["D:\\pytthon_work\\image\\kaishiyouxi.jpg", 
               "D:\\pytthon_work\\image\\congtoukaishi.jpg",
               "D:\\pytthon_work\\image\\huzi.png",
               "D:\\pytthon_work\\image\\ailisi.png",
               "D:\\pytthon_work\\image\\xiagou.png",
               "D:\\pytthon_work\\image\\kaishi.png",
               "D:\\pytthon_work\\image\\ailisi_1.png",
               "D:\\pytthon_work\\image\\huzi_1.png",
               "D:\\pytthon_work\\image\\xiagou_1.png",
               "D:\\pytthon_work\\image\\buff.png",
               "D:\\pytthon_work\\image\\queding.png",
               "D:\\pytthon_work\\image\\next.png"
               ]
# 调用 start_game 函数
start_game(image_files)













