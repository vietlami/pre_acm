#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2018/8/29 17:20 
# @Author : virus 
# @File : 1-12.py 
# @Desp : python


# 三整数排序
a = int(input("请输入第一个数"))
b = int(input("请输入第二个数"))
c = int(input("请输入第三个数"))

if a > b:
    t = a
    a = b
    b = t
if a > c:
    t = a
    a = c
    c = t
if b > c:
    t = b
    b = c
    c = t

print("%d < %d < %d"%(a,b,c))