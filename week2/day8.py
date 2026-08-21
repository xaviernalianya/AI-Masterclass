#Start with this list of step counts: [8800, 6500, 11000, 9200, 7300].
#  Do the following steps in order: 
# add 10500 to the end,
#  remove 6500, 
# sort the list from highest to lowest, then 
# print the final list and 
# print how many days exceeded 9000 steps

steps=[8800, 6500, 11000, 9200, 7300]
steps.append(10500)
steps.remove(6500)
steps.sort(reverse=True)
print(steps)
#count over 9000 steps
high_steps=0
for step in steps:
    if step > 9000:
        high_steps += 1
print(f"Number of days with over 9000 steps: {high_steps}")