#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/3 16:37 
# @Author : virus 
# @File : 2-4.py 
# @Desp : python

# 子序列的和

m = int(input("请输入正整数"))
n = int(input("请输入第二个正整数"))

t = m
if m > n:
    m = n
    n = t

i = m
s = 0
while i <= n:
    s += float(1)/(i*i)
    i +=1

print("%.5f"%s)

print("n = m = 0")