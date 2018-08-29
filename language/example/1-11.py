#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2018/8/29 16:22 
# @Author : virus 
# @File : 1-11.py 
# @Desp : python


# 鸡兔同笼

n = int(input("请输入总数量\n"))
m = int(input("请输入总腿数\n"))

a = (4*n-m)/2
b = n-a

if m % 2 == 1 or int(a) < 0 or int(b) < 0:
    print("No answer")
else:
    print("鸡的数量为%s" % (int(a)))
    print("兔的数量为%s" % (int(b)))
