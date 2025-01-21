"""Insertion Sort Algorithm:

    - Start from the second element of the array.
    - Compare the current element with the previous elements.
    - If the current element is smaller, swap it with the previous element.
    - Iterate this process until the current element is greater than the previous element.
    - Repeat the process until the list is sorted.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    return arr

B = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(insertion_sort(B))