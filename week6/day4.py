import numpy as np
import pandas as pd

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


df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "bench_press_kg": [100, 110, 90, 120, 80, 105, 115]
})

# Pull a column as a NumPy array
steps_arr = df["steps"].to_numpy()
bench_arr=df["bench_press_kg"].to_numpy()
print("NumPy array from pandas column:", steps_arr)
print("Type:", type(steps_arr))

# Use NumPy on it
print(f"\nMean:    {np.mean(steps_arr):,.0f}")
print(f"Std dev: {np.std(steps_arr):,.0f}")
print(f"corr: {np.corrcoef(steps_arr, bench_arr)[0, 1]:.3f}")
# Add a normalized column back to the DataFrame
# Normalize to 0-1 range (min-max scaling)
df["steps_norm"] = (df["steps"] - df["steps"].min()) / (df["steps"].max() - df["steps"].min())
df["steps_norm"] = df["steps_norm"].round(3)
print("\nWith normalized steps:")
print(df[["day", "steps", "steps_norm"]].to_string())