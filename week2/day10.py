week_log=[{"day":"Monday", "steps":9200, "water_glasses":8, "cold_shower":True, "fasting_protocol":"OMAD", "sleep_hours":7.5},
          {"day":"Tuesday", "steps":12000, "water_glasses":10, "cold_shower":False, "fasting_protocol":"5:2", "sleep_hours":6.0},
          {"day":"Wednesday", "steps":8000, "water_glasses":7, "cold_shower":True, "fasting_protocol":"16:8", "sleep_hours":8.0},
          {"day":"Thursday", "steps":15000, "water_glasses":9,  "cold_shower":False, "fasting_protocol":"OMAD", "sleep_hours":7.0},
          {"day":"Friday", "steps":11000, "water_glasses":8, "cold_shower":True, "fasting_protocol":"5:2", "sleep_hours":6.5},
          {"day":"Saturday", "steps":7000, "water_glasses":6, "cold_shower":False, "fasting_protocol":"16:8", "sleep_hours":9.0},
          {"day":"Sunday", "steps":13000, "water_glasses":10, "cold_shower":True, "fasting_protocol":"OMAD", "sleep_hours":7.5}]
#print(week_log)
week_log[0]["steps"]
print("Steps on Monday:", week_log[0]["steps"])
for log in week_log:
    if log["steps"] > 10000:
        print(f"Steps goal hit {log['day']}: {log['steps']}")
    else:
        print(f"Steps goal not hit {log['day']}: {log['steps']}")   

week_summary={
    "week": 1,
    "steps":[9200, 12000, 8000, 15000, 11000, 7000, 13000],
    "protocol":["OMAD","2OMAD","Autopagy","OMAD","5:2","16:8","OMAD"],

}
print("Week one", week_summary["week"])