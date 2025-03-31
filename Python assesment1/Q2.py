## Name : Unish Bhattarai
## Student ID: 2509860
## Title: Sequence generator In gp
## This program generates a sequence of 20 numbers in geometric progression using a list in Python.

def sequence_generator():
    # Create an empty list to store the sequence
    sequence_list = []

    # Generate 20 numbers in geometric progression
    for i in range(1, 21):
        i = 2 ** i  # Calculate the value for the sequence
        sequence_list.append(i)  # Add the value to the list

    return sequence_list  # Return the generated sequence

# Print the generated sequence
print(sequence_generator())