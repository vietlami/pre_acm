# -*- coding: utf-8 -*- 
# @Time : 2018/9/11
# @Author : virus 
# @File : 3-2.py 
# @Desp : 开灯问题


n = int(input("请输入灯数量\n"))

n2 = []
n3 = []
nn = []

for i in range(1,n+1):
    if i%2 == 0:
        n2.append(i)
        continue
    elif i%3 == 0:
        n3.append(i)
        continue
    else:
        nn.append(i)
        continue


print("被第二个人关掉的灯编号有%s"%n2)
print("被第三个人关掉的灯编号有%s"%n3)
print("没有关掉的灯编号有%s"%nn)