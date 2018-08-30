#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 11:09 
# @Author : virus 
# @File : 1-3.py 
# @Desp : python

# 连续求和

n = int(input("请输入一个正整数"))

sum = 0
i = 1
while n >= i:
    sum = sum + i
    i += 1

print("1 到 %d 之和为：%d" % (n,sum))


sum1 = 0
i1 = 1

for i in range(1, n+1):
    sum1 = sum1 + i1
    i1 += 1

print("1 到 %d 之和为：%d" % (n,sum1))