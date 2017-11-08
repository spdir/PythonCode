# -*- coding: UTF-8 -*-
#打印一个菱形
n = input('n = ')
j = 0
for i in range(1,n+1,2):
  print  ' '*(n/2 -j) + '*'*i,
  j +=1
  print
j -=1
for k in range(n-2,0,-2):
  j -=1
  print ' '*(n/2 - j) + '*'*k,
  print
