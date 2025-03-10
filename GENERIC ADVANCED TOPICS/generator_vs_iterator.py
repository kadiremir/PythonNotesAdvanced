"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain and compare iterators and generators.

========================================
Iterators:
    - are objects that implement the __iter__ and __next__ methods.
    - are used to iterate over a sequence of elements.
    - can be created using the iter() function.
    - can be used with the for loop.

    Which types are iterators?
        - Lists
        - Tuples
        - Dictionaries
        - Sets
        - Strings
        - Files

========================================
Generators
    - are iterators, a kind of iterable you can only iterate over once.
"""

#############################################
# ITERATOR - EXAMPLE
#############################################

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)  # Create an iterator object from a list

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3


#############################################
# GENERATOR - EXAMPLE
#############################################
def my_generator():
    """Generator example."""
    x = 1
    while True:
        yield x
        x += 1


gen = my_generator()  # Create a generator object

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


#############################################
# GENERATOR - FIBONACCI EXAMPLE
#############################################
def fibonacci():
    """Generator for Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = fibonacci()  # Create a generator object

print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
