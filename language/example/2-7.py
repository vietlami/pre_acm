#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 16:50 
# @Author : virus 
# @File : 2-7.py 
# @Desp : python

# 阶乘之和

sum = 0

n = int(input("请输入正整数\n"))

for i in range(1,n+1):
    # print(i)
    its = 1
    for j in range(1,i+1):
        its *= j
    sum += its
print("%d"%(sum % 1000000))