
# Lets explain EVAL via calculator example

# syntax of eval is: eval(expression, globals=None, locals=None)
# expression - the expression to evaluate
# globals (optional) - a dictionary containing global variables
# locals (optional) - a dictionary containing local variables

user_input = input("Enter a mathematical expression: ")

# Evaluate the user's expression
result = eval(user_input)
print(f"The result of the expression is {result}")

# The eval() function evaluates the expression and returns the result.
# It is a built-in function in Python that takes a string as an argument and evaluates it as a Python expression.
# The eval() function can be used to execute arbitrary Python code from a string.
# However, it is important to be cautious when using eval() with user input, as it can be a security risk if the input is not properly sanitized.
# In the example above, the user is prompted to enter a mathematical expression, which is then evaluated using eval() and the result is printed.
# For example, if the user enters "2+3", the result will be 5.
# The eval() function can be useful for simple calculations or for evaluating expressions dynamically at runtime.


# The eval() function can also be used to define functions dynamically. For example:
def create_add_function(x):
    return eval(f"lambda   y: {x} + y")    # This is a lambda function that takes a parameter y and returns the sum of x and y.

add_five = create_add_function(5)
print(add_five(3))  # Output: 8

x = 10
result = eval("x + 5")
# Here the eval() function evaluates the expression "x + 5" in the context of the current scope, where x is defined as 10.

result_with_context = eval("x + y", {"x": 5}, {"y": 3})  # Evaluates to 8 (int)
# Here the eval() function evaluates the expression "x + y" in the context of the provided globals and locals dictionaries.

result = eval("x + y", {"x": 5, "y": 10}, {"y": 3})  # x is global, y is local
print(result)  # Outputs: 8 (x = 5 from globals, y = 3 from locals)
# Here the global y is overridden by the local y, so the result is 8.

# In this example, the create_add_function() function dynamically creates a lambda function that adds a specified value x to its input y.
# The eval() function is used to evaluate the lambda function expression, which is then returned by create_add_function().
# The resulting lambda function add_five is then called with an argument of 3, resulting in the output 8.
# This demonstrates how eval() can be used to create and evaluate functions dynamically at runtime.

# The eval() function can be a powerful tool for dynamically evaluating expressions and creating functions, but it should be used with caution, especially with untrusted input.
# It is important to validate and sanitize user input before passing it to eval() to prevent security vulnerabilities such as code injection attacks.
# In general, it is recommended to avoid using eval() with user input unless absolutely necessary, and to consider alternative approaches for dynamic code execution.

# Now lets talk about EXEC

# The exec() function in Python is used to execute a dynamically created Python code string or object.
# It is a built-in function in Python that takes a string as an argument and executes it as Python code.
# The exec() function can be used to execute arbitrary Python code dynamically at runtime. !!!!!!!!
# However, it is important to be cautious when using exec() with user input, as it can be a security risk if the input is not properly sanitized.
# The exec() function can be used to define functions, classes, and other Python code dynamically.


# In the example below, the exec() function is used to define a simple function that prints a message:
code = f"for i in range(5): print('Hello, World!')"
exec(code)

# Whatever exists in the code string will be executed by exec() function
# We can also define a function using exec() function
# The exec() function can be used to define functions, classes, and other Python code dynamically.
# In the example above, the exec() function is used to define a for loop that prints the message "Hello, World!" five times.
# The code string is passed to exec(), which executes the code dynamically at runtime.
# This demonstrates how exec() can be used to execute arbitrary Python code strings and define functions dynamically.


# Dynamic functions:
# The exec() function can be used to define DYNAMIC FUNCTIONS based on user input or other sources.

name = input("Enter your name: ")
code = f"def greet(name): print(f'Hello, {name}!')"
exec(code)
greet(name)

# Here above we are defining a function greet() dynamically using the exec() function.
# The user is prompted to enter their name, which is then passed to the greet() function defined using exec().
# The greet() function prints a personalized greeting message using the user's name.
# This demonstrates how exec() can be used to define functions dynamically based on user input.

