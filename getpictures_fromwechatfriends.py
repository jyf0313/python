# 导入网页版微信模块
import itchat
# 导入系统模块
import os
# 导入数学模块
import math
# 导入图像处理模块
from PIL import Image
# 判断是否存在文件夹img，如果不存在就创建img
if not os.path.exists('F:\\python\\微信头像拼接\\img'):
    os.mkdir('F:\\python\\微信头像拼接\\img')
# 登陆网页版微信，hotReload可以登陆5分钟
itchat.auto_login(hotReload = True)
# 获取所有好友信息, 返回的是一个生成器
friends = itchat.get_friends()
# 打印一下，调试用
# print(friends)
num = 0
# 生成器需要用for循环遍历
for friend in friends:
    # 打印friend，调试用，是一个dict
    # print(friend)
    # 获取好友头像
    img = itchat.get_head_img(userName = friend['UserName'])
    with open('F:\\python\\微信头像拼接\\img'+'\\'+str(num)+'.png', 'wb') as f:
        f.write(img)
    num += 1
# 确定有多少张图片，遍历img文件夹里的图片，返回的是list
images = os.listdir('F:\\python\\微信头像拼接\\img')
# 打印一下，发现是list，里面的元素是每个图片的名称
# print(images)
# list的元素多少，就是图片的多少
print(len(images))
# 设定总的图片大小是640*640，计算每张图片的长和宽
each_size = int(math.sqrt((640*640)/len(images)))
print(each_size)
# 每行可以容纳的头像个数
lines = int(640/each_size)
# 创建空白图片
image = Image.new('RGBA', (640, 640))
x = 0
y = 0
# 一张一张粘贴
for i in range(0, len(images)):
    img = Image.open('F:\\python\\微信头像拼接\\img'+'\\'+str(i)+'.png')
    # 缩放头像尺寸，由于缩小，品质要设置为高
    img_setting = img.resize((each_size, each_size), Image.ANTIALIAS)
    # 粘贴这张图片img到image
    image.paste(img_setting, (x*each_size, y*each_size))
    # 粘贴下一张
    x += 1
    # 判断一行粘贴满了
    if x == lines:
        # x重置
        x = 0
        # 换一行
        y += 1
image.save('F:\\python\\微信头像拼接\\img'+'/'+'all.png')




    
