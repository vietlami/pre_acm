#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 15:19 
# @Author : virus 
# @File : 2-2.py 
# @Desp : python

# 输出所有形如aabb的4位完全平方数 7744问题（1）
import math

for i in range(1,10):
    for j in range(1,10):
        n = i*1100 + j*11
        m = math.floor(math.sqrt(n))
        if m*m == n:
            print(n)
