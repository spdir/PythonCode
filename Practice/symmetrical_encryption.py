# -*- coding: UTF-8 -*-
#对称加密
def crypt(s,p):
  r = ''
  for i in s:
    for j in p:
      i = chr(ord(i)^ord(j))
    r +=i
  return r
def output(s):
  for i in s:
    print '0x%X' %(ord(i)),
 
s = 'hello, world!'
p = '12345'
print s,p
r = crypt(s,p)
output(r)
r = crypt(r,p)
output(r)

