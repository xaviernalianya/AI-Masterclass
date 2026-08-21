#Dictionaries: Key-Value Data


daily_log={
    "steps":9200,
    "water_glasses":8,
    "cold_shower":True,
    "fasting_protocol":"OMAD",
    "sleep_hours":7.5,
}
print(daily_log)
print("Steps Today:", daily_log["steps"])
print(f"Water Glasses Today: {daily_log['water_glasses']}")
print(f"Cold Shower Today: {daily_log['cold_shower']}")
print(f"Fasting Protocol Today: {daily_log['fasting_protocol']}")
print(f"Sleep Hours Today: {daily_log['sleep_hours']}") 

#adding a new key-value pair to the dictionary
daily_log["pages_read"]=15
print(daily_log)
#updating a value in the dictionary
daily_log["steps"]=12000
print(daily_log)
#deleting a key-value pair from the dictionary
del daily_log["cold_shower"]
print(daily_log)
if "cold_shower" in daily_log:
    print("Cold shower was logged today.")
else:
    print("Cold shower was not logged today.")
if daily_log['steps'] > 10000:
    print("You hit your step goal today!")
else:
    print("You did not hit your step goal today.")