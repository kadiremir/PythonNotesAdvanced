"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain and compare the copy and deep_copy methods from the copy module.

1. copy() i.e. shallow copy method:
The copy() method is used to create a shallow copy of an object.
It creates a new object and copies the references of the nested objects.
So that the id of the main object is different but the id of the nested objects is the same.
Then, if you modify the nested objects, the changes will be reflected in the original object.

3. deep_copy() method:
The deep_copy() method is used to create a deep copy of an object.
It creates a new object that is a copy of the original object.
It also creates tje copies of the nested objects as well.
This means that changes made to the nested objects are not reflected in the original object.
"""

import copy

####################################################################################################
# 1. copy() method:
####################################################################################################

a = [1, 2, 3]
b = copy.copy(a)

# As you can see, the id of a and b are different, which means they are different objects.
print(f"The id of a on the memory is: {id(a)}")
print(f"The id of b on the memory is: {id(b)}")

# However, the id of the nested objects is the same.
print(f"The id of the first element of a is {id(a[0])}")
print(f"The id of the first element of b is {id(b[0])}")

# Now let`s modify the list a and see if it affects b.
a[2] = 4
print(f"The list a is {a}")
print(f"The list b is {b}")

####################################################################################################
# 2. deep_copy() method:
####################################################################################################

c = [1, 2, 3]
d = copy.deepcopy(c)

print(f"The id of c on the memory is: {id(c)}")
print(f"The id of d on the memory is: {id(d)}")

# This time, the ids of the nested objects are different.
print(f"The id of the first element of c is {id(c[0])}")
print(f"The id of the first element of d is {id(d[0])}")

# Now let`s modify the list c and see if it affects d.
c[2] = 4
print(f"The list c is {c}")
print(f"The list d is {d}")
