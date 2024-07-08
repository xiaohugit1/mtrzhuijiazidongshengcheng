import os
import string
print("Because of the characteristics of Python, please ensure that the folder is empty.")
zhuwengjianjia=input("Please enter the main folder location:")
liechezuijia=input("Please enter the main folder location.")
shengyingzuijia=input("To customize train addition, please press 1; if not, please press 2:")
print("It is being generated.")
if(liechezuijia=='1'and shengyingzuijia == '1'):
    os.makedirs(zhuwengjianjia + '/assets' + '/mtr' + './custom_directory')
    tmp=zhuwengjianjia+'\\assets' + '\\mtr'
    os.mkdir(tmp + './sounds')
elif (liechezuijia == '1'):
    os.makedirs(zhuwengjianjia + './assets' + './mtr' + './custom_directory')
elif (shengyingzuijia == '1'):
    os.makedirs(zhuwengjianjia + './assets' + './mtr' + './sounds')
print("The main folder has been successfully created.")
print("The subsidiary files are about to start generating.")
file=open(zhuwengjianjia+'pack.mcmeta','w+')
file.close()