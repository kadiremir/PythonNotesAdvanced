"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain the difference between "is" and "==" operators.

is:
    - Compares the memory address of the objects.
    - Returns True if both objects are the same object.

==:
    - Compares the values of the objects.
    - Returns True if the values of the objects are equal.
"""

#############################################
# Example 1
#############################################
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because `b` references the same object as `a`.
print(a is c)  # False, because `c` is a different object with the same content.

#############################################
# Example 2
#############################################
a = [1, 2, 3]
c = [1, 2, 3]

print(a == c)  # True, because the contents of `a` and `c` are the same.
