#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 15:58 
# @Author : virus 
# @File : 2-4.py 
# @Desp : python

# 3n+1问题

n = int(input("请输入任意大于1的自然数\n"))
count = 0
while n > 1:
    if n % 2 == 1:
        n = 3*n + 1
    else:
        n = n/2
    count +=1

print("变换的次数%d"%count)