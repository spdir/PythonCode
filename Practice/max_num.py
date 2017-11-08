# -*- coding: UTF-8 -*-
#从键盘获取三个数字，打印输出最大的那个数字

n1 = input('n1 = ')
n2 = input('n2 = ')
n3 = input('n3 = ')

m = n1

if m < n2:
    m = n2

if m < n3:
    m = n3

print m