import matplotlib.pyplot as plt

# Initialize empty lists to store y data points for three different functions
y1 = []
y2 = []
y3 = []

# Initialize an empty list to store x data points
x = []

# Loop through the range 1 to 20 (inclusive) to generate data points
for a in range(1, 21):
    # Append the current value of a to the x data points list
    x.append(a)

    # Calculate y data points for three different functions
    i1 = 5 * a ** 3 + 2 * a - 1
    i2 = -2 * a ** 3 + a ** 2 + 100
    i3 = 2 * 3.14 + 20

    # Append the calculated y data points to their respective lists
    y1.append(i1)
    y2.append(i2)
    y3.append(i3)

    # Plot the data points for each function with markers
    plt.subplot(2,2,1)
    plt.plot(x, y1)
    plt.subplot(2,2,2)
    plt.plot(x, y2,)
    plt.subplot(2,2,3)
    plt.plot(x, y3)

# Label the x-axis
plt.xlabel('X-axis')

# Label the y-axis
plt.ylabel('Y-axis')

# Display the plot
plt.show()