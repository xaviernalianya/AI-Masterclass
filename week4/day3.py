# Writing JSON to a file (use in VS Code):
#with open("log.json", "w") as f:
 #   json.dump(daily_log, f, indent=2) adds line breaks and indentation to make the output readable. Use it when printing JSON for humans. Leave it out when sending data to an API.

# Reading JSON from a file (use in VS Code):
#with open("log.json", "r") as f:
 #   data = json.load(f) 

import json

#simulate writing
daily_log={
    "steps":9000,
    "protocaol":"OMAD",
    "cold_shower":True,
    "glasses":7.5,
}
json_string=json.dumps(daily_log, indent=2)
print(json_string)

#simulating reading back
loaded_data=json.loads(json_string)
for key, value in loaded_data.items():
    print(f"{key}:{value}")

import json

# Simulated API response with nested data
api_json = '''
{
  "client": "James Omondi",
  "week": 1,
  "daily_logs": [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 7600,  "protocol": "OMAD"},
    {"day": "Saturday",    "steps": 7600,  "protocol": "OMAD"}
  ]
}
'''

data = json.loads(api_json)

print("Client:", data["client"])
print("Week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "low"
    print(f"  {log['day']}: {log['steps']} steps ({status})")


#JSON and Error Handling
#Always wrap JSON parsing in a try-except block.
# If the JSON string is malformed, Python raises a json.JSONDecodeError.

responses = [
    '{"steps": 9200, "protocol": "OMAD"}',
    'not valid json at all',
    '{"steps": 10500, "protocol": "2MAD"}'
]

for r in responses:
    try:
        data = json.loads(r)
        print(f"Parsed OK: {data['steps']} steps")
    except json.JSONDecodeError:
        print(f"Invalid JSON: {r[:30]}...")

        #Exercise
#Create a Python dictionary called week_report that contains your name, 
# a list of 5 daily step counts, and
#  the fasting protocols used each day. 
# Convert it to a JSON string and print it.
#  Then load it back and compute the average steps from the list inside the JSON.

weekly_report={
    "name":"Xavier Nalianya",
    "steps":[8000,9000,10000,10500,9400],
    "protocol":["OMAD","2OMAD","OMAD","Autopagy","OMAD"]
    }
json_string=json.dumps(weekly_report, indent=2)
print("JSON String",json_string)
loaded_data=json.loads(json_string)
avg=sum(loaded_data["steps"])/len(loaded_data["steps"])
print(f"\n Average steps:{loaded_data["name"]}: {avg}")
