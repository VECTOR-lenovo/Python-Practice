hrs = input("Enter Hours:")  # Asks the user to enter hours worked
h = float(hrs)  # Converts the entered hours to a float number
rate = input("Enter the rate per hour:")  # Asks the user to enter the rate per hour
r = float(rate)  # Converts the entered rate to a float number
if h <= 40:  # Checks if hours worked are less than or equal to 40
    total_amount = h * r  # Calculates total pay for 40 or fewer hours
    print(f"The total amount of gross pay equals to: {total_amount}")  # Printz the total amount
elif h > 40:  # Checks if hours worked are more than 40
    total_amount = 40 * r + (h - 40) * (r * 1.5)  # Calculates total pay with overtime
    print(f"The total amount of gross pay equals to: {total_amount}")  # Prints the total amount
else:  # If the input is invalid
    print("Invalid Time!")  # Print an error message