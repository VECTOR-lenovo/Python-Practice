def SumDigits(n):  # Define a function named SumDigits that takes an integer n as an argument
    sum_of_digits = sum(int(digit) for digit in str(n))  # Convert the integer n to a string, iterate over each character, convert each character back to an integer, and sum them up
    print(sum_of_digits)  # Print the sum of the digits
SumDigits(611)  # Call the SumDigits function with the argument 611