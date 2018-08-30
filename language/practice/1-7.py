#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 15:04 
# @Author : virus 
# @File : 1-7.py 
# @Desp : python

# 年份
year = int(input("请输入年份\n"))

if (year%4 == 0) & (year%100 != 0):
    print("yes")
else:
    if year%400==0:
        print("yes")
    else:
        print("no")

