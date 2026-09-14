import pandas as pd
jobs = [
    {"client": "Kamau", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "boxes_used": 60, "price_per_box": 2200},
]
df=pd.DataFrame(jobs)
total_boxes=df["boxes_used"].sum()
revenue=(df["boxes_used"]*df["price_per_box"]).sum()
print(f"Total: {total_boxes}")
print(f"Revenue: {revenue}")

# using a for loop
jobs = [
    {"client": "Kamau", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "boxes_used": 60, "price_per_box": 2200},
]
total_boxes=0
total_revenue=0
for job in jobs:
 total_boxes +=job["boxes_used"]
 total_revenue +=job["boxes_used"]*job["price_per_box"]

print(f"Total: {total_boxes}")
print(f"Revenue: {revenue}")


import pandas as pd

patients = [
    {"name": "Alice",  "bp": 155, "glucose": 130, "creatinine": 0.9},
    {"name": "Brian",  "bp": 120, "glucose": 118, "creatinine": 1.5},
    {"name": "Carol",  "bp": 148, "glucose": 142, "creatinine": 1.0},
    {"name": "David",  "bp": 130, "glucose": 110, "creatinine": 0.8},
    {"name": "Eve",    "bp": 160, "glucose": 98,  "creatinine": 1.1},
    {"name": "Frank",  "bp": 125, "glucose": 115, "creatinine": 0.7},
]
df = pd.DataFrame(patients)
hypertension=df["bp"]>= 140
diabetes=df["glucose"]>=126
kidney=df["creatinine"]>=1.2
print(f"Hypertension risk: {hypertension.sum()}")
print(f"Diabetes risk: {diabetes.sum()}")
print(f"Kidney risk: {kidney.sum()}")