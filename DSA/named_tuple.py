"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain Named Tuples in Python.

Named Tuples:
    - Are extensions of the regular tuples.
    - Attributes can be accessed by name.
    - Created via a factory function.
    - Factory method takes two arguments:
        - class name
        - list of field names.

    - They are immutable, like regular tuples.
"""

from collections import namedtuple

# Creating a Named Tuple
Color = namedtuple('Color', ('red', 'green', 'blue'))

# Creating an instance of the Named Tuple
color = Color(255, 0, 0)

# Accessing the fields by name
print(color.red)  # 255
print(color.green)  # 0
print(color.blue)  # 0
