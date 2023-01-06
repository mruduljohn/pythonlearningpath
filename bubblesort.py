#array bubble sort
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

#input array using manual input
def new_func(bubbleSort):
    array = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        array.append(ele)
    print(bubbleSort(array))

new_func(bubbleSort)

