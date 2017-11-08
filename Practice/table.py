# -*- coding: UTF-8 -*-
'''
[root@aery 011]# python bit.py
+------+-------------------------------------------+-----------+
| User | Password                                  | Host      |
+------+-------------------------------------------+-----------+
| root | *AC241830FFDDC8943AB31CBD47D758E79F7953EA | localhost |
| aery | *E56A114692FE0DE073F9A1DD68A00EEB9703F3F1 | 127.0.0.1 |
+------+-------------------------------------------+-----------+
'''


t = [
 ['User', 'Password', 'Host'],
 ['root', '*AC241830FFDDC8943AB31CBD47D758E79F7953EA', 'localhost'],
 ['aery', '*E56A114692FE0DE073F9A1DD68A00EEB9703F3F1', '127.0.0.1'],
]

def getLengths(t):
  l = []
  r = len(t)  #行
  c = len(t[0]) #列
  for i in range(c):
    n = 0
    for j in range(r):
      m = len(t[j][i])
      if n < m:
        n = m
    l.append(n)
  return l

def putLine(t):
  ls = getLengths(t)
  for i in ls:
    print '\b+--',
    for j in range(i):
      print '\b-',
  print '\b+'

def putContent(t,f):
  ls = getLengths(t)
  if f == 0:
    t = t[:1]
  else:
    t = t[1:]
  for i in t:
    for j in i:
      print '\b| ',
      print '\b%s' %(j),
      n = ls[i.index(j)] - len(j) + 1
      for k in range(n):
        print '',
    print '\b|'

def putHead(t):
  putContent(t, 0)

def putBody(t):
  putContent(t, 1)

def putTable(t):
  putLine(t)
  putHead(t)
  putLine(t)
  putBody(t)
  putLine(t)

putTable(t)

