# -*- coding: utf-8 -*-
import random

def quick_sort(array,reverse=False):
  def sort(array):
    if len(array) < 2:
      return array
    else:
      pivot = array[0]
      less = [i for i in array[1:] if i <= pivot]
      greater = [i for i in array[1:] if i > pivot]
    return sort(less) + [pivot] + sort(greater)
  if reverse:
    return sort(array)[-1::-1]
  else:
    return sort(array)


if __name__ == '__main__':
  array = [i for i in range(30)]
  random.shuffle(array)
  print array
  # print quick_sort(array)
  print quick_sort(array,reverse=True)
