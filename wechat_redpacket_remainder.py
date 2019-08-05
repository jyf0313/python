# 导入微信模块
import itchat
# 导入gui模块
from tkinter import messagebox
# 导入pygame模块
import pygame
# 导入time模块
import time
# 导入os模块
import os

# 自动登录，hotReload='True'表示长时间登录，5分钟左右，登陆的是网页版微信
itchat.auto_login(hotReload=True)

# 定义一个提醒弹窗，用到tkinter模块
def box_pop():
    messagebox.showinfo(title='红包提醒', message='快抢红包')

# 定义一个声音弹窗提醒，用到pygame模块
def voice_pop():
        # 设置一个界面
        pygame.display.set_mode((300, 300))
        # 初始化
        pygame.mixer.init()
        # 加载音乐
        pygame.mixer_music.load('audio.mp3')
        # 播放，pygame播放音乐会失真
        pygame.mixer_music.play()
        # 播放5秒
        time.sleep(5)
        # 停止播放
        pygame.mixer_music.stop()

# 定义函数播放音乐，用os模块打开播放
def voice_play():
        os.system('audio.mp3')

# 接收所有好友信息，用一个装饰器来表示，收到的信息保存在'Note'内
itchat.msg_register('NOTE', isGroupChat=False)
def get_messages(note):
    print(note)
    if '收到红包' in note['TEXT']:
        print('快抢红包')
        # 下面三种提醒，可以随意一种使用
        box_pop()
        voice_pop()
        voice_play()

    
itchat.run()


