#Grouping and Aggregation
import pandas as pd 

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, None, 7600, 9400, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Group by protocol and calculate the average steps a.nd sleep hours
grouped=df.groupby("protocol")["steps"].mean().round(2)
print(grouped)
sum=df.groupby("protocol")["steps"].sum().round(2)
print(sum)
aggregate=df.groupby("day")["steps"].agg(["min", "max", "mean","count"]).round(2)
print(aggregate)
breakdown=df.groupby(["day","protocol"])["steps"].agg(["min", "max", "mean","count"]).round(2)
print(breakdown)

#use of value counts
print(df["protocol"].value_counts())

#Handling missing values
print("Rows with Missing Values:")
print(df[df.isna().any(axis=1)].to_string())

#filling missing values with mean
df["steps"]=df["steps"].fillna(df["steps"].mean())
df["sleep_hr"]=df["sleep_hr"].fillna(df["sleep_hr"].mean())
print("DataFrame after filling missing values:")
print(df.to_string())