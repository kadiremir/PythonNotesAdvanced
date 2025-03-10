"""2025, Kadir Emir, https://github.com/kadiremir

This file explains the difference between the break, continue and pass statements.
"""

####################################################################################################
# PASS
####################################################################################################
# The pass statement is used as a placeholder for future code.
# Does nothing

# Example:
for i in range(4):
    if i == 2:
        pass  # Placeholder, does nothing
    print(i)

# Output:
# 0
# 1
# 2
# 3

####################################################################################################
# CONTINUE
####################################################################################################
# The continue statement is used to skip the rest of the code inside a loop for the current iteration.
# It moves the control to the beginning of the loop.

# Example:
for i in range(4):
    if i == 2:
        continue
    print(i)

# Output:
# 0
# 1
# 3

####################################################################################################
# BREAK
####################################################################################################
# The break statement is used to exit a loop prematurely.
# It terminates the current loop and resumes execution at the next statement after the loop.

# Example:
for i in range(5):
    if i == 2:
        break
    print(i)

# Output:
# 0
# 1
