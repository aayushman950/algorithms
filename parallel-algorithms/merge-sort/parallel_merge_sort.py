import multiprocessing
from merge_sort import merge, merge_sort

def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    if len(arr) > 10000:  # Threshold for parallel processing
        with multiprocessing.Pool(2) as pool:
            left, right = pool.map(merge_sort, [left, right])
    else:
        left = merge_sort(left)
        right = merge_sort(right)
    
    return merge(left, right)