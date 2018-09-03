#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/3 17:40 
# @Author : virus 
# @File : 2-6.py 
# @Desp : python

# 排列 c33 a33

a = [1,2,3,4,5,6,7,8,9]
res_a = a[:]
while len(a) == 9:
    a1 = res_a[0:3]
    a2 = res_a[3:6]
    a3 = res_a[6:9]
    res_a1 = a1[:]
    res_a2 = a2[:]
    res_a3 = a3[:]
    i1 = 0
    i2 = 0
    i3 = 0
    while len(a1) == 3:
        i1 = res_a1[0]*100 + res_a1[1]*10 + res_a1[2]
        a1_p = res_a1.pop(2)
        res_a1.insert(0,a1_p)
        while len(a2) == 3:
            i2 = res_a2[0] * 100 + res_a2[1] * 10 + res_a2[2]
            a2_p = res_a2.pop(2)
            res_a2.insert(0, a2_p)
            while len(a3) == 3:
                i3 = res_a3[0] * 100 + res_a3[1] * 10 + res_a3[2]
                print(i1,i2,i3)
                if (i2 == 2 * i1) & (i3 == 3 * i1):
                    print("%d %d %d" % (i1, i2, i3))
                a3_p = res_a3.pop(2)
                res_a3.insert(0, a3_p)
                if res_a3 == a3:
                    break
            if res_a2 == a2:
                break
        if res_a1 == a1:
            break

    a_p = res_a.pop(8)
    res_a.insert(0,a_p)
    if (res_a == a):
        break