#Step 1
#Load 28 days of data. Inspect shape, data types, and check for missing values before doing any analysis.
import pandas as pd
import numpy as np

data= {
    "day":      list(range(1, 29)),
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200,
                 8900, 10800, 9100, 11200, 7900, 10000, 9700,
                 9500, 10300, 8600, 11500, 8200, 9800, 10600,
                 9000, 10100, 8400, 10900, 7500, 9600, 10400],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0,
                 6.0, 8.5, 7.0, 7.5, 9.0, 7.0, 7.5,
                 7.0, 8.0, 6.5, 7.5, 8.0, 7.0, 8.5,
                 7.0, 7.5, 6.5, 8.0, 9.5, 7.0, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8, 6, 9, 8, 8, 7, 9, 8,
                 7, 8, 6, 9, 8, 7, 9, 8, 8, 6, 9, 7, 8, 9],
    "protocol": (["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"] * 4),
    "cold_shower": ([True, True, False, True, True, True, True,
                     False, True, True, True, True, False, True] * 2),
    "bench_kg": [80, 82, 78, 85, 80, 83, 84,
                 81, 85, 80, 86, 79, 84, 83,
                 82, 86, 79, 88, 81, 85, 87,
                 82, 86, 80, 87, 79, 84, 86],
}
df=pd.DataFrame(data)
print(df.head(10))
print(f"Shape: {df.shape}")
print(f"Data types:\n{df.dtypes}")
print(f"Missing Values: {df.isna().sum().sum()}")

#Step 2: Filter and Analyze
#Filter for high-performance days. Group by protocol. Compute key statistics.
# High-performance days: 10k+ steps AND 7.5+ hours sleep
high_perf=df[(df["steps"]>=10000) & (df["sleep_hr"]>=7.5)]
print(f"High-performance days:\n{high_perf}")
print(f"Number of high-performance days: {len(high_perf)}/28")

#protocol comparison
df_group=df.groupby("protocol").agg(
    steps_mean=("steps", "mean"),
    sleep_hr_mean=("sleep_hr", "mean"),
    water_mean=("water", "mean"),
    days=("day", "count"),
).round(1)
print(f"\n Protocol Stats: {df_group}")

