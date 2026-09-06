import json
import os

# --- Configuration ---
BASE_URL = "https://api.smptracker.com/v1"
API_KEY = os.environ.get("SMP_API_KEY", "demo_key_123")
TARGET_CITY = "Nairobi"
STEP_GOAL = 10000

# --- Fetch ---
def fetch_members(city, limit=50):
    # Simulated API response
    all_members = [
        {"name": "James Omondi",  "city": "Nairobi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5},
        {"name": "Sandra Weru",   "city": "Nairobi",  "steps": 10500, "protocol": "2MAD", "sleep": 8.0},
        {"name": "Patrick Njiru", "city": "Mombasa",  "steps": 8100,  "protocol": "OMAD", "sleep": 6.5},
        {"name": "Grace Achieng", "city": "Nairobi",  "steps": 11000, "protocol": "OMAD", "sleep": 7.0},
        {"name": "Brian Kamau",   "city": "Kisumu",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0},
        {"name": "Kevin Mwangi",  "city": "Nairobi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5},
    ]
    return [m for m in all_members if m["city"] == city][:limit]

# --- Process ---
def process_members(members, step_goal):
    goal_met = [m for m in members if m["steps"] >= step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / len(members)) if members else 0
    avg_sleep = round(sum(m["sleep"] for m in members) / len(members), 1) if members else 0
    top = max(members, key=lambda m: m["steps"]) if members else {}
    return {
        "total": len(members),
        "goal_met": len(goal_met),
        "avg_steps": avg_steps,
        "avg_sleep": avg_sleep,
        "top_name": top.get("name", "N/A"),
        "top_steps": top.get("steps", 0),
        "achievers": [m["name"] for m in goal_met]
    }

# --- Output ---
def print_report(city, summary):
    print(f"\n{'='*48}")
    print(f"  SMP DAILY REPORT: {city.upper()}")
    print(f"{'='*48}")
    print(f"  Members:       {summary['total']}")
    print(f"  Hit {STEP_GOAL:,} steps: {summary['goal_met']}")
    print(f"  Avg steps:     {summary['avg_steps']:,}")
    print(f"  Avg sleep:     {summary['avg_sleep']} hrs")
    print(f"  Top:           {summary['top_name']} ({summary['top_steps']:,})")
    print(f"\n  Achievers: {', '.join(summary['achievers'])}")
    print(f"{'='*48}\n")

# --- Main ---
members = fetch_members(TARGET_CITY)
summary = process_members(members, STEP_GOAL)
print_report(TARGET_CITY, summary)