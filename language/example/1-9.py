#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/29 16:17 
# @Author : virus 
# @File : 1-9.py 
# @Desp : python

# 变量交换（2）

a = int(input("请输入a\n"))
b = int(input("请输入b\n"))

a = a + b
b = a - b
a = a - b

print("a等于%s\nb等于%s"%(a,b))