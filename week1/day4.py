steps=9500
sleep_hours=6
water_glasses=5
cold_shower=False
pages_read=15

if steps>=10000:
    print("Excellent DailySteps target hit above 10000 steps")
elif steps>=9000:
    print("Great job. You have reached your 9000 DailySteps goal")
elif steps ==4500:
    print(f"Halfway there to reach your 9000 DailySteps goal.")
elif steps >4500:
    print(f"Past Halfway there to reach your 9000 DailySteps goal. ")
else:
    print(f"Not quite there to reach your 9000 DailySteps goal. ")

if sleep_hours>=7:
    print("You've had enough sleep")
else:
    print(f"You need more {7-sleep_hours} sleep hours")
if water_glasses>=8:
    print("Good, you have had enought water today")
else:
    print(f"You need {8-water_glasses} more glasses of water today")

if cold_shower==True:
    print("Good, you have taken a cold shower today")
else:
    print(f"You need to take a cold shower today. ")
   
if pages_read>=10:
    print("Good, you have read enough pages today")
else:
    print(f"You need to read {10-pages_read} more pages today")  
   

print("--Daily check complete--")
print(f"Today's steps were: {steps}")
print(f"You have slept {sleep_hours} hours")
print(f"You have had {water_glasses} glasses of water today")
print(f"You have read {pages_read} pages today")
print(f"Did you take a cold shower today? {cold_shower}")

      