# -*- coding: UTF-8 -*-
#从键盘输入一个四位数字，然后分别输出每个位置的数字
num = input('input four digit number: ')

q = num % 10000 / 1000
b = num % 1000 / 100
s = num % 100 / 10
g = num % 10 / 1

print 'G:%d S:%d B:%d Q:%d' %(q,b,s,g)

'''
input four digit number: 1234
G:1 S:2 B:3 Q:4
'''