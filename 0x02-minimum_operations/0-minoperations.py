#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0  # If n is 1, no operations are needed since 'H' is already present
    
    operations = 0
    factor = 2  # Start with factor = 2 (smallest possible factor)
    
    while factor <= n:
        if n % factor == 0:
            operations += factor  # Perform Copy All followed by Paste factor times
            n = n // factor  # Update n by dividing with factor
        else:
            factor += 1  # Increment factor if it doesn't divide n evenly
    
    return operations
