"""2025, Kadir Emir, https://github.com/kadiremir

This file is to explain the difference between decorators and context managers in Python.

Context Managers:
- Purpose: Manage resources by ensuring proper setup and cleanup, even in case of exceptions.
- Typical Use Cases: File operations, database connections, network sessions, etc.
- Key Features: Implemented using the 'with' statement and methods __enter__() and __exit__().

Decorators:
- Purpose: Modify or enhance the behavior of a function or method.
- Typical Use Cases: Logging, performance measurement, access control, etc.
- Key Features: Implemented as higher-order functions using the '@' syntax.
"""


########################################
# Basic example of using a context manager
########################################

with open("example.txt", "w") as file:
    file.write("Hello, context managers!")  # File is automatically closed after this block.


########################################
# A custom context manager
########################################

class ResourceManager:
    def __enter__(self):
        print("Acquiring resource.")
        # Setup code goes here (e.g., opening a file, acquiring a lock)
        return self  # Optionally return an object to the 'with' block.

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource.")
        # Cleanup code goes here (e.g., closing a file, releasing a lock)
        # Handle exceptions if necessary
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        # Return False to propagate the exception, True to suppress it.
        return False

# Using our custom context manager
try:
    with ResourceManager() as resource:
        print("Using the resource.")
        raise ValueError("An intentional error.")
except Exception as e:
    print(f"Caught an exception: {e}")

# Output:
# Acquiring resource.
# Using the resource.
# An exception occurred: An intentional error.
# Releasing resource.
# Caught an exception: An intentional error.


########################################
# Example of a custom decorator
########################################

def execution_logger(func):
    """A decorator that logs the start and end of a function's execution.
    """
    def wrapper(*args):
        print("Starting execution of the function.")
        func(*args)
        print("Function execution completed.")
    return wrapper

@execution_logger
def say_hello(name):
    print(f"Hello, {name}!")

# Using the decorated function
say_hello("Alice")

# Output:
# Starting execution of the function.
# Hello, Alice!
# Function execution completed.


############################################################
# Key Differences Between Context Managers and Decorators:
############################################################

"""
1. Purpose:
   - Context Manager: Ensures proper resource management with setup and cleanup.
   - Decorator: Modifies or enhances the behavior of functions or methods.

2. Syntax:
   - Context Manager: Used with the 'with' statement and __enter__/__exit__ methods.
   - Decorator: Uses '@' syntax and higher-order functions.

3. Focus:
   - Context Manager: Handles resource lifecycles (e.g., opening/closing files).
   - Decorator: Adds functionality (e.g., logging, validation) around existing code.

4. Exception Handling:
   - Context Manager: Can handle exceptions that occur within the 'with' block.
   - Decorator: Can only handle exceptions explicitly caught within the wrapper function.

5. Reusability:
   - Both context managers and decorators are reusable, but their focus and typical use cases differ significantly.
"""

# Combined Use Case: Using Both a Context Manager and a Decorator

class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed.")
        return result
    return wrapper

@log_decorator
def write_to_file(file, content):
    print(f"Writing to file: {content}")
    file.write(content)

# Using both
try:
    with FileContextManager("example.txt", "w") as f:
        write_to_file(f, "Hello, combined use of context managers and decorators!")
except Exception as e:
    print(f"Caught exception: {e}")

# Output:
# Opening file: example.txt
# Calling function: write_to_file
# Writing to file: Hello, combined use of context managers and decorators!
# Function write_to_file completed.
# Closing file: example.txt
