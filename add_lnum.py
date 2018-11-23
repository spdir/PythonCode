#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time

# 大数相加, 超出int64存储范围

def random_number():
  """
  随机生成一个大数
  :return:
  """
  length = random.randint(99, 9999)
  s = ''
  for i in range(length):
    s += str(random.randint(0, 9))
  return s


def strToList(s):
  """
  字符串转换为列表
  :param s:
  :return:
  """
  l = []
  for i in range(len(s)):
    l.append(s[i])
  return l


def floadBigAdd(a, b, c, d):
  """
  计算带小数点的大数
  :param a:
  :param b:
  :return:
  """
  max_x = max(len(c), len(d))  # 获取小数点后最长的长度
  x = bigAdd(c, d)  # 计算小数点后相加的结果
  if len(x) > max_x:  # 如果小数点计算后长度大于原先的长度，则进行进位1，小数点计算去除第一位
    # 小数点前的数进行加1
    a_l = strToList(a)
    a_l[0] = str(int(a_l[0]) + 1)
    a = ''.join(a_l)
    # 小数点后的数去除第一位
    x_l = strToList(x)
    x_l.pop(0)
    x = ''.join(x_l)
  s = bigAdd(a, b)
  return s + '.' + x


def bigAdd(a, b):
  """
  大数相加
  :param a:
  :param b:
  :return:
  """
  # 反转字符串之后转换为列表
  a = strToList(a[::-1])
  b = strToList(b[::-1])
  c = []  # 定义存储结果的列表

  max_str = [0]  # 定义不同位数存储列表，默认有一个数，如果位数相同且最后移为计算进1为，取值时会报错
  # 获取最短的数字长度
  if len(a) > len(b):
    length = len(b)
    max_str = a[length:]  # 取出最长字符串超出最短的部分
  elif len(a) < len(b):
    length = len(a)
    max_str = b[length:]
  else:
    length = len(a)

  t = 0  # 定义进位值
  for i in range(length):  # 循环计算值
    t1 = int(a[i]) + int(b[i])
    if t1 >= 10:
      t1 = t1 - 10
      c.append(str(t1 + int(t)))
      t = 1  # 大于10下一次计算进位1
    else:
      c.append(str(t1 + int(t)))
      t = 0  # 小于10下一次计算进位0
  if t == 1:  # 如果最后一次进位为1，将在超出部分加1
    max_str[0] = str(int(max_str[0]) + t)
  if max_str[-1] == 0:
    max_str = []
  c.extend(max_str)  # 计算合并列表
  sum = ''.join(c)  # 拼接字符串
  return sum[::-1]  # 反转字符串即为最后的计算结果


def main(a, b):
  """
  算法开始
  :param a:
  :param b:
  :return:
  """
  start_time = time.time()

  if '.' in a or '.' in b:
    a1, a2 = a.split('.')[0], a.split('.')[1] if len(a.split('.')) > 1 else []
    b1, b2 = b.split('.')[0], b.split('.')[1] if len(b.split('.')) > 1 else []
    c = floadBigAdd(a1, b1, a2, b2)
  else:
    c = bigAdd(a, b)
  print("Use Time: ", time.time() - start_time)
  return c


if __name__ == '__main__':
  ty = input("select Type(r/i): ")  # 选择是随机生成大数，还是手动输入数字
  a, b = '', ''
  if ty == 'r':
    a, b = random_number(), random_number()
  elif ty == 'i':
    a = str(input('A= '))
    b = str(input('B= '))
  else:
    exit("Input Error")
  print("A(%s):" % (len(a)), a)
  print("B(%s):" % (len(b)), b)
  c = main(a, b)
  print(c)
