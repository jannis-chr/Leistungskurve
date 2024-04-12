import os
import matplotlib.pyplot as plt
from load_data import load_data


data = load_data('activity.csv')
power_unsorted = data["PowerOriginal"]
n = len(power_unsorted)

x_values = range(n)


# plot the data
plt.plot(x_values, power_unsorted)

# add labels and title
plt.xlabel('time in seconds')
plt.ylabel('power in watts')
plt.title('workout')

# display the plot
plt.grid(True)
plt.savefig('power_graph.png')

# create folder "figures"
figures_folder = 'figures'
if not os.path.exists(figures_folder):
    os.makedirs(figures_folder)

# Save the picture
plt.savefig(os.path.join(figures_folder, 'power_graph.png'))



plt.show()