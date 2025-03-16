"""Bubble Sort Algorithm:

    - Compare each "pair" of adjacent elements from the beginning of an array.
    - If the pairs are in reversed order, swap them.
    - Repeat the process for the whole array until the list is sorted.

Time Complexity: O(n^2) (worst-case) O(n) (best-case, already sorted)
Space Complexity: O(1) (in-place algorithm)
"""

def bubble_sort(arr):
    """Bubble sort algorithm."""
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
          if arr[i-1] > arr[i]:
            flag = True
            arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

def bubble_sort_another(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swap happens
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # No swaps mean the list is sorted
        if not swapped:
            break

# Test
A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(bubble_sort(A))  # [-5, -3, -3, 1, 2, 2, 2, 3, 7]
