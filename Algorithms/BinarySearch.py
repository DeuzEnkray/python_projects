# __gold-init__
# Binary Search
# Only works with sorted arrays

def binary_search(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2

        if array[mid] == item:
            return mid

        elif array[mid] < item:
            low = mid + 1

        else:
            high = mid - 1

    return None
