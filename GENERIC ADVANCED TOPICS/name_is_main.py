"""2025, Kadir Emir, https://github.com/kadiremir

This file explains the meaning of

if __name__ == __main__

usage of Python files.

__name__ Variable:

    - Every Python module (file) has a built-in attribute called __name__.
    - When a module is run directly, __name__ is set to "__main__".
    - When a module is imported, __name__ is set to the module's name (its filename without the .py extension).

Purpose:

    - It is used to identify whether the script is being run directly or imported as a module.
    - i.e., the code within this block will only execute if the script is run directly.
"""

def function():
    return f"OK, got it, see ya!"

if __name__ == "__main__":
    # This block runs only when the script is executed directly.
    print(function())