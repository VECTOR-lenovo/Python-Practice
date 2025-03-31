values = [10, 20, 30, 40, 50]  # List of values
Sum = 0  # Initialize sum to 0
length = 0  # Initialize length to 0
for value in values:  # Loop through each value in the list
    Sum = Sum + value  # Add the value to the sum
    length = length + 1  # Increment the length by 1
print("Total sum= " + str(Sum) + " and the Average=" + str(Sum / length))  # Print the total sum and average