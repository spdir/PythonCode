#使用二分查找法快速从一个数组中查找一个指定元素，并返回该元素的索引值
def binary_search(list, item):
    #low和high用于跟踪要在其中查找的列表部分
    low = 0
    high = len(list)-1

    while low <= high: #只要范围没有缩小到只包含一个元素
        #如果(low + high)不是偶数，python自动向下取整，这里来检查中间元素
        mid = (low + high) / 2  #取中间数
        guess = list[mid]
        if guess == item: #找到了元素
            return mid
        if guess > item: #猜的数字大了
            high = mid -1
        else:   #猜的数字小了
            low = mid + 1
    return None #没有指定元素

my_list1 = ['zhangsan', 'lisi', 'wangwu',]
my_list2 = list(range(10000))

print(binary_search(my_list1, 'lisi'))
print(binary_search(my_list2, 5002))
print(binary_search(my_list2, -110))
