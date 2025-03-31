def number_group(number):  # Defines a function named number_group that takes one argument called number
    if number > 0:  # Checks if the number is greater than 0
        return "Positive"  # If true, returns "Positive"
    elif number == 0:  # Checks if the number is equal to 0
        return "Zero"  # If true, returns "Zero"
    else:  # If the number is not greater than 0 and not equal to 0
        return "Negative"  # Returns "Negative"
print(number_group(10))  # Calls the function with 10 and print the result
print(number_group(0))  # Calls the function with 0 and print the result
print(number_group(-5))  # Calls the function with -5 and print the result