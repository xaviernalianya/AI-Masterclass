#Exercise
#You have a list of weekly step counts for four different people. 
# Use list comprehensions to:
#  (1) build a list of all step counts that are above 10,000 from any person, and
#  (2) build a list of names of people whose average steps for the week is above 9,000.


people=[
    {"name":"James","steps":[7000,9000,7600,1200,8000,8700,9900]},
    {"name":"John","steps":[8877,2829,9884,6783,7878,6457,9000]},
    {"name":"Martha","steps":[9000,8000,7000,6000,11000,4000,8990]},
    {"name":"Tomas","steps":[8877,2829,9884,6783,7878,6457,9000]},
    {"name":"Xavy","steps":[9000,8000,7000,6000,11000,4000,8990]},
]

# 1 Building step counts above 10,000
all_steps = [s for p in people for s in p["steps"]]
high_steps = [s for s in all_steps if s > 10000]
print("Steps above 10,000:", high_steps)

# 2 Building names of people whose weekly average is above 9,000
names_above_average = [
    p["name"] for p in people
    if sum(p["steps"]) / len(p["steps"]) > 7000
]
print("People averaging above 9,000 steps:", names_above_average)