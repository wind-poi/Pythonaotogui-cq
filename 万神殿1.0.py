
import pyautogui
import os

def start_game(image_files):

    current_dir = os.getcwd()

    loop_counter = 0
    while True:
  
        found_all = True

        for image_file in image_files:

            image_path = os.path.join(current_dir, image_file)

            position = pyautogui.locateOnScreen(image_path)

            if position is not None:
                pyautogui.click(position) 
                print("ok,game ready")
            else:

                found_all = False

        if found_all:
            break

        if loop_counter >= 30:
            print("ok,done")
            break
           

        loop_counter += 1

# 指定图片文件的绝对路径  下面这些是例子
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

start_game(image_files)













