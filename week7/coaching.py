'''The coaching layer is a function that takes structured data in and returns a formatted coaching response out. 
It does not make decisions about whether to run or when. 
It only knows how to turn data into a message.'''

'''
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    prompt = (f"Athlete data: sleep {sleep}h, water {water} glasses, "
              f"bench {bench}kg. "
              f"Goal prediction: {'HIT' if hit_goal else 'MISS'} ({confidence:.0%} confidence). "
              "Give a 2-sentence coaching response. Be direct and specific.")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": ("You are an SMP performance coach. "
                          "You give direct, data-driven coaching feedback. "
                          "No filler. Two sentences maximum.")},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
    '''
import pandas as pd
import numpy as np
import openai, os, joblib
from dotenv import load_dotenv
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load data from CSV
df = pd.read_csv("smp_log.csv")
X = df[["sleep_hr", "water_glasses", "bench_kg"]].to_numpy()
y = (df["steps"] >= 10000).astype(int).to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save trained model so you do not retrain every time
joblib.dump(clf, "smp_coach_model.pkl")

def get_coaching_message(sleep, water, bench, hit_goal, confidence):
    prompt = (f"Athlete logged: sleep {sleep}h, water {water} glasses, bench {bench}kg. "
              f"Model predicts: {'HIT GOAL' if hit_goal else 'MISS GOAL'} at {confidence:.0%} confidence. "
              "Give a direct 2-sentence coaching response. No filler. No hedging.")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
             "content": "You are an SMP performance coach. Data-driven. Direct. Two sentences maximum."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def analyze_day(sleep_hr, water_glasses, bench_kg, day_label=None):
    features = np.array([[sleep_hr, water_glasses, bench_kg]])
    prediction = clf.predict(features)[0]
    confidence = clf.predict_proba(features)[0][prediction]
    coaching = get_coaching_message(sleep_hr, water_glasses, bench_kg, prediction, confidence)
    return {
        "label":      day_label or "Day",
        "hit_goal":  bool(prediction),
        "confidence": confidence,
        "coaching":   coaching,
    }