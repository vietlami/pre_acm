#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/30 11:45 
# @Author : virus 
# @File : 1-5.py 
# @Desp : python

# 打折

price = 95

n = int(input("请输入购买衣服件数"))
pay_cash = n * 95

if n * 95 >= 300:
    print("需要支付的金额%.2f"%float(pay_cash*0.85))
else:
    print("需要支付的金额%.2f"%pay_cash)