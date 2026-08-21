#Write a function called generate_week() 
# that uses random to simulate a week of step counts (7 days, each between 6000 and 12000 steps). 
# The function should print each day's count, 
# calculate the average using math.floor() to round it down, and
#  print how many days were at or above 8000 steps.

import random
import math

def generate_week():
    day=["Monday","Tuesday","Wednesday","Thursday", "Friday","Saturday","Sunday"]
    total=0
    goal_days=0

    for d in day:
        steps=random.randint(6000,12000)
        total+=steps
        if steps>=8000:
            goal_days +=1
        print(f"{d}:{steps} steps")

    avg=math.floor(total/7)
    print(f"\n Average Steps:{avg}")
    print("Days on Goal:", goal_days/7)
generate_week()
