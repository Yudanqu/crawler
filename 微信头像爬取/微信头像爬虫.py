from numpy import *
import itchat
import PIL.Image as Image
from os import listdir

def get_imgs():
    itchat.auto_login(hotReload=True) # 登录微信
    friends = itchat.get_friends(update=True)[0:325] # 获取好友数量
    num = 0
    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"]) # 获取头像
        fileImage = open( "F:/python案例/new/" + str(num) + ".jpg",'wb') # 命名
        fileImage.write(img)
        fileImage.close()
        num += 1 # 计数，递增命名
def get_big_img():
    pics = listdir("F:/python案例/new/")
    numPic = len(pics)
    print(numPic)
    toImage = Image.new("RGB", (450, 450)) # 创建450*450px的大图
    x = 0
    y = 0
    for i in pics:
        try:
            img = Image.open("F:/python案例/new/{}".format(i))
        except IOError:
            print("Error: 没有找到文件或读取文件失败",i)
        else:
            img = img.resize((30, 30), Image.ANTIALIAS) # 拼接的每个头像调整尺寸为30*30px
            toImage.paste(img, (x * 30, y * 30)) # 粘贴位置
            x += 1
            if x == 15: # 达到15个图片换行
                x = 0
                y += 1
    toImage.save("F:/python案例/new/" +"touxiang.jpg") # 保存大图
    itchat.send_image("F:/python案例/new/" +"touxiang.jpg", 'filehelper') # 自动发送给文件传输助手

get_imgs()
get_big_img()