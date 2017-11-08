# -*- coding: UTF-8 -*-
#讲一个数字转换位二进制，并将对应的位数修改为1或者0
def setbit(n,m):  #1
  n |= (1<<(m-1))
  return n

def unsetbit(n,m):  #0
  n &= ~(1<<(m-1))
  return n

n = 7

print '23 --> ',setbit(n,5)
print ' 3 --> ',unsetbit(n,3)
print '19 --> ',setbit(unsetbit(n,3),5)
print '19 --> ',unsetbit(setbit(n,5),3)