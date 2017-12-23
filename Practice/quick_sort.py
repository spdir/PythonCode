#python 2.7
 
def quickSort(array):
  if len(array) < 2:
    return array
  else:
    provi = array[0]
    less = [i for i in array[1:] if i <= provi ]
    gt = [i for i in array[1:] if i > provi]
  return quickSort(less) + [provi] + quickSort(gt)

print quickSort([5,3,12,66,88,99,1,2])
