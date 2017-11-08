# -*- coding: UTF-8 -*-
#水仙花数：153=1*1*1+5*5*5+3*3*3
#输入位数,比如6
#n = 6
#548834

def power(n,m):
  r = 1
  for i in range(m):
    r *=n
  return r

def number(n):
  if n <= 0:
    print 'error: n must positive number and greator then 0.'
    return
  # 1: 0-9
  # 2: 10-99
  # 3: 100-999
  l = 0
  u = 0
  if n == 1:
    l = 0
    u = 9
  else:
    l = 1
    u = 10
    for i in range(n-1):
      l *=10
      u *=10
    u -=1
  for i in range(l,u+1):
    k = str(i)
    o = len(k)
    p = 0
    for x in k:
      x = int(x)
      p +=power(x,n)
    if i == p:
      print i
number(input('n = '))
'''
for i in range(1,6+1):
  number(i)
  print '---------------------'
'''
