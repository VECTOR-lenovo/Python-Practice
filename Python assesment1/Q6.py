## Name : Unish Bhattarai
## Student ID: 2509860
## Title: Pascal triangle generator
## This program generates Pascal's triangle up to a specified number of rows using a list of lists in Python.

def generate_pascals_triangle(rows):
    # Create an empty list to store the triangle
    triangle = []
    # Loop through each row
    for i in range(rows):
        # Start each row with a 1
        row = [1]
        # Loop through the positions in the row to calculate values
        for j in range(1, i):
            # Calculate the value by adding the two numbers above it
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with a 1 if it's not the first row
        if i > 0:
            row.append(1)
        # Add the row to the triangle
        triangle.append(row)
    # Return the complete triangle
    return triangle

# Generate Pascal's triangle with 10 rows
pascals_triangle = generate_pascals_triangle(10)
# Print each row of the triangle
for row in pascals_triangle:
    print(row)