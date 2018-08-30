#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 16:17 
# @Author : virus 
# @File : 2-6.py 
# @Desp : python


# 近似计算
sum = 0
i = 1

while i > 0:
    term = 11.0/(2*i+1)
    if term < 0.000001:
        print(i)
        break
    if i%2 == 0 :
        sum += term
    else:
        sum -= term
    i += 1

print(sum)