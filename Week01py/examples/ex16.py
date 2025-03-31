for left in range(7):  # Loop through numbers 0 to 6
    for right in range(left, 7):  # Loop through numbers from 'left' to 6
        print("["+str(left)+"|"+str(right)+"]", end=" ")  # Print the pair in the format [left|right] without a new line
print()  # Print a new line at the end