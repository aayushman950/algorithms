def heap_sort(arr):
    n = len(arr)

    # Step 1: Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (largest element) with the last element
        arr[0], arr[i] = arr[i], arr[0]

        # Call max_heapify on the reduced heap
        max_heapify(arr, i, 0)

    return arr


def max_heapify(arr, n, i):
    largest = i  # Initialize largest as the root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if the right child exists and is greater than the largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        max_heapify(arr, n, largest)  # Recursively heapify the affected subtree
