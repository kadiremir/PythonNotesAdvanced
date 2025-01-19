"""2025, Kadir Emir, https://github.com/kadiremir

Goal:
    Merge two sorted arrays into a single sorted array.

Solution:
    - Initialize two pointers, one for each array (i for the first array, j for the second array), starting at the beginning (index 0).
    - Initialize an empty array to hold the merged result.
    - Compare the elements at the current indices of both arrays:
    - If the element in the first array is smaller, append it to the result and move the pointer in the first array forward.
    - Otherwise, append the element from the second array and move its pointer forward.
    - Continue this process until one of the arrays is fully traversed.
    - Append any remaining elements from the non-traversed array to the result (since it's already sorted).
    - The merged array is now sorted.

Notes:
    - This algorithm is used as a main idea of the "Merge Sort" algorithm.

Time Complexity: O(n+m) where n and m are the length of the arrays.
"""


def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []

    # Merge elements until one of the arrays is exhausted
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append the remaining elements from either array
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged


# Example Usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = merge_sorted_arrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
