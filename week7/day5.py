'''.
Train the Classifier
The classifier learns from 28 days of SMP training data. Features are sleep hours, water glasses, and bench press weight. The label is whether steps reached 10,000 that day.

The model splits the data 80/20 for training and testing, then reports its accuracy on the held-out test set.
'''
from unittest import result

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

#Step 3 of 4
#Connect the Classifier to the Coaching Layer
#Now both components run together. 
# The classifier produces a prediction and a confidence score. 
# Those values pass directly into the coaching layer, which returns a message.
#  One function, analyze_day(), wraps both steps and returns a single result dict.

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# --- Training data ---
X = np.array([
    [6.5,6,80],[7.2,8,85],[5.8,5,75],[8.0,10,90],[7.5,9,88],
    [6.0,6,78],[7.8,8,86],[8.2,10,92],[5.5,4,70],[7.0,7,82],
    [6.8,8,84],[8.5,11,95],[7.3,9,89],[6.2,6,76],[7.9,10,91],
    [5.9,5,73],[8.1,11,93],[7.4,8,87],[6.7,7,83],[8.3,10,94],
    [5.6,4,71],[7.1,8,85],[8.0,9,90],[6.4,6,77],[7.6,9,88],
    [8.4,11,96],[6.3,7,79],[7.7,10,91]
])
y = np.array([0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# --- Coaching templates ---
COACHING_TEMPLATES = {
    (True, True, True):  ("Strong inputs, strong output. Baseline is locked in.",
                          "Keep this pattern consistent."),
    (True, True, False): ("Hit the goal despite low water. Sleep is the primary driver.",
                          "Close the hydration gap tomorrow."),
    (True, False, True): ("Water carried today's performance despite low sleep.",
                          "Fix sleep tonight. Hitting goals on low sleep has hidden costs."),
    (True, False, False): ("Goal hit through willpower, not system. That is not repeatable.",
                           "Build the foundation: sleep first, water second."),
    (False, True, True): ("Inputs were solid. The miss came from schedule pressure or load.",
                          "Audit what absorbed the energy. Do not cut sleep or water."),
    (False, True, False): ("Sleep is solid but hydration is low, and the goal was missed.",
                           "Add two glasses of water tomorrow. Hydration shifts step counts directly."),
    (False, False, True): ("Low sleep is the primary variable. Water is fine.",
                           "Get to bed 45 minutes earlier. The compound effect shows within 72 hours."),
    (False, False, False): ("Both inputs are below threshold. A reset is required.",
                            "8 hours sleep minimum. 10 glasses water tomorrow. No shortcuts."),
}

def get_coaching_message(sleep, water, hit_goal):
    key = (bool(hit_goal), sleep >= 7.0, water >= 8)
    line1, line2 = COACHING_TEMPLATES[key]
    return f"{line1} {line2}"

def analyze_day(sleep_hr, water_glasses, bench_kg, day_label=None):
    """Run the full pipeline: predict, score, coach."""
    features = np.array([[sleep_hr, water_glasses, bench_kg]])
    prediction = clf.predict(features)[0]
    proba = clf.predict_proba(features)[0]
    confidence = proba[prediction]
    coaching = get_coaching_message(sleep_hr, water_glasses, prediction)
    return {
        "label":         day_label or "Day",
        "sleep_hr":      sleep_hr,
        "water_glasses": water_glasses,
        "bench_kg":      bench_kg,
        "hit_goal":      bool(prediction),
        "confidence":    confidence,
        "coaching":      coaching,
    }

# Test on three new days
new_days = [
    (8.0, 10, 92),   # strong day
    (5.5,  4, 70),   # weak day
    (7.2,  7, 84),   # borderline day
]

for sleep, water, bench in new_days:
    result = analyze_day(sleep, water, bench)
    outcome = "HIT GOAL" if result["hit_goal"] else "MISS GOAL"
    print(f"Prediction: {outcome} ({result['confidence']:.0%} confidence)")
    print(f"Inputs:     sleep={result['sleep_hr']}h, water={result['water_glasses']} glasses, bench={result['bench_kg']}kg")
    print(f"Coach:      {result['coaching']}")
    print()

#Step 4 of 4
#Full Application with Batch Output and Summary
#The complete application processes multiple days in a batch, prints a formatted coaching report for each day, then prints an overall summary: hit rate, average confidence, and the input difference between hit and miss days.
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# --- Training ---
X = np.array([
    [6.5,6,80],[7.2,8,85],[5.8,5,75],[8.0,10,90],[7.5,9,88],
    [6.0,6,78],[7.8,8,86],[8.2,10,92],[5.5,4,70],[7.0,7,82],
    [6.8,8,84],[8.5,11,95],[7.3,9,89],[6.2,6,76],[7.9,10,91],
    [5.9,5,73],[8.1,11,93],[7.4,8,87],[6.7,7,83],[8.3,10,94],
    [5.6,4,71],[7.1,8,85],[8.0,9,90],[6.4,6,77],[7.6,9,88],
    [8.4,11,96],[6.3,7,79],[7.7,10,91]
])
y = np.array([0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# --- Coaching templates ---
COACHING_TEMPLATES = {
    (True, True, True):  ("Strong inputs, strong output. Baseline is locked in.",
                          "Keep this pattern consistent."),
    (True, True, False): ("Hit the goal despite low water. Sleep is the primary driver.",
                          "Close the hydration gap tomorrow."),
    (True, False, True): ("Water carried today despite low sleep.",
                          "Fix sleep tonight. Low sleep has costs that accumulate."),
    (True, False, False): ("Goal hit through willpower, not system. That is not repeatable.",
                           "Build the foundation: sleep first, water second."),
    (False, True, True): ("Inputs were solid. The miss came from schedule pressure or load.",
                          "Audit what absorbed the energy. Do not cut sleep or water."),
    (False, True, False): ("Sleep is solid but hydration is low, and the goal was missed.",
                           "Add two glasses of water tomorrow. Hydration shifts step counts directly."),
    (False, False, True): ("Low sleep is the primary variable. Water is fine.",
                           "Get to bed 45 minutes earlier. The effect shows within 72 hours."),
    (False, False, False): ("Both inputs are below threshold. A reset is required.",
                            "8 hours sleep minimum. 10 glasses water tomorrow. No shortcuts."),
}

def get_coaching_message(sleep, water, hit_goal):
    key = (bool(hit_goal), sleep >= 7.0, water >= 8)
    line1, line2 = COACHING_TEMPLATES[key]
    return f"{line1} {line2}"

def analyze_day(sleep_hr, water_glasses, bench_kg, day_label=None):
    features = np.array([[sleep_hr, water_glasses, bench_kg]])
    prediction = clf.predict(features)[0]
    proba = clf.predict_proba(features)[0]
    confidence = proba[prediction]
    coaching = get_coaching_message(sleep_hr, water_glasses, prediction)
    return {
        "label":         day_label or "Day",
        "sleep_hr":      sleep_hr,
        "water_glasses": water_glasses,
        "bench_kg":      bench_kg,
        "hit_goal":      bool(prediction),
        "confidence":    confidence,
        "coaching":      coaching,
    }

# --- Batch of incoming days ---
incoming_days = [
    ("Day 29", 8.0, 10, 92),
    ("Day 30", 5.5,  4, 70),
    ("Day 31", 7.2,  7, 84),
    ("Day 32", 8.5, 11, 95),
    ("Day 33", 6.1,  5, 76),
    ("Day 34", 7.8,  9, 88),
    ("Day 35", 5.9,  6, 73),
]

# Process all days, collect before printing
results = [analyze_day(sleep, water, bench, label)
           for label, sleep, water, bench in incoming_days]

# --- Individual reports ---
SEP = "=" * 62
print(SEP)
print("    SMP PERFORMANCE COACH  |  DAILY REPORTS")
print(SEP)

for r in results:
    outcome = "HIT GOAL" if r["hit_goal"] else "MISS GOAL"
    print(f"\n{r['label']}")
    print(f"  Outcome:  {outcome} ({r['confidence']:.0%} confidence)")
    print(f"  Inputs:   sleep={r['sleep_hr']}h  water={r['water_glasses']}gl  bench={r['bench_kg']}kg")
    print(f"  Coach:    {r['coaching']}")

# --- Summary ---
print()
print(SEP)
print("    SUMMARY")
print(SEP)

total  = len(results)
hits   = sum(1 for r in results if r["hit_goal"])
misses = total - hits
avg_conf = np.mean([r["confidence"] for r in results])

hit_days  = [r for r in results if r["hit_goal"]]
miss_days = [r for r in results if not r["hit_goal"]]

avg_sleep_hit  = np.mean([r["sleep_hr"]      for r in hit_days])  if hit_days  else 0
avg_water_hit  = np.mean([r["water_glasses"]  for r in hit_days])  if hit_days  else 0
avg_sleep_miss = np.mean([r["sleep_hr"]      for r in miss_days]) if miss_days else 0
avg_water_miss = np.mean([r["water_glasses"]  for r in miss_days]) if miss_days else 0

print(f"\n  Days analyzed:    {total}")
print(f"  Goals hit:        {hits} / {total}  ({hits/total:.0%})")
print(f"  Goals missed:     {misses} / {total}  ({misses/total:.0%})")
print(f"  Avg confidence:   {avg_conf:.0%}")
print()
print("  On HIT days:")
print(f"    avg sleep:  {avg_sleep_hit:.1f}h  |  avg water: {avg_water_hit:.1f} glasses")
print()
print("  On MISS days:")
print(f"    avg sleep:  {avg_sleep_miss:.1f}h  |  avg water: {avg_water_miss:.1f} glasses")
print()
sleep_diff = avg_sleep_hit - avg_sleep_miss
water_diff = avg_water_hit - avg_water_miss
print(f"  HIT days averaged {sleep_diff:+.1f}h more sleep and {water_diff:+.1f} more glasses of water")
print()
print(SEP)
print("    End of report")
print(SEP)
