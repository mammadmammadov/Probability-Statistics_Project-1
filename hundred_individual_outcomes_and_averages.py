import matplotlib.pyplot as plt
import numpy as np

individual_outcomes = [1, 2, 6, 1, 2, 6, 4, 4, 4, 6, 1, 6, 1, 2, 4, 3, 6, 5, 5, 4,
                       5, 3, 5, 2, 5, 2, 3, 6, 5, 2, 6, 5, 6, 5, 6, 2, 3, 3, 2, 6,
                       4, 3, 3, 2, 3, 6, 4, 5, 6, 1, 2, 3, 2, 1, 2, 6, 6, 6, 1, 1, 3,
                       1, 3, 2, 5, 1, 3, 6, 6, 6, 3, 6, 4, 5, 2, 3, 3, 3, 4, 2, 6, 4,
                       5, 1, 4, 2, 3, 2, 3, 1, 1, 5, 4, 5, 4, 6, 2, 5, 4, 5]

frequency_individual_outcomes = [individual_outcomes.count(i) for i in range(1, 7)]

probability_individual_outcomes = [f / len(individual_outcomes) for f in frequency_individual_outcomes]


average_values = [3.2, 4, 4.8, 3.6, 4.2, 4.4, 3, 4.6, 3.2, 2, 5.2, 3.2, 3.8, 5, 4.2, 4.4, 4.4, 4.4, 3.4, 3.6]

bins = np.arange(2, 7)
frequency_averages, _ = np.histogram(average_values, bins=bins)

probability_averages = frequency_averages / len(average_values)

fig, ax = plt.subplots()
ax.bar(range(1, 7), probability_individual_outcomes, label='Individual Values')
ax.bar(bins[:-1], probability_averages, width=0.5, align='edge', label='Average Values')

ax.set_title('Histogram of Individual and Average Values')
ax.set_xlabel('Value')
ax.set_ylabel('Probability')

ax.legend()
plt.show()
