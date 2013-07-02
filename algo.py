def insertionSort(array):
    for j in range(1,len(array)):
        key = array[j]
        i = j
        while i > 0 and array[i - 1] > key:
            array[i] = array[i - 1]
            i = i - 1
        array[i] = key
    return array

def mergeSort(array):
    if len(array) <= 1:
        return array # recursion base case
    else:
        middle_index = len(array)/2
        left = []
        right = []
        for i in range(middle_index):
            left.append(array[i])

        for i in range(middle_index,len(array)):
            right.append(array[i])
        left = mergeSort(left)
        right = mergeSort(right)
        result = merge(left,right)
        return result

def merge(left, right):
    result = []
    while len(left) > 0 or len(right)>0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def quickSort(array):
    if len(array) <= 1:
        return array
    less = []
    greater = []
    pivot = array[len(array)/2]
    array.remove(pivot)
    for value in array:
        if value < pivot:
            less.append(value)
        else:
            greater.append(value)
    return quickSort(less)+[pivot]+quickSort(greater)

def bubbleSort(array):
    swap = True
    while swap:
        swap = False
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                save = array[i-1]
                array[i-1] = array[i]
                array[i] = save
                swap = True
    return array
