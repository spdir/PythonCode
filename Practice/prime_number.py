# -*- coding: UTF-8 -*-
#判断2到100之间的质数
#
#-------------------------------
a = []
for i in range(2,100+1):
  for j in range(2,int(i**(1/2.0))+1):
    if i % j == 0:
       break
  else:
    a.append(i)
print a
print len(a)



#-------------------------------
n = 2
a = []
while n <= 100:
  i = 2
  while i < n:
    if n % i == 0:
      break
    i +=1
  else:
    a.append(n)
  n +=1

print a
print len(a)
