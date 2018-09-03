#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2018/9/3 15:31 
# @Author : virus 
# @File : 2-9.py 
# @Desp : python

n = 0
min = 0
max = 0
s = 0

while n >= 0:
    x = int(input("请输入正整数\n"))
    s += x
    if x < min:
        min = x
    if x > max:
        max = x
    if n == 0:
        min = x
    n += 1

    print("%d %d %.3f\n"%(min,max,float(s)/n))