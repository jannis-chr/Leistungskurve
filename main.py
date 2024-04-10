import matplotlib.pyplot as plt
from load_data import load_data


data = load_data('activity.csv')
power_unsorted = data["PowerOriginal"]
n = len(power_unsorted)

x_values = range(n)


# Plot the data
plt.plot(x_values, power_unsorted)

# Add labels and title
plt.xlabel('time in seconds')
plt.ylabel('power in watts')
plt.title('workout')

# Display the plot
plt.grid(True)
plt.savefig('power_graph.png')
plt.show()