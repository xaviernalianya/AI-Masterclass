'''Write a function called service_offer that takes three parameters:
 skill, price, and delivery. 
 It should return a formatted string in this exact format:

Service: [skill] | Price: KES [price] | Delivery: [delivery] days
Call it twice and print each result. Your output must match exactly:

Service: Python Automation | Price: KES 15000 | Delivery: 3 days
Service: Data Report | Price: KES 8000 | Delivery: 2 days
Calls to use: service_offer("Python Automation", 15000, 3) and service_offer("Data Report", 8000, 2)'''

def service_offer(skill, price, delivery):
    return f"Service: {skill} | Price: KES {price} | Delivery: {delivery} days"

print(service_offer("Python Automation", 15000, 3))
print(service_offer("Data Report", 8000, 2))