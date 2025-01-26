def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    smaller = []   # Elements smaller than the pivot
    bigger = []  # Elements bigger than the pivot
    equal = []

    # Partition the array
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num > pivot:
            bigger.append(num)
        else:
            equal.append(num)
    
    # Recursively sort the left (smaller) and right (bigger) partitions
    return quick_sort(smaller) + equal + quick_sort(bigger)