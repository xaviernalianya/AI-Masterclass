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
