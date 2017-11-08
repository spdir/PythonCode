# -*- coding: UTF-8 -*-
#两点形成一个面，判断随机点是否在这个面中或上
a1x = 0
a1y = 4
a2x = 3
a2y = 0

x_min = a1x
y_min = a1y
x_max = a2x
y_max = a2y

if a1x > a2x:
  x_min = a2x
  x_max = a1x
if a1y > a2y:
  y_min = a2y
  y_max = a1y

x0 = input('x0 = ')
y0 = input('y0 = ')

if (x0 >= x_min and x0 <= x_max) and (y0 >= y_min and y0 <= y_max):
  print 'IN'
else:
  print 'OUT'