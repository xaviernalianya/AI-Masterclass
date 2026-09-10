#Grouping and Aggregation
import pandas as pd 

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
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