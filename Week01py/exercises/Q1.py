def fib(n):  # Define a function to generate Fibonacci series up to n terms
    a, b = 0, 1  # Initialize the first two terms of the series
    result = []  # Create an empty list to store the series
    for _ in range(n):  # Loop n times
        result.append(a)  # Add the current term to the list
        a, b = b, a + b  # Update the terms for the next iteration
    return result  # Return the generated series

n = int(input("Enter the number of terms in the Fibonacci series: "))  # Get the number of terms from the user
print(fib(n))  # Print the generated Fibonacci series

