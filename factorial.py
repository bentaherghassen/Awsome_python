def factorial(n):
    """Calculates the factorial of a number.

    Args:
      n: A non-negative integer.

    Returns:
      The factorial of n.
    """

    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage:

print(factorial(5))  # 120
