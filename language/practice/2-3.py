#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/3 16:25 
# @Author : virus 
# @File : 2-3.py 
# @Desp : python

n = int(input("请输入一个正整数"))
s = 2*n-1
print(s*"#")
i = 1
while n > 0:
    print(i*" " + (s-2*i)*"#" + i* " ")
    i +=1
    n -=1
