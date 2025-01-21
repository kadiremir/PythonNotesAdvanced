

def countdown(num: int) -> None:
    """Prints the countdown from the given number to 1."""
    if num == 0:
        return
    print(num, "...")
    countdown(num - 1)
    print("Returning from", num)


countdown(5)

# Actual output:
# 5 ...
# 4 ...
# 3 ...
# 2 ...
# 1 ...
# Returning from 1
# Returning from 2
# Returning from 3
# Returning from 4
# Returning from 5

# Why?
# The countdown(num - 1) call pauses execution of the current instance of the function,
# saving its state (including the line to execute next: print("Returning from", num)) on the call stack.
# This process repeats until the base case (num == 0) is reached. At that point, the recursion stops and the function returns.

# Breakdown for countdown(3):
# Step 1: Call countdown(3):
#
# Print 3, "...".
# Call countdown(2).
# Step 2: Call countdown(2):
#
# Print 2, "...".
# Call countdown(1).
# Step 3: Call countdown(1):
#
# Print 1, "...".
# Call countdown(0).
# Step 4: Call countdown(0):
#
# Base case is reached, so it returns without printing anything.
# Step 5: Return to countdown(1):
#
# Execute print("Returning from", 1).
# Step 6: Return to countdown(2):
#
# Execute print("Returning from", 2).
# Step 7: Return to countdown(3):
#
# Execute print("Returning from", 3).
