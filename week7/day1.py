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