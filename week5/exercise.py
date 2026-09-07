data = {
    "user": "Amerix",
    "followers": 1200000,
    "last_post": {
        "title": "Cold shower protocol",
        "likes": 4800
    }
}
print(f"Followers: {data['followers']}")
print(f"Last post likes: {data['last_post']['likes']}")

#A welding contractor's script fetches steel prices from a supplier API. Using the response below, calculate and print the cost of 3 mild steel sheets and 6 metres of angle iron, then print the total. Your output must match exactly:

#Mild steel sheets (3): KES 13500
#Angle iron (6m): KES 16800
#Total: KES 30300

# Paste the data dict above and calculate the costs

data = {
    "supplier": "Nairobi Steel Ltd",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800
    }
}
mild_steel_cost = data['prices']['mild_steel_sheet'] * 3
angle_iron_cost = data['prices']['angle_iron'] * 6
total_cost = mild_steel_cost + angle_iron_cost

print(f"Mild steel sheets (3): KES {mild_steel_cost}")
print(f"Angle iron (6m): KES {angle_iron_cost}")
print(f"Total: KES {total_cost}")

#A ride-hailing app returns a driver's completed trips for the day. Loop through the trips, count them, add up the fares, and find the highest-paying trip. Your output must match exactly:

#Total trips: 5
#Total earned: KES 3420
#Highest trip: South B to Karen | KES 980

data = {
    "driver": "Kamau Njoroge",
    "date": "2026-08-13",
    "trips": [
        {"route": "Westlands to CBD",     "fare_kes": 560},
        {"route": "CBD to South B",       "fare_kes": 420},
        {"route": "South B to Karen",     "fare_kes": 980},
        {"route": "Karen to Westlands",   "fare_kes": 720},
        {"route": "Westlands to Airport", "fare_kes": 740},
    ]
}
total_trips = len(data['trips'])
total_earned = sum(trip['fare_kes'] for trip in data['trips'])
highest_trip = max(data['trips'], key=lambda trip: trip['fare_kes'])

print(f"Total trips: {total_trips}")
print(f"Total earned: KES {total_earned}")
print(f"Highest trip: {highest_trip['route']} | KES {highest_trip['fare_kes']}")