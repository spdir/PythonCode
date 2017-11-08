# -*- coding: UTF-8 -*-
#输入某年某月，判断这一天是一年的第几天

year = input('year = ')
mouth = input('mouth = ')
day = input('day = ')
def getdays(year,mouth,day):
  mouths = [0,31,59,90,120,151,181,212,243,273,304,334]
  if mouth > 0 and mouth <= 12:
    m = mouths[mouth-1]
  day +=m
  if mouth > 2:
    if year < 3200:
      if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        day +=1
    else:
      if (year % 3200 == 0 and year % 172800 == 0):
        day +=1
  print 'day(s):%d' %day

getdays(year,mouth,day)
