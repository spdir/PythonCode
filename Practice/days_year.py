# -*- coding: UTF-8 -*-
#输入某年某月，判断这一天是一年的第几天
#输入某年的多少天，判断是该年的几月几天
def isLeapYear(year):
  if year < 3200:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      return 1
  else:
    if year % 3200 == 0 and year % 172800 == 0:
      return 1
  return 0

def getDaysByYearMouth(year,mouth):
  days = [
          # 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12
           [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
           [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]        
         ]
  return days[isLeapYear(year)][mouth-1]

def getDaysYearMouth(year,mouth,day):
  days = day
  for i in range(1,mouth):
    days += getDaysByYearMouth(year,i)
  return days

def getMouthDayByYearDays(year,days):
  mouth = 1
  day = days
  while True:
    t = getDaysByYearMouth(year,mouth)
    if day < t:
      break
    mouth +=1
    day -=t
  return (mouth,day)

year = input('year = ')
mouth = input('mouth = ')
day = input('day = ')

days = getDaysYearMouth(year,mouth,day)
print '%d-%02d-%02d is %d day(s) of %d year.' %(year,mouth,day,days,year)

print '---------------------------------------------'
year = input('year = ')
days = input('days = ')
t = getMouthDayByYearDays(year,days)
mouth = t[0]
day = t[1]
print '%d day(s)(in %d year) is %02d mouth %02d day.' %(days,year,mouth,day)

