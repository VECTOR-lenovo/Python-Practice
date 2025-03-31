def square(n):  # Define a function to square a number
    return n*n  # Return the square of the number

def sum_squares(x):  # Define a function to sum the squares of numbers
    sum = 0  # Initialize sum to 0
    for n in range(10):  # Loop through numbers from 0 to 9
        sum += square(n)  # Add the square of the current number to sum
    return sum  # Return the total sum

print(sum_squares(10))  # Print the result of sum_squares function with input 10