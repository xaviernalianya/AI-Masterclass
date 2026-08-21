morning_steps=4200
afternoon_steps= 5000

#addition
total_steps= morning_steps + afternoon_steps
print(f"Total Steps Today:{total_steps}")

#subtraction
steps_remaining= 10000 - total_steps
print(f"Steps remaining to reach 10,000 steps: {steps_remaining}")

#multiplication
weekly_target=8000 * 7
print(f"Weekly target steps: {weekly_target}")

#division
daily_average= 65000 / 7
print(f"Daily average steps: {daily_average}")

#interger division, modulo and exponentiation
total_steps= 65000
days= 7

#clean whole number division(no decimal)
daily_average= total_steps //days
print(f"Daily average steps (whole number): {daily_average}")

#power: how many steps in two weeks squared
print(f"Steps in two weeks squared: {total_steps ** 2}")

#BUILDING A WEEKLY TRAINING REPORT
bench_press_sets= 5
reps_per_set= 12
weight_per_rep= 80

total_reps= bench_press_sets * reps_per_set
total_volume_kg=total_reps * weight_per_rep
reps_per_minute= total_reps / 4 #assuming it took 4 minutes to complete the sets

print("--BENCH PRESS REPORT--")
print(f"Sets: {bench_press_sets}")
print(f"Reps per Set: {reps_per_set}")
print(f"Total Reps: {total_reps}")
print(f"Weight per rep (kg): {total_volume_kg}")
print(f"Reps per Minute: {reps_per_minute}")

#COMPARISON OPERATOR
steps= 9200
water_glasses= 8
sleep_hours= 7
fasting="OMAD"

print(steps >=10000)
print(water_glasses == 8)
print(sleep_hours <=8 )
print(fasting != "None")

