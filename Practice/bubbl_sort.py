# -*- coding: utf-8 -*-
import random

def bubbl_sort(array):
  l = len(array)
  for i in range(l):
     exchange = False
     for j in range(i+1,l):
       if array[i] > array[j]:
         array[j], array[i] = array[i], array[j]
         exchange = True
     if not exchange:
       break
  return array
  
if __name__ == '__main__':
  array = [i for i in range(1000)]
  random.shuffle(array)
  print array
  print bubbl_sort(array)