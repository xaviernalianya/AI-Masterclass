#Single and Batch Predictions

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],[6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],[7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],[7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])
y = (steps >= 10000).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X_train, y_train)

# Single prediction (must still be 2D)
single_day = np.array([[8.0, 8, 84]])  # 8hr sleep, 8 water, 84kg bench
pred = clf.predict(single_day)[0]
label = "Goal hit" if pred == 1 else "Below goal"
print(f"Single prediction: {label}")

# Batch predictions
new_days = np.array([
    [8.0, 8, 84],   # good sleep, good hydration
    [6.0, 5, 78],   # poor sleep, low water
    [9.0, 9, 87],   # excellent sleep and hydration
    [7.0, 7, 82],   # average day
    [6.5, 6, 79],   # rough day
])

preds = clf.predict(new_days)
print("\nBatch predictions:")
for inputs, pred in zip(new_days, preds):
    label = "Goal hit" if pred == 1 else "Below goal"
    print(f"  sleep={inputs[0]}h water={int(inputs[1])} bench={int(inputs[2])}kg => {label}")


#Probability Scores
probas = clf.predict_proba(new_days)
print("Prediction with confidence:")
for inputs, proba in zip(new_days, probas):
    prob_hit = proba[1]  # probability of class 1 (hit goal)
    label = "Goal hit" if prob_hit >= 0.5 else "Below goal"
    confidence = max(proba) * 100
    print(f"  sleep={inputs[0]}h water={int(inputs[1])} bench={int(inputs[2])}kg")
    print(f"    => {label}  (confidence: {confidence:.0f}%)")