
def sumDigits(num):  # Define a function that takes a number as input
    return sum(int(digit) for digit in str(num))  # Convert the number to a string, iterate over each character, convert each character back to an integer, and sum them

print(sumDigits(123))  # Call the function with 123 and print the result