"""2025, Kadir Emir, https://github.com/kadiremir

This file explains the enumerate() function in Python.

enumerate():
    - Returns an enumerate object.
    - The enumerate object contains the index and the value of the elements in an iterable.
    - The enumerate object can be converted to a list, tuple, or dictionary.

Which objects can be enumerated?
    - Lists
    - Tuples
    - Strings
    - Sets
    - Dictionaries
"""

# Example with a list
my_list = ['a', 'b', 'c', 'd', 'e']
for i, value in enumerate(my_list):
    print(f"Index: {i}, Value: {value}")

# Example with a tuple
my_tuple = ('a', 'b', 'c', 'd', 'e')
for i, value in enumerate(my_tuple):
    print(f"Index: {i}, Value: {value}")

# Example with a string
my_string = "Hello, World!"
for i, value in enumerate(my_string):
    print(f"Index: {i}, Value: {value}")

# Example with a set
my_set = {1, 2, 3, 4, 5}
for i, value in enumerate(my_set):
    print(f"Index: {i}, Value: {value}")

# Example with a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for i, (key, value) in enumerate(my_dict.items()):
    print(f"Index: {i}, Key: {key}, Value: {value}")
