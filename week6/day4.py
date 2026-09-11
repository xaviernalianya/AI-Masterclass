import numpy as np


steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("First 3 days:", steps[:3])
print("Last 2 days:", steps[-2:])
print("Weekdays (Mon-Fri):", steps[:5])
print("Weekend:", steps[5:])

print()
# Best week start: first day above 10k
first_10k = np.argmax(steps >= 10000)   # index of first True
print(f"First 10k+ day: {days[first_10k]} with {steps[first_10k]:,} steps")

# Sort and show progression
sorted_steps = np.sort(steps)
print("Steps sorted low to high:", sorted_steps)

