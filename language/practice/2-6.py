#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/9/3 17:40 
# @Author : virus 
# @File : 2-6.py 
# @Desp : python

# 排列 c33 a33

a = [1,2,3,4,5,6,7,8,9]


for i in range(0,9):
    res_a1 = a[:]
    i1 = res_a1[i]
    res_a1.pop(i)
    for j in range(0,8):
        res_a2 = res_a1[:]
        i2 = res_a2[j]
        res_a2.pop(j)
        for k in range(0,7):
            res_a3 = res_a2[:]
            i3 = res_a3[k]
            res_a3.pop(k)
            for l in range(0,6):
                res_a4 = res_a3[:]
                i4 = res_a4[l]
                res_a4.pop(l)
                for m in range(0,5):
                    res_a5 =  res_a4[:]
                    i5 = res_a5[m]
                    res_a5.pop(m)
                    for n in range(0,4):
                        res_a6 = res_a5[:]
                        i6 = res_a6[n]
                        res_a6.pop(n)
                        for o in range(0,3):
                            res_a7 = res_a6[:]
                            i7 = res_a7[o]
                            res_a7.pop(o)
                            for p in range(0,2):
                                res_a8 = res_a7[:]
                                i8 = res_a8[p]
                                res_a8.pop(p)
                                i9 = res_a8[0]
                                # print(i1,i2,i3,i4,i5,i6,i7,i8,i9)
                                item1 = i1*100 + i2*10 + i3
                                item2 = i4*100 + i5*10 + i6
                                item3 = i7*100 + i8*10 + i9
                                if (item2== 2*item1)&(item3 == 3*item1):
                                    print("%d %d %d"%(item1,item2,item3))



