#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/4 11:38 
# @Author : virus 
# @File : 3-1.py 
# @Desp : python


x = 0
a = []

while x >= 0:
    x = int(input("请输入整数"))
    a.append(x)
    print(sorted(a,reverse=True))
