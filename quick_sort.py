def quick_sort(arr):
    """Quick Sort Algorithm"""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr1 = [38, 27, 43, 3, 9, 82, 10]
arr2 = arr1.copy()