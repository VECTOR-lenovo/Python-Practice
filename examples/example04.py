import matplotlib.pyplot as plt
x=[2, 3, 4, 5]
y=[3, 4, 5, 6]
plt.plot(x, y, marker='o', color='blue',label='line 1', linewidth=3)
plt.plot(x, marker='+', color='green',label='line 2', linewidth=2)
#function to add title
plt.title('Example 4')
#Function to label axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
# Function to add a legend
plt.legend()
# function for the visibility of grid
plt.grid()
plt.show()

# output: There are two parallel lines that passes through the given points