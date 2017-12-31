# -*- coding: utf-8 -*-
import random

def insert_sort(array):
  for i in range(1,len(array)):
    tmp = array[i]
    j = i - 1
    while j >=0 and array[j] > tmp:
      array[j+1] = array[j]
      j  = j - 1
    array[j + 1] = tmp
  return array

if __name__ == '__main__':
  array = [i for i in range(9)]
  random.shuffle(array)
  print insert_sort(array)