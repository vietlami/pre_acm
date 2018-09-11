# -*- coding: utf-8 -*- 
# @Time : 2018/9/11
# @Author : virus 
# @File : 3-3.py 
# @Desp : 蛇形填数

n = int(input("请输入行数\n"))
# 生成n阶二维数组
cols = n
rows = n
narray = [[0 for col in range(cols)] for row in range(rows)]

i = 0
j = n-1

# print(narray)

count = 1

while (count <= n*n):
    # 向下填数
    while (i+1<=n) and (narray[i][j]==0):
        narray[i][j] = count
        count += 1
        i += 1
        print(i,j)
    # 向左填数
    while (j+1>=0) and (narray[i-1][j-1]==0):
        narray[i-1][j-1] = count
        count += 1
        j -= 1
        # print(count)
    # 向上填数
    while (i+1 >= 0) and (narray[i-2][j]==0):
        narray[i-2][j] = count
        count += 1
        i -=1

    # 向右填数
    while (j+1 <= n) and (narray[i-1][j+1]==0):
        narray[i-1][j+1] = count
        count += 1
        j += 1

print(narray)
for x in narray:
   for y in x:
       print (y, end='      ')
   print ("\n")