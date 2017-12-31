# -*- coding: utf-8 -*-
import random

def select_sort(array):
  l = len(array)
  for i in range(l-1):
    mix_loc = i
    for j in range(i+1,l):
      if array[j] < array[mix_loc]:
        mix_loc = j
    array[i], array[mix_loc] = array[mix_loc], array[i]
  return array

    

if __name__ == '__main__':
  array = [i for i in range(1000)]
  random.shuffle(array)
  print select_sort(array)