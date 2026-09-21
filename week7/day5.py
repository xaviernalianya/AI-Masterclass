'''.
Train the Classifier
The classifier learns from 28 days of SMP training data. Features are sleep hours, water glasses, and bench press weight. The label is whether steps reached 10,000 that day.

The model splits the data 80/20 for training and testing, then reports its accuracy on the held-out test set.
'''
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 28-day SMP training data
# Features: [sleep_hr, water_glasses, bench_kg]
X = np.array([
    [6.5, 6, 80], [7.2, 8, 85], [5.8, 5, 75], [8.0, 10, 90],
    [7.5, 9, 88], [6.0, 6, 78], [7.8, 8, 86], [8.2, 10, 92],
    [5.5, 4, 70], [7.0, 7, 82], [6.8, 8, 84], [8.5, 11, 95],
    [7.3, 9, 89], [6.2, 6, 76], [7.9, 10, 91], [5.9, 5, 73],
    [8.1, 11, 93], [7.4, 8, 87], [6.7, 7, 83], [8.3, 10, 94],
    [5.6, 4, 71], [7.1, 8, 85], [8.0, 9, 90], [6.4, 6, 77],
    [7.6, 9, 88], [8.4, 11, 96], [6.3, 7, 79], [7.7, 10, 91]
])
print(f"Training data shape: {X.shape}")
# Labels: 1 = hit 10,000 steps, 0 = did not
y = np.array([0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1])
print(f"Labels shape: {y.shape}")
# Split 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Training samples: {len(X_train)}")
print(f"Test samples:     {len(X_test)}")
print(f"Accuracy on test: {accuracy:.0%}")

# Feature importance
features = ["sleep_hr", "water_glasses", "bench_kg"]
importances = clf.feature_importances_
print()
print("Feature importance:")
for name, imp in sorted(zip(features, importances), key=lambda x: -x[1]):
    bar = "#" * int(imp * 40)
    print(f"  {name:<16} {imp:.3f}  {bar}")

# Step 2: Coaching layer
# Simulated coaching layer
# The response structure mirrors the OpenAI API object

class SimulatedMessage:
    def __init__(self, content):
        self.content = content

class SimulatedChoice:
    def __init__(self, content):
        self.message = SimulatedMessage(content)

class SimulatedResponse:
    def __init__(self, content):
        self.choices = [SimulatedChoice(content)]

COACHING_TEMPLATES = {
    # key: (hit_goal, sleep_ok, water_ok)
    (True, True, True):  ("Strong inputs, strong output. Sleep and hydration are locked in.",
                          "Keep this baseline consistent and the steps will follow."),
    (True, True, False): ("You hit the goal despite low water. Sleep is your biggest lever.",
                          "Push hydration tomorrow and the margin grows."),
    (True, False, True): ("Water carried today's performance despite low sleep.",
                          "Shore up sleep tonight. Hitting goals on low sleep has hidden costs."),
    (True, False, False): ("Goal hit through willpower, not system. Willpower runs out.",
                           "Fix sleep and water before the next session."),
    (False, True, True): ("Inputs were solid but the goal was missed.",
                          "Audit what absorbed the energy. Do not cut sleep or water."),
    (False, True, False): ("Sleep is solid, hydration is low, goal was missed.",
                           "Add two glasses of water tomorrow. Hydration shifts step counts more than expected."),
    (False, False, True): ("Low sleep is the lead variable. Water is fine.",
                           "Get to bed 45 minutes earlier. The effect shows within 72 hours."),
    (False, False, False): ("Both inputs are below threshold and the goal was missed.",
                            "Reset tonight: 8 hours sleep minimum, 10 glasses water tomorrow."),
}

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    """Simulated coaching. Real version calls OpenAI Chat API."""
    sleep_ok = sleep >= 7.0
    water_ok = water >= 8
    key = (bool(hit_goal), sleep_ok, water_ok)
    line1, line2 = COACHING_TEMPLATES[key]
    coaching_text = f"{line1} {line2}"
    return SimulatedResponse(coaching_text)

# Test the coaching layer directly
test_cases = [
    (8.0, 10, 90, True,  0.91),
    (5.5, 4,  70, False, 0.88),
    (7.5, 6,  85, True,  0.74),
]
for sleep, water, bench, hit, conf in test_cases:
    response = get_coaching_message(sleep, water, bench, hit, conf)
    message = response.choices[0].message.content
    outcome = "HIT GOAL" if hit else "MISS GOAL"
    print(f"[{outcome} | {conf:.0%} confidence]")
    print(f"Sleep: {sleep}h | Water: {water} glasses | Bench: {bench}kg")
    print(f"Coach: {message}")
    print("-" * 60)


