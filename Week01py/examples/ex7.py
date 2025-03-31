def is_Even(number):  # Defines a function named is_Even that takes one argument called number
    if (number % 2 == 0):  # Checks if the number is divisible by 2 with no remainder
        return True  # If true, returns True
    return False  # If false, returns False

print(is_Even(7))  # Calls the function with the argument 7 and print the result