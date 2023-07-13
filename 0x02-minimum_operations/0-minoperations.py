def minOperations(n):
    if not isinstance(n, int):
        return 0  # If n is not an integer, return 0
    
    ops_count = 0  # Variable to keep track of the number of operations
    clipboard = 0  # Variable to store the copied value
    done = 1  # Variable to keep track of the number of 'H' characters achieved
    
    while done < n:
        if n % done == 0:
            # If the remaining count is divisible by the achieved count, perform Copy All and Paste operation
            clipboard = done  # Copy the current number of 'H' characters
            done += clipboard  # Add the copied value to the number of 'H' characters achieved
            ops_count += 2  # Increment the operation count by 2 (Copy All and Paste)
        else:
            # If the remaining count is not divisible by the achieved count, perform only Paste operation
            done += clipboard  # Add the copied value to the number of 'H' characters achieved
            ops_count += 1  # Increment the operation count by 1 (Paste)
    
    return ops_count  # Return the total number of operations required
