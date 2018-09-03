#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/3 15:47 
# @Author : virus 
# @File : 2-1.py 
# @Desp : python


#  水仙花数
n = 100

while n < 1000:
    # print(n)
    if n == int(n/100)*int(n/100)*int(n/100) + int(n%100/10)*int(n%100/10)*int(n%100/10) + int(n%10)*int(n%10)*int(n%10):
        print(n)
    n +=1