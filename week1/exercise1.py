#Create a file called day3.py. You are a personal trainer tracking a client's workout. Write a program that stores the following data and calculates a full session report:

#Number of exercises: 6
#Sets per exercise: 4
#Reps per set: 10
#Average weight per rep: 60 kg
#Session duration in minutes: 45
#Calculate and print: total sets, total reps, total volume (kg lifted), reps per minute, and whether total volume exceeded 10,000 kg.

#Xavier's Workout Report\
#Variables
exercises=6
sets_per_exercise=4
reps_per_set=10
weight_per_rep=60
duration_per_rep=45

#computations
total_sets=exercises*sets_per_exercise
print(f"Today's total sets were: {total_sets}")

total_reps=total_sets*reps_per_set
print(f"Today's total reps were: {total_reps}")

total_volume=total_reps*weight_per_rep
print(f"Todays total volume lifted was: {total_volume} kg") 

reps_per_minute=total_reps/duration_per_rep
print(f"Today's reps per minute were: {reps_per_minute}")

print(f"Did Xavier exceed 10,000 kg lifted? {total_volume>10000}")
