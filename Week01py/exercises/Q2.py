def myPow(x, n):  # Define a function myPow that takes two arguments x and n
    result = 1  # Initialize result to 1
    while n > 0:  # Loop while n is greater than 0
        result *= x  # Multiply result by x
        n -= 1  # Decrease n by 1
    return result  # Return the final result
print(myPow(4, 2))  # Print the result of myPow(4, 2)