
## Name : Unish Bhattarai
## Student ID: 2509860
## Title: Sum of AP and GP from problem 1 and problem 2
## This program calculates the sum of arithmetic progression (AP) from problem 1 and geometric progression (GP) from problem 2 using the built-in sum function in Python.

from Q1 import generate_AP
from Q2 import sequence_generator

def sum_calculation(sequence1, sequence2):
    # Calculate the sum of the arithmetic progression sequence
    sum_ap = sum(sequence1)
    # Calculate the sum of the geometric progression sequence
    sum_gp = sum(sequence2)
    return sum_ap, sum_gp

def main():
    # Get the arithmetic progression sequence from problem 1
    sequence1 = generate_AP()
    # Get the geometric progression sequence from problem 2
    sequence2 = sequence_generator()
    # Calculate the sums of both sequences
    total_ap, total_gp = sum_calculation(sequence1, sequence2)
    # Print the sum of the arithmetic progression sequence
    print("Sum of AP (problem 1) is:", total_ap)
    # Print the sum of the geometric progression sequence
    print("Sum of GP (problem 2) is:", total_gp)

# Call the main function to run the program
main()
