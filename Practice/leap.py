#  -*- coding: UTF-8 -*-
#从键盘输入一个年号，判断这一年是平年还是闰年
while True:
    year = input('Please input year: ')

    if year >= 3200:
        if year % 3200 == 0 and year % 172800 == 0:
            print 'year= %d is leap year' % year
        else:
            print 'year= %d is nonleap year' % year
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print 'year= %d is leap year' % year
        else:
            print 'year= %d is nonleap year' % year