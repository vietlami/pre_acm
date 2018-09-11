#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/4 11:38 
# @Author : virus 
# @File : 3-1.py 
# @Desp : python


# 逆序输出

x = 0
a = []

while x >= 0:
    x = int(input("请输入整数"))
    if a == []:
        a.append(x)
        print(a)
        continue
    # print(sorted(a,reverse=True))

    for i in a:
        print(x)
        print(i)
        if x >= i:
            index = a.index(i)
            a.insert(index, x)
            print(a)
            break
        else:
            if a[-1] == i:
                a.append(x)
                print(a)
                break
            else:
                continue
