"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain mutable and immutable objects in Python.
"""

#############################################
# MUTABLE OBJECTS
#############################################
# Mutable objects are objects whose state or contents can be changed after they are created.
# Mutables: LISTS, SETS, DICTIONARIES

# When a mutable object is modified, its memory address remains the same.
my_list = [1, 2, 3, 4, 5]

# Lists
print(f"Object: {my_list}, Memory Address: {id(my_list)}") # Memory Address of the object
my_list.append(6)
print(f"Object: {my_list}, Memory Address remains the same: {id(my_list)}") # Memory Address remains the same

# Dictionaries
my_dict = {"key1": "value1", "key2": "value2"}
print(f"Object: {my_dict}, Memory Address: {id(my_dict)}") # Memory Address of the object
my_dict["key3"] = "value3"
print(f"Object: {my_dict}, Memory Address remains the same: {id(my_dict)}") # Memory Address remains the same

# Sets
my_set = {1, 2, 3}
print(f"Object: {my_set}, Memory Address: {id(my_set)}") # Memory Address of the object
my_set.add(4)
print(f"Object: {my_set}, Memory Address remains the same: {id(my_set)}") # Memory Address remains the same

#############################################
# IMMUTABLE OBJECTS
#############################################
# Immutable objects are objects whose state or contents cannot be changed after they are created.
# Immutables: INTEGERS, STRINGS, TUPLES

# When an immutable object is "modified," a new object is created with a different memory address.

# Strings
my_str = "Hello, World!"
print(f"Object: {my_str}, Memory Address: {id(my_str)}") # Memory Address of the object
my_str += " How are you?"
print(f"Object: {my_str}, Memory Address changed: {id(my_str)}") # Memory Address changed

# Integers
my_int = 5
print(f"Object: {my_int}, Memory Address: {id(my_int)}") # Memory Address of the object
my_int = 6
print(f"Object: {my_int}, Memory Address changed: {id(my_int)}") # Memory Address changed
my_int += 5
print(f"Object: {my_int}, Memory Address changed: {id(my_int)}") # Memory Address changed

# Tuples
my_tuple = (1, 2, 3)
print(f"Object: {my_tuple}, Memory Address: {id(my_tuple)}") # Memory Address of the object
my_tuple += (4,)
print(f"Object: {my_tuple}, Memory Address changed: {id(my_tuple)}") # Memory Address changed

################################################################
# WARNING! Be cautious when modifying immutable objects.
################################################################

# Since they are immutable, we can not modify the contents of an immutable object.

# For example, tuples:
# my_int = (1,2,3)
# my_int[0] = 4  # TypeError: 'tuple' object does not support item assignment

# or strings:
# my_str = "Hello, World!"
# my_str[0] = "h"  # TypeError: 'str' object does not support item assignment

#############################################
# Assignment and References
#############################################

# Behavior of immutable objects:
a = 5
b = a
print(f"Memory Address of a: {id(a)}")
print(f"Memory Address of b: {id(b)}") # Memory Address of a and b are the same.
b = 6
print(f"Value of a: {a}, Memory Address of a: {id(a)}") # Memory Address of a remains the same.
print(f"Value of b: {b}, Memory Address of b: {id(b)}") # Memory Address of b is now different.
# When b is reassigned, it creates a new object in memory.

# Behavior of mutable objects:
c = [1, 2, 3]
d = c # d is a reference to c
print(f"Memory Address of c: {id(c)}")
print(f"Memory Address of d: {id(d)}") # Memory Address of c and d are the same.
d.append(4)
print(f"Value of c: {c}, Memory Address of c: {id(c)}")
print(f"Value of d: {d}, Memory Address of d: {id(d)}") # Memory Address of c and d are still the same.
# When d is modified, c is also affected because both variables reference the same object.

#############################################
# Key Takeaways
#############################################
# - Use mutable objects when you need to modify the data in place.
# - Use immutable objects when you want to ensure the data remains constant and avoid unintended side effects.
# - Be cautious when assigning mutable objects to multiple variables, as changes in one variable will reflect in others.
