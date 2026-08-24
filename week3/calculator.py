import math
from datetime import date

# ---- DATA ----
client_name  = "James"
weight_kg    = 84
height_m     = 1.78
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
protocols    = ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"]
step_goal    = 8000

# ---- FUNCTIONS ----
def calculate_bmi(w, h):
    return round(w / (h**2), 1)

def bmi_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif bmi < 25: return "Normal weight"
    elif bmi < 30: return "Overweight"
    else: return "Obese"

def weekly_step_summary(steps, goal=8000):
    return {
        "days_on_goal": len([s for s in steps if s >= goal]),
        "average": round(sum(steps) / len(steps)),
        "best": max(steps),
        "worst": min(steps)
    }

def estimate_calories(steps, rate=0.04):
    return math.floor(steps * rate)

def protocol_summary(plist):
    return {p: plist.count(p) for p in set(plist)}

# ---- REPORT ----
today = date.today().strftime("%d %B %Y")
bmi = calculate_bmi(weight_kg, height_m)
steps_report = weekly_step_summary(weekly_steps, step_goal)
total_cals = sum(estimate_calories(s) for s in weekly_steps)
proto_report = protocol_summary(protocols)

print("=" * 42)
print(f"  WEEKLY REPORT: {client_name.upper()}")
print(f"  Date: {today}")
print("=" * 42)
print(f"\nBODY")
print(f"  Weight : {weight_kg} kg")
print(f"  BMI    : {bmi} ({bmi_category(bmi)})")
print(f"\nSTEPS (Goal: {step_goal})")
print(f"  Days on goal : {steps_report['days_on_goal']}/7")
print(f"  Average      : {steps_report['average']} steps/day")
print(f"  Best day     : {steps_report['best']} steps")
print(f"  Worst day    : {steps_report['worst']} steps")
print(f"  Cals burned  : ~{total_cals} kcal")
print(f"\nPROTOCOL BREAKDOWN")
for p, d in proto_report.items():
    print(f"  {p}: {d} day(s)")
print("\n" + "=" * 42)