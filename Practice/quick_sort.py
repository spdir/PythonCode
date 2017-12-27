#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quickSort(array,reverse=False):
  if len(array) < 2:
    return array
  else:
    provi = array[0]
    less = [i for i in array[1:] if i <= provi]
    geater = [i for i in array[1:] if i > provi]
  if reverse:
    return quickSort(geater, reverse=True) + [provi] + quickSort(less,reverse=True)
  else:
    return quickSort(less) + [provi] + quickSort(geater)

mylist = [2,55,66,22,43,67,12]

print quickSort(mylist,reverse=False)
