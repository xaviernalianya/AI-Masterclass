#A construction contractor wants to know if a project will finish on time. 
# Write a function called predict_delivery_risk that takes three parameters:
#  crew_size, days_remaining, and tasks_left. 
# Apply this logic:

#Calculate efficiency = tasks_left / (crew_size * days_remaining)
#If efficiency is above 1.5: return "High risk"
#If efficiency is above 0.8: return "Medium risk"
# Otherwise: return "Low risk"
#Call it three times and print each result. Your output must match exactly:

def predict_delivery_risk(crew_size, days_remaining, tasks_left):
    efficiency = tasks_left / (crew_size * days_remaining)
    if efficiency > 1.5:
        return "High risk"
    elif efficiency > 0.8:
        return "Medium risk"
    else:
        return "Low risk"
print(predict_delivery_risk(3, 5, 25))
print(predict_delivery_risk(4, 10, 18))
print(predict_delivery_risk(2, 4, 8))

#Code Challenge 2 — The Simp Detector
'''A man has been trying to impress a woman for weeks. 
He tracked his spending, how many texts he sent, how many she replied to, 
how many times he asked her out, and how many times she said yes.

Write a function called simp_alert that takes five parameters: money_spent, texts_sent, texts_replied, dates_asked, dates_accepted. Apply this logic:

Calculate reply_rate = texts_replied / texts_sent
Calculate date_rate = dates_accepted / dates_asked
Calculate score = (reply_rate + date_rate) / 2
If score is 0.5 or above: return "She likes you"
If score is 0.2 or above: return "Lukewarm"
Otherwise: return "You are simping"
Call it three times and print each result. Your output must match exactly:

You are simping
She likes you
Lukewarm'''

def simp_alert(money_spent, texts_sent, texts_replied, dates_asked, dates_accepted):
    reply_rate= texts_replied / texts_sent
    date_rate= dates_accepted / dates_asked
    score= (reply_rate + date_rate) / 2
    if score >= 0.5:
        return "She likes you"
    elif score >= 0.2:
        return "Lukewarm"
    else:
        return "You are simping"

print(simp_alert(45000, 80, 2, 10, 0))
print(simp_alert(8000, 20, 15, 4, 2))
print(simp_alert(18000, 20, 6, 5 ,1))