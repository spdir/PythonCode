# -*- coding: UTF-8 -*-
#冒泡排序
n = [1,11,22,11,-9,10,8,7,121,13]
def sort(n):
  l = len(n)
  for i in range(l):
    for j in range(i+1, l):
      if n[i] > n [j]:
        c = n[i]
        n[i] = n[j]
        n[j] = c
print n
sort(n)
print n
