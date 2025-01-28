import multiprocessing
from quick_sort import quick_sort

def parallel_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if len(arr) > 10000:
        with multiprocessing.Pool(2) as pool:
            left, right = pool.map(quick_sort, [left, right])
    else:
        left = quick_sort(left)
        right = quick_sort(right)
    
    return left + middle + right