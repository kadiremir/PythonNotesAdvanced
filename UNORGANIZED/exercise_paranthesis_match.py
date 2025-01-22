

def paranthesis_match(word: str) -> bool:
    """Check if the parentheses in the string are balanced."""
    stack = []
    
    for char in word:
        if char == "(":
            stack.append(char)  # Push opening parenthesis onto the stack
        elif char == ")":
            if stack and stack[-1] == "(":  # Check for a matching opening parenthesis
                stack.pop()
            else:
                return False  # Unmatched closing parenthesis

    return len(stack) == 0  # Return True if the stack is empty (balanced)



