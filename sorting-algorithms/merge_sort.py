def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    else:
        arr1 = arr[:len(arr)//2]
        arr2 = arr[len(arr)//2:]

        arr1 = merge_sort(arr1)
        arr2 = merge_sort(arr2)

        return merge(arr1, arr2)

def merge(arr1, arr2):
    result = []
    i = j = 0
    
    # Merge the arrays by comparing the elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # If any elements are left in arr1, add them
    result.extend(arr1[i:])
    
    # If any elements are left in arr2, add them
    result.extend(arr2[j:])
    
    return result