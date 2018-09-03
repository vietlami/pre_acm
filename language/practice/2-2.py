#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/3 15:58 
# @Author : virus 
# @File : 2-2.py 
# @Desp : python

a = int(input("请输入三人一排余数"))
b = int(input("请输入五人一排余数"))
c = int(input("请输入七人一排余数"))

m = 70*a + 21*b + 15*c
while m > 105:
    m -= 105
if (m > 100) | (m < 10):
    print("no answer")
else:
    print("%d"%m)
