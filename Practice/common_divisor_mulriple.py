# -*- coding: UTF-8 -*-
#输入一个非0的整数，计算最大公约数和最小公倍数
n = input('n = ')
m = input('m = ')

def gy(m,n):
  t = m
  if t > n:
    t = n
  for i in range(t,1-1,-1):
    if m % i == 0 and n % i == 0:
      return i

def gb(m,n):
  t = m
  if t < n:
    t = n
  for i in range(t, m*n+1):
    if i % m == 0 and i % n ==0:
      return i
print 'GY:(%d,%d):%d' %(m,n,gy(m,n))
print 'GB:(%d,%d):%d' %(m,n,gb(m,n))
