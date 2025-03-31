def order_numbers(number1, number2):  # Defines a function to order two numbers
    if number2 > number1:  # Checks if the second number is greater than the first
        return number1, number2  # Returns the numbers in ascending order
    else:
        return number2, number1  # Returns the numbers in ascending order if the first is greater

smaller, bigger = order_numbers(100, 99)  # Calls the function with 100 and 99, and unpack the result
print(smaller, bigger)  # Prints the ordered numbers