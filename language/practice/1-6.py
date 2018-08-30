#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 11:50 
# @Author : virus 
# @File : 1-6.py 
# @Desp : python

# 三角形

a = int(input("请输入第一条边的长度\n"))
b = int(input("请输入第二条边的长度\n"))
c = int(input("请输入第三条边的长度\n"))

if (a + b >= c) & (a + c >= b) & (c + b >= a):
    print("1")
    if (a*a + b*b == c*c) | (a*a + c*c == b*b) | ( b*b + c*c == a*a):
        print("2")
        print("yes")
    else:
        print("no")
else:
    print("not a triangle")