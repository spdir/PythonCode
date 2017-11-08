# -*- coding: UTF-8 -*-
#斐波那契额
def fib(max):
  n,a,b = 0,0,1
  while max > n:
    a,b = b ,a+b
    print b
    n +=1

fib(100)
