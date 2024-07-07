import os
import string
print("因为python的特性，请保证文件夹是空的")
zhuwengjianjia=input("请输入主文件夹位置:")
liechezuijia=input("要自定义列车追加请按1，不要请按2:")
shengyingzuijia=input("要自定义列车追加请按1，不要请按2:")
print("正在生成中")
if(liechezuijia=='1'and shengyingzuijia == '1'):
    os.makedirs(zhuwengjianjia + '/assets' + '/mtr' + './custom_directory')
    tmp=zhuwengjianjia+'\\assets' + '\\mtr'
    os.mkdir(tmp + './sounds')
elif (liechezuijia == '1'):
    os.makedirs(zhuwengjianjia + './assets' + './mtr' + './custom_directory')
elif (shengyingzuijia == '1'):
    os.makedirs(zhuwengjianjia + './assets' + './mtr' + './sounds')
print("主文件夹已经生成完成")
print("附属文件即将开始生成")
file=open(zhuwengjianjia+'pack.txt','w+')
file.close()