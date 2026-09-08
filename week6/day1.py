
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data)
print("Shape (rows, cols):", df.shape)
print("\nColumns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nFirst 3 rows:")
print(df.head(3).to_string())
print(df["steps"])
print("\nRows 0 to 2 (iloc[0:3]):")
print(df.iloc[0:3].to_string())

print("\nLast row (iloc[-1]):")
print(df.iloc[-1])



print("Statistics for all numeric columns:")
print(df.describe())
df2=pd.read_csv("SME Inspection.csv")
print(df2.head())
print(df2.describe())
print(df2.info())