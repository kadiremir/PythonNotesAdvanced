"""Merge Sort Algorithm:

    - It is a divide-and-conquer algorithm.
    - It divides the input array into two halves.
    - Continues dividing the array until each sub-array has only one element.
    - Merges the sub-arrays with single items to produce new sorted arrays.
    - Repeats the process until there is only one sorted array remaining.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Combine
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge two sorted arrays into one sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Append remaining elements (if any)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array

# Example Usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
