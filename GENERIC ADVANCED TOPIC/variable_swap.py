"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain the swap of two variables in Python.

The main question is: How to swap two variables in Python?

Brief answer: You can swap two variables in Python using the following syntax:
a, b = b, a

Note that, "there is no need to use a temporary variable to swap the values of a and b".

The reason is that the right-hand side of the assignment is evaluated first.
Python on the back side creates a tuple of the right-hand side values and then unpacks it into the left-hand side variables.
"""

# Let's dive into the details of how this works:

a = 5
b = 10

# When we call the following line of code:
a, b = b, a

# The right-hand side of the assignment is evaluated first.
# Python creates a tuple of the right-hand side values (b, a) which is (10, 5)
# and then unpacks it into the left-hand side variables (a, b).
# But these are not the same as the original a and b. Because the original a and b are replaced with these new values.
# And they become a completely new object in memory.

# In other words, something like this happens:
# temp = (b, a)
# a = temp[0]
# b = temp[1]
# This is why the values of a and b are swapped without using a temporary variable like other programming languages.

# Lets this time do it with printing the values and also the memory addresses of the variables.

x = 5
y = 10

print(f"The memory address of x is: {id(x)}")
print(f"The memory address of y is: {id(y)}")

x, y = y, x

print(f"The new value of x is: {x}, and the memory address of x is: {id(x)}")
print(f"The new value of y is: {y}, and the memory address of y is: {id(y)}")

####################################################################################################
# Advanced question:
# Why not only the values of the variables are swapped but also the memory addresses?
####################################################################################################

# The reason is that when you use the assignment (=) statement, Python does not create a new object.
# Instead, it creates a new reference to the original object.
# Changes made via one reference affect the other since they point to the same memory location.

# Example:
e = [1, 2, 3]
f = e
print(f"The memory address of a is: {id(e)}")
print(f"The memory address of b is: {id(f)}")
e.append(4)
print(f"The list a is: {e}")
print(f"The list b is: {f}")
