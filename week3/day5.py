#Modular Calculator
#Calculator 1 BMI

import math

def calculate_bmi(weight_kg, height_m):
    bmi= weight_kg/ (height_m**2)
    return round(bmi, 1)
def bmi_category(bmi):
    if bmi <18.5:
        return"underweight"
    elif bmi <25:
        return "Normal Weight"
    elif bmi <30:
        return "Overweight"
    else:
        return "Obese"


#Test
weight= 84.9
height= 1.74
bmi= calculate_bmi(weight, height)
print(f"BMI: {bmi}")
print(f"Category: {bmi_category(bmi)}") 

#Function 2
#Takes a list of daily step counts and an optional goal (default 8,000).
#  Returns a summary of the week.

def weekly_step_summary(steps_list, goal=8000):
    days_hit = len([s for s in steps_list if s >= goal])
    average = sum(steps_list) / len(steps_list)
    best = max(steps_list)
    worst = min(steps_list)

    return {
        "days_on_goal": days_hit,
        "total_days": len(steps_list),
        "average": round(average),
        "best_day": best,
        "worst_day": worst
    }

weekly = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
result = weekly_step_summary(weekly)

print("Step Summary:")
print(f"  Days on goal : {result['days_on_goal']}/{result['total_days']}")
print(f"  Average      : {result['average']} steps")
print(f"  Best day     : {result['best_day']} steps")
print(f"  Worst day    : {result['worst_day']} steps")