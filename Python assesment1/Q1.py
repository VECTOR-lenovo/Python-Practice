## Name : Unish Bhattarai
## Student ID: 2509860
## Title: Sequence generator In AP
## This program generates a sequence of 100 numbers in arithmetic progression using a list in Python.

def generate_AP():
    # Create an empty list to store the sequence
    ap_sequence = []

    # Generate 100 numbers in arithmetic progression
    for i in range(0, 100):
        i = i * 4  # Multiply the index by 4 to get the sequence value
        ap_sequence.append(i)  # Add the value to the list

    return ap_sequence  # Return the generated sequence


# Print the generated sequence
print(generate_AP())