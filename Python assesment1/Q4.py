## Name : Unish Bhattarai
## Student ID: 2509860
## Title: Finding missing numbers in a list
## This program finds the missing numbers in a list of integers from 1 to 15.

def missing_nums():
    # List of given numbers
    input_nums = [1, 2, 4, 5, 6, 8, 10, 13]
    # List to store missing numbers
    missing_nums = []
    # Check each number from 1 to 15
    for i in range(1, 16):
        # If the number is not in the given list, add it to the missing list
        if i not in input_nums:
            missing_nums.append(i)
    # Return the list of missing numbers
    return missing_nums

# Print the missing numbers
print(f"The missing numbers are: {missing_nums()}")