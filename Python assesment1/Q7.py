## Name : Unish Bhattarai
## Student ID: 2509860
## Title: Graphs of f(x) = 3x^2 and f(x) = 4x - 3
## This program plots the graphs of two mathematical functions, ( f(x) = 3x^2 ) and ( f(x) = 4x - 3 ), using the matplotlib library in Python.

import matplotlib.pyplot as plt

def plot_graph():
    # Lists to store x values and corresponding y values for both functions
    value_x = []
    value_y1 = []
    value_y2 = []

    # Calculate y values for each x from -5 to 15
    for x in range(-5, 16):
        value_x.append(x)
        y1 = 3 * (x ** 2)  # Calculate y for f(x) = 3x^2
        y2 = 4 * x - 3     # Calculate y for f(x) = 4x - 3
        value_y1.append(y1)
        value_y2.append(y2)

    # Plot the graph for f(x) = 3x^2
    plt.plot(value_x, value_y1, label='f(x) = 3x^2', color='blue')
    # Plot the graph for f(x) = 4x - 3
    plt.plot(value_x, value_y2, label='f(x) = 4x - 3', color='red')

    # Add labels and title to the graph
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphs of f(x) = 3x^2 and f(x) = 4x - 3')

    # Add legend and grid to the graph
    plt.legend()
    plt.grid()

    # Display the graph
    plt.show()

# Call the function to plot the graph
plot_graph()