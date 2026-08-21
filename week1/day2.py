#int
steps= 9200
#float
body_weight_kg=70.51
#str
skill_of_the_day="welding"
#bool
cold_shower=True

#outputting the values
print("Steps toady:", steps)
print("Body weight in kg:", body_weight_kg)
print("Skill of the day:", skill_of_the_day)
print("Cold shower:", cold_shower )

#checking for data types
print(type(steps))
print(type(body_weight_kg))
print(type(skill_of_the_day))
print(type(cold_shower))

#alternative way of outputting the values
print(f"My body weight in Kg is {body_weight_kg}")

#variable reassignments
steps=7200
print (f"Morning count: {steps}")

steps=9400
print (f"Evening count: {steps}")

steps= steps+600
print (f"Total steps today: {steps}")