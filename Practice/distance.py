# -*- coding: UTF-8 -*-
#计算两点直线的距离
#p1: x1 y1
#p2: x2,y2

x1,y1,x2,y2 = 0, 4, 3, 0
l = ((x1-x2)**2 + (y1-y2)**2)**(1./2)
print '(%f,%f) to (%f,%f) is : %f' %(x1,y1,x2,y2,l)

x = input('x = ')
y = input('y = ')
if 0 <= x <= 3 and 0 <= y <= 4:
    print 'in'
else:
    print 'out'