#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/29 15:48 
# @Author : virus 
# @File : 1-5.py
# @Desp : python


import math

# 圆柱体的表面积
# area = 2*math.pi*r(r+h)

r = float(input("请输入圆柱体的半径："))
h = float(input("请输入圆柱体的高："))

print("%f" % (2*math.pi*r*(r+h)))