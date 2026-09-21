#ML using scikit-learn
import sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Data (28 days of SMP fitness log)
# Features: sleep hours, water glasses
# Label: steps taken that day
X = np.array([
    [7.5, 7], [8.0, 8], [6.5, 6], [7.0, 9], [9.0, 8], [7.5, 7], [8.0, 8],
    [6.0, 6], [8.5, 9], [7.0, 8], [7.5, 8], [9.0, 7], [7.0, 9], [7.5, 8],
    [7.0, 7], [8.0, 8], [6.5, 6], [7.5, 9], [8.0, 8], [7.0, 7], [8.5, 9],
    [7.0, 8], [7.5, 8], [6.5, 6], [8.0, 9], [9.5, 7], [7.0, 8], [8.0, 9]
])  # shape: (28, 2) - 28 days, 2 features each

y = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])  # shape: (28,) - one step count per day

print(f"Features shape: {X.shape}")
print(f"Labels shape:   {y.shape}")

# Step 2: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTraining rows: {X_train.shape[0]}")
print(f"Test rows:     {X_test.shape[0]}")

# Step 3: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Evaluate
score = model.score(X_test, y_test)
print(f"\nModel R2 score: {score:.3f}")
print("(1.0 = perfect, 0 = no better than guessing the mean)")

#Making Predictions
import sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7],[8.0,8],[6.5,6],[7.0,9],[9.0,8],[7.5,7],[8.0,8],[6.0,6],[8.5,9],[7.0,8],[7.5,8],[9.0,7],[7.0,9],[7.5,8],[7.0,7],[8.0,8],[6.5,6],[7.5,9],[8.0,8],[7.0,7],[8.5,9],[7.0,8],[7.5,8],[6.5,6],[8.0,9],[9.5,7],[7.0,8],[8.0,9]])
y = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Predict for new days not in the training data
new_days = np.array([
    [8.0, 8],   # 8 hours sleep, 8 glasses water
    [6.0, 5],   # 6 hours sleep, 5 glasses water
    [9.0, 9],   # 9 hours sleep, 9 glasses water
    [7.5, 7],   # typical day
])

predictions = model.predict(new_days)
print("Predictions for new days:")
for i, (inputs, pred) in enumerate(zip(new_days, predictions)):
    sleep, water = inputs
    print(f"  Sleep={sleep}h, Water={water}g => predicted steps: {pred:,.0f}")



#predicting categories
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([[7.5,7],[8.0,8],[6.5,6],[7.0,9],[9.0,8],[7.5,7],[8.0,8],[6.0,6],[8.5,9],[7.0,8],[7.5,8],[9.0,7],[7.0,9],[7.5,8],[7.0,7],[8.0,8],[6.5,6],[7.5,9],[8.0,8],[7.0,7],[8.5,9],[7.0,8],[7.5,8],[6.5,6],[8.0,9],[9.5,7],[7.0,8],[8.0,9]])
steps = np.array([9200,10500,8800,11000,7600,9400,10200,8900,10800,9100,11200,7900,10000,9700,9500,10300,8600,11500,8200,9800,10600,9000,10100,8400,10900,7500,9600,10400])

# Convert step counts to binary labels: 1 = hit goal, 0 = missed
y = (steps >= 10000).astype(int)
print("Label distribution (1=hit goal, 0=missed):")
print(f"  Hit goal:  {y.sum()}/28 days")
print(f"  Missed:    {(y==0).sum()}/28 days")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(f"\nClassification accuracy: {accuracy:.0%}")

# Predict new days
new_days = np.array([[8.0, 8], [6.0, 5], [9.0, 9]])
preds = clf.predict(new_days)
labels = {1: "Goal hit", 0: "Below goal"}
print("\nPredictions for new days:")
for inputs, pred in zip(new_days, preds):
    print(f"  Sleep={inputs[0]}h, Water={int(inputs[1])}g => {labels[pred]}")

