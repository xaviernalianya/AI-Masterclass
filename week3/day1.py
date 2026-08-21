#functions

def show_daily_doal():
    print("Steps Goal: 8000 steps ")
    print("Water Goal: 8 glasses ")
    print("Cold Shower: Yes")

#call the function
show_daily_doal()

def check_steps(steps):
    if steps >=10000:
        print(steps,"steps- Goal Exceeded")
    elif steps >=8000:
        print(steps,"steps- Goal Achieved")
    else:
        print(steps,"steps- Goal Not Achieved")

#csll with different values
check_steps(9200)
check_steps(7500)
check_steps(12000)

def log_day(day, steps, protocol):
    print(f"{day}: {steps} steps| Protocol {protocol}")

log_day("Monday", 9200, "OMAD")



#Return: Getting a Value Back
def calculate_average_steps(steps_list):
    total= sum(steps_list)
    average= total/len(steps_list)
    return average

weekly_steps=[9200,5000,10500,8800,11000,7600,9400]
avg=calculate_average_steps(weekly_steps)
print("Average steps", avg)


#Exercise

#Write a function called day_report(steps, water, protocol) that prints a formatted report of a day's discipline data. 
# Then write a second function called hit_goal(steps) that returns True if steps is 8000 or more, and False if not.
# Call both functions with at least three different sets of values.

    
def day_report(steps, water, protocol):
    print("----Daily Report----")
    print("Steps",steps,water," glasses of water","Protocol",protocol)

def hit_goal(steps):
   return steps >=8000
day_report(9200,8,"OMAD")
day_report(10200,9,"Autopagy")
day_report(2000,6,"2OMAD")

print("Goal Hit(9200)", hit_goal(9200))
print("Goal Hit(1200)", hit_goal(1200))
    