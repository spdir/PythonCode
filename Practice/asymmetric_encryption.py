# -*- coding: UTF-8 -*-
#非对称加密
pubilc_key = 'abcde'
private_key = '12345'
def crypt(s):
  r = ''
  for i in s:
    for j in pubilc_key:
      i = chr(ord(i)^ord(j))
    for m in private_key:
      i = chr(ord(i)^ord(m))
    r +=i
  return r
def output(s):
  for i in s:
    print '0x%02X' %(ord(i)),
  print 
s = 'hello, world!'
output(s)
r = crypt(s)
output(r)
r = crypt(r)
output(r)

