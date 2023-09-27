# __gold-init__
# Adaptive Bubble Sort

def bubble_sort(array):
    for i in range(len(array) - 1):
        flag = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True

        if flag is False:
            return
