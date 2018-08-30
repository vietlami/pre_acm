#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 11:31 
# @Author : virus 
# @File : 1-4.py 
# @Desp : python

# 正弦和余弦

import math

n = int(input("请输入正整数\n"))
x = n * math.pi/180
sin = math.sin(x)
cos = math.cos(x)

print("%d的正弦为%f"%(n,sin))
print("%d的余弦为%f"%(n,cos))

