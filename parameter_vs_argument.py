"""2025, Kadir Emir, https://github.com/kadiremir

Parameters vs Arguments in Python

The terms parameter and argument are distinct in Python programming.
This file explains the difference with examples and includes a table for clarity.
"""
##############
# Parameter:
##############

# - A parameter is the variable listed in the function definition.
# - It acts as a placeholder to define what kind of data the function can accept.
# - Parameters are defined at the time of function creation and exist within the scope of the function.

def greet(name):  # 'name' is the parameter
    print(f"Hello, {name}!")

##############
# Argument:
##############

# - An argument is the actual value or data passed to the function when it is called.
# - Arguments supply the information required for the function to execute.

greet("Alice")  # "Alice" is the argument

##############
# Key Differences:
##############

# The following table summarizes the key differences between parameters and arguments:

key_differences = """
| Aspect           | Parameter                          | Argument                          |
|-------------------|------------------------------------|------------------------------------|
| **Definition**    | Placeholder in the function       | Actual data passed to the function |
| **Location**      | Function definition               | Function call                     |
| **Role**          | Specifies input requirements      | Supplies the input data           |
"""

print("Key Differences Between Parameter and Argument:\n")
print(key_differences)

##############
# Example:
##############
def add(a, b):  # 'a' and 'b' are parameters
    return a + b

# Passing arguments to the function
result = add(5, 3)  # 5 and 3 are arguments

print(f"The result of adding 5 and 3 is: {result}")