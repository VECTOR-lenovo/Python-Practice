import matplotlib.pyplot as plt

# Define the x data points
x = [1, 4, 8, 12]

# Define the y data points
y = [1, 3, 6, 9]

# Plot the data points
plt.plot(x, y)

# Set the x-axis limit from 0 to 50
plt.xlim(0, 50)

# Set the y-axis limit from 0 to 50
plt.ylim(0, 50)

# Add a grid to the plot
plt.grid()

# Display the plot
plt.show()