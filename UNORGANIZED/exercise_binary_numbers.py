from collections import deque


def print_binary_numbers(n: int):
    """Print binary numbers from 1 to n using a deque.

    Args:
        n (int): Number of binary numbers to generate.
    """
    # Initialize a deque
    q = deque()

    # Start with the first binary number
    q.append("1")

    # Generate binary numbers
    for _ in range(n):
        # Get the front of the deque
        front = q.popleft()

        # Print the current binary number
        print(front)

        # Generate the next two binary numbers and add them to the deque
        q.append(front + "0")
        q.append(front + "1")


# Example usage
num = 20  # Generate binary numbers from 1 to 20
print_binary_numbers(num)
