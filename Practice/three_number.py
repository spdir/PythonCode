# -*- coding: UTF-8 -*-
#四个数，生成3位不相同的数字
n = (1,2,3,4)
s = 0
for i in n:
  for j in n:
    for m in n:
      if i == j or i == m or j== m:
        continue
      print '%d%d%d' %(i,j,m),
      s +=1
  print
print '-----------------------------------'
print 'sum%d: ' %s
