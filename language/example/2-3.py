#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 15:19 
# @Author : virus 
# @File : 2-2.py 
# @Desp : python

# 输出所有形如aabb的4位完全平方数 7744问题（2）
import math

i = 1
while i > 0:
    n = i * i
    i += 1
    if n > 9999:
        break
    if n > 1000:
        hi = int(n/100)
        lo = int(n%100)
        if (int(hi / 10) == hi % 10) & (int(lo / 10) == lo % 10):
            print(n)
        else:
            continue

