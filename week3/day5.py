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
weight= 84
height= 1.74
bmi= calculate_bmi(weight, height)
print(f"BMI: {bmi}")
print(f"Category: {bmi_category(bmi)}")

