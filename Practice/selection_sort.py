#-*- coding:utf-8 -*-
#选择排序
#python3.5.2
def findSmallest(arr):
    smallest = arr[0]   #存储最小的值
    smallest_index = 0  #存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): #对数组进行排序
    newArr = []
    for i in range(len(arr)):  # 通过遍历找出数组中最小的元素，并将其加入到数组中
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
