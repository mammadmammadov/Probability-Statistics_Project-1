import matplotlib.pyplot as plt
import numpy as np

average_values = [3.2, 4, 4.8, 3.6, 4.2, 4.4, 3, 4.6, 3.2, 2, 5.2, 3.2, 3.8, 5, 4.2, 4.4, 4.4, 4.4, 3.4, 3.6]

bins = np.linspace(2, 6, 9)

frequency_averages, _ = np.histogram(average_values, bins=bins)


probability_averages = frequency_averages / len(average_values)

fig, ax = plt.subplots()
ax.bar(bins[:-1], probability_averages, width=1, align='edge', label='Average Values')
ax.set_title('Histogram of Average Values')
ax.set_xlabel('Value')
ax.set_ylabel('Probability')
ax.legend()
plt.show()
