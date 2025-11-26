#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a number using recursion.

    Parameters:
        n (int): The number to calculate the factorial for.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the argument from command line, convert to int, and compute factorial
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
