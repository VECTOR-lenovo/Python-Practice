## Name : Unish Bhattarai
## Student ID: 2509860
## Title: Fibonacci sequence generator
## This program generates the Fibonacci sequence up to 20 terms using a list in Python.

def fibo():
    # Create a list with the first two terms of the Fibonacci sequence
    fibo_list = [0, 1]
    # Generate the next 18 terms of the sequence
    for i in range(18):
        # Calculate the next term by adding the last two terms
        next_term = fibo_list[-1] + fibo_list[-2]
        # Add the next term to the list
        fibo_list.append(next_term)
    # Return the complete Fibonacci sequence
    return fibo_list

# Print the generated Fibonacci sequence
print(f"The fibonacci sequence is :{fibo()}")