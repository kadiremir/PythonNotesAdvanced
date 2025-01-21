"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain mutable and immutable objects in Python.
"""

#############################################
# MUTABLE OBJECTS
#############################################
# Mutable objects are objects whose state or contents can be changed after they are created.
# Examples: Lists, Dictionaries, and Sets.

# When a mutable object is modified, its memory address remains the same.
my_list = [1, 2, 3, 4, 5]

print(f"Object: {my_list}, Memory Address: {id(my_list)}")
my_list.append(6)
print(f"Object: {my_list}, Memory Address remains the same: {id(my_list)}")

# Dictionaries are also mutable.
my_dict = {"key1": "value1", "key2": "value2"}
print(f"Object: {my_dict}, Memory Address: {id(my_dict)}")
my_dict["key3"] = "value3"
print(f"Object: {my_dict}, Memory Address remains the same: {id(my_dict)}")

# Sets are mutable as well.
my_set = {1, 2, 3}
print(f"Object: {my_set}, Memory Address: {id(my_set)}")
my_set.add(4)
print(f"Object: {my_set}, Memory Address remains the same: {id(my_set)}")

#############################################
# IMMUTABLE OBJECTS
#############################################
# Immutable objects are objects whose state or contents cannot be changed after they are created.
# Examples: Integers, Strings, and Tuples.

# When an immutable object is "modified," a new object is created with a different memory address.

# Example with strings:
my_str = "Hello, World!"
print(f"Object: {my_str}, Memory Address: {id(my_str)}")
my_str += " How are you?"
print(f"Object: {my_str}, Memory Address changed: {id(my_str)}")

# Example with integers:
my_int = 5
print(f"Object: {my_int}, Memory Address: {id(my_int)}")
my_int = 6
print(f"Object: {my_int}, Memory Address changed: {id(my_int)}")
my_int += 5
print(f"Object: {my_int}, Memory Address changed: {id(my_int)}")

# Example with tuples:
my_tuple = (1, 2, 3)
print(f"Object: {my_tuple}, Memory Address: {id(my_tuple)}")
my_tuple += (4,)
print(f"Object: {my_tuple}, Memory Address changed: {id(my_tuple)}")

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
print(f"Memory Address of b: {id(b)}")
b = 6
print(f"Value of a: {a}, Memory Address of a: {id(a)}")
print(f"Value of b: {b}, Memory Address of b: {id(b)}")
# When b is reassigned, it creates a new object in memory.

# Behavior of mutable objects:
c = [1, 2, 3]
d = c
print(f"Memory Address of c: {id(c)}")
print(f"Memory Address of d: {id(d)}")
d.append(4)
print(f"Value of c: {c}, Memory Address of c: {id(c)}")
print(f"Value of d: {d}, Memory Address of d: {id(d)}")
# When d is modified, c is also affected because both variables reference the same object.

#############################################
# Key Takeaways
#############################################
# - Use mutable objects when you need to modify the data in place.
# - Use immutable objects when you want to ensure the data remains constant and avoid unintended side effects.
# - Be cautious when assigning mutable objects to multiple variables, as changes in one variable will reflect in others.
