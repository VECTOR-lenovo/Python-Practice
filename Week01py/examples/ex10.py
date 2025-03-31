def count_down(start_number):  # Define a function named count_down that takes one argument
    current = 3  # Initialize the variable current to 3
    while (current > 0):  # Start a while loop that runs as long as current is greater than 0
        print(current)  # Print the current value
        current -= 1  # Decrease the value of current by 1
    print("Zero!")  # Print "Zero!" after the loop ends
count_down(3)  # Call the count_down function with the argument 3