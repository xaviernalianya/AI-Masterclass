#Filtering and Transforming Data
import pandas as pd
df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD"],
    "water_glasses":[7, 8, 6, 9, 8, 7],
})

# Members from Nairobi or Mombasa
#.isin() checks if a column's value is in a list
nbi_msa = df[df["city"].isin(["Nairobi", "Mombasa"])]
print("Nairobi and Mombasa members:")
print(nbi_msa[["name", "city", "steps"]].to_string())
#adding a new column
df["steps_hit"]= df["steps"] >= 10000
df["steps_goal"]=df["steps"]-10000
df["hydration"] = df["water_glasses"].apply(lambda x: "Good" if x >= 8 else "Low")
print(df)