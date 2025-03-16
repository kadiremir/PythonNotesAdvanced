"""Linear Search Algorithm:

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """Linear search algorithm."""
    for i in arr:
        if i == target:
            return True
    return False

# Test
arr = [2, 3, 4, 10, 40]
target = 10
print(linear_search(arr, target))  # True
target = 100
print(linear_search(arr, target))  # False