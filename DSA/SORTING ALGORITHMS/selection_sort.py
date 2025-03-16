"""Selection Sort Algorithm:

    - Selection sort repeatedly finds the smallest element from the unsorted portion of the list and places it at the beginning.
    - It continues this process until the list is sorted.

Time Complexity: Best, Average, and Worst-case: O(n²)
Space Complexity: O(1) (in-place algorithm)
"""

def selection_sort(arr):
    """Selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Test
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
