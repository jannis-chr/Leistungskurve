import matplotlib.pyplot as plt
from load_data import load_data


data = load_data('activity.csv')
power_unsorted = data["PowerOriginal"]
n = len(power_unsorted)

x_values = range(n)


# Plot the data
plt.plot(x_values, power_unsorted)

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Power Number')
plt.title('Plot of Power Numbers')

# Display the plot
plt.grid(True)
plt.show()