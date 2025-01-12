"""2025, Kadir Emir, https://github.com/kadiremir

Big O Notation is a mathematical notation that describes the complexity of an algorithm in terms of time and space.

Note that it descibes the complexity in the worst-case scenario.
For the best-case scenario, we can use Omega Notation; and for the average-case scenario, we can use Theta Notation.

It provides a standardized way to compare the efficiency of different algorithms and data structures.

For the table and cheat sheet, please visit:
https://www.bigocheatsheet.com/
"""

########################################################################################
# 1. TIME COMPLEXITY:
########################################################################################

# In terms of time complexity, the Big O Notation describes
# how the running time of an algorithm grows as the input size increases.

#####################################
# 1. O(1) - Constant Time Complexity:
#####################################


def print_number():
    print(1)


def print_number_two_times():
    print(1)
    print(2)


def function_three(n: int):
    return 3 * (n + n)

# These functions have time complexity of O(1)
# because the number of operations is constant and does not depend on the input size.

# Note that there is no O(2) or O(3) in the big O notation,
# unless the input size does not affect the number of operations!
# The constant factor is ignored in the big O notation.


#####################################
# 2. O(n) - Linear Time Complexity (In otger words, Proportional Time Complexity):
#####################################

def print_numbers(n: int):
    for i in range(n):
        print(i)

# This function has a time complexity of O(n)
# because the number of iterations in the loop is directly proportional to the input size n.


def print_numbers_two_times(n: int):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

# This function has a time complexity of O(n) instead of O(2n)
# because the constant factor 2 is ignored in the big O notation.
# The importance is being linearly proportional to the input size n.


#####################################
# 3. O(n^2) - Quadratic Time Complexity:
#####################################

def print_numbers_combinations(n: int):
    for i in range(n):
        for j in range(n):
            print(i, j)

# This function has a time complexity of O(n^2)
# because the number of iterations in the nested loops is proportional to the square of the input size n.


def function_powered(n: int):
    return 3 * (n ** n)

# This function has also a time complexity of O(n^2)
# because the power operation (n raised to the power of n), which is exponential in nature.
# and multiplication by 3 is a constant-time operation, which does not affect the overall time complexity.

# Note that:
# Not only constants, we can also drop non-dominant terms in the big O notation.
# Because the non-dominant terms are not important when the input size is large.
# For instance, O(n^2 + n) is simplified as O(n^2) because n^2 is the dominant term.
# Similarly, O(n^2 + 2n + 3) is simplified as O(n^2) because n^2 is the dominant term.


#####################################
# 4. O(log n) - Logarithmic Time Complexity:
#####################################

# Logarithmic time complexity is commonly seen in algorithms that divide the problem in half at each step.
# For instance, binary search algorithm has a time complexity of O(log n).

# Example: Lets say we have an ORDERED list of 16 elements.
# We want to find the index of the element 16.
# We can start from the middle element (8th element).
# If the middle element is greater than 16, then we can discard the right half.
# If the middle element is less than 16, then we can discard the left half.
# In each step, we can eliminate half of the elements.
# So, the number of steps required to find the element is log2(16) = 4.
# In other words, the number of the operations is 2**4 = 16.

# In general, for an ORDERED list of n elements, the number of operations is log2(n).
# So, the time complexity of the binary search algorithm is O(log n).

# WARNING: Multiple variable functions needs to be considered carefully. For instance,

def function_multi(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

# The time complexity of this function is O(a + b) because
# the number of iterations in the loops is proportional to the sum of a and b.

# WARNING: Be careful with lists. For instance,

a = [1, 2, 3, 4, 5]

a.append(6)  # O(1)
# This is O(1) because the append operation is a constant-time operation.
a.pop(3)  # O(n)
# This is O(n) because the pop operation requires shifting the elements after the deleted element.
last_index = len(a) - 1
a.pop(last_index)  # O(1)
# This is O(1) because the last element can be deleted directly.
a.insert(3, 4)  # O(n)
# This is O(n) because the insert operation requires shifting the elements after the inserted element.


########################################################################################
# 1. SPACE COMPLEXITY:
########################################################################################

# In terms of space complexity, the Big O Notation describes
# how the memory usage of an algorithm grows as the input size increases.

# Space complexity refers to the total amount of memory required by a program to execute, including memory for:
#
# Variables: Memory used by variables, constants, arrays, etc.
# Auxiliary Data Structures: Memory for additional data structures created during execution.
# Function Call Stack: Memory used for recursive function calls.
# Input Storage: Memory used to store input data.

#####################################
# 1. O(1) - Constant Space Complexity:
#####################################

# The space complexity of an algorithm is O(1) if the amount of memory used by the algorithm is constant,
# regardless of the input size.

def constant_space(n: int):
    x = 5
    y = 10
    z = x + y
    return z

# This function has a space complexity of O(1)
# because the amount of memory used by the algorithm is constant and does not depend on the input size.

#####################################
# 2. O(n) - Linear Space Complexity:
#####################################

# The space complexity of an algorithm is O(n)
# if the amount of memory used by the algorithm is proportional to the input size n.


def linear_space(n: int):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers

# This function has a space complexity of O(n) because the result list grows as n.


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# This function has a space complexity of O(n) because the recursive calls are stored in the function call stack.


#####################################
# 3. O(n^2) - Quadratic Space Complexity:
#####################################

def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix

# Space complexity O(n^2) because the 2D list requires n * n space.
