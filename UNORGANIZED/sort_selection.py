"""Selection Sort Algorithm:

    - Iterate over each element in the array.
    - For each element, find the index of the smallest element in the unsorted (right) part.
    - Swap the found minimum element with the first element of the unsorted part.


Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def selection_sort(arr):
    a = len(arr)
    for i in range(a):
        # Find the index of the smallest element in the unsorted part
        min_index = i
        for j in range(i + 1, a):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

C = [-3, 3, 2, 1, -5, -3, 7, 2, 2]
print(selection_sort(C))
