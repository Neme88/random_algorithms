
def selection_sort(arr):
    """Selection Sort Algorithm"""
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume current index is the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update the minimum index
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr