import matplotlib.pyplot as plt

# Define the x data points
x = [1, 2, 3, 4, 5]

# Define the y data points for each bike
y = [
    [50, 40, 70, 80, 20],  # Bike 1 distances
    [80, 20, 20, 50, 60],  # Bike 2 distances
    [70, 20, 60, 40, 60],  # Bike 3 distances
    [40, 20, 30, 70, 60],  # Bike 4 distances
    [20, 60, 60, 60, 60]   # Bike 5 distances
]

# Add a title to the plot
plt.title("Bike and distance")

# Add labels to the x and y axes
plt.xlabel("Days")
plt.ylabel("Distance")
plt.figure(figsize=(10,8))
# Plot the data points for each bike with a marker
for i in range(5):
    j=i+1
    plt.subplot(3,2,j,)
    plt.plot(x, y[i])

# Display the plot

plt.show()