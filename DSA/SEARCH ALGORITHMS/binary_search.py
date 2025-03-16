"""Binary Search Algorithm:

    - Binary search is a divide-and-conquer algorithm.
    - It works on sorted arrays.

Time Complexity: O(log_2 n)
Space Complexity: O(1)

Pseudocode:
    Assume that we search x.

    If x is in the middle:
        Return True.
    Else if x is less than the middle:
        Search the left half.
    Else:
        Search the right half.
"""

def binary_search_recursive(arr, target):
    """Binary search algorithm."""
    if arr == []:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            return binary_search_recursive(arr[:mid], target)
        else:
            return binary_search_recursive(arr[mid + 1:], target)


def binary_search_non_recursive(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  # Found, return index

        elif arr[mid] < target:
            left = mid + 1  # Search right half

        else:
            right = mid - 1  # Search left half

    return -1  # Not found


# Test
arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90]
target = 10
print(binary_search_recursive(arr, target))  # True
print(binary_search_non_recursive(arr, target))  # 3
target = 100
print(binary_search_recursive(arr, target))  # False
print(binary_search_non_recursive(arr, target))