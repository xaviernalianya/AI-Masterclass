weekly_steps=[9200,10500,8800,11000,7600,9400,10200]

print("Weekly steps:", weekly_steps)
print("Days Tracked", len(weekly_steps))
print(f"Monday's steps: {weekly_steps[0]} and Saturday's steps: {weekly_steps[-2]}")


for steps in weekly_steps:
    if steps > 10000:
        print(f"Great job! You walked {steps} steps today!")
    else:
        print(f"You walked {steps} steps today. Keep going!")

   