#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/29 15:57 
# @Author : virus 
# @File : 1-6.py 
# @Desp : python


# 三位数反转

n  = int(input("请输入一个三位数\n"))

print("%d%d%d\n"%(n%10,int(n/10%10),n/100))