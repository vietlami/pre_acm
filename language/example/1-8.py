#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/29 16:12 
# @Author : virus 
# @File : 1-8.py
# @Desp : python

# 变量交换（1）

a = int(input("请输入a\n"))
b = int(input("请输入b\n"))

t = a
a = b
b = t

print("a等于%s\nb等于%s"%(a,b))