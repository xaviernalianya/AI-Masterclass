#API Dashboard
#Combines all three processed sections into a single formatted report, 
# then exports the combined data as JSON.
import json

# --- Data (simulated API responses) ---
raw_members = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "cold_shower": True},
    {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "cold_shower": False},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "cold_shower": True},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "cold_shower": True},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
]
daily_steps = [54200, 62000, 58400, 71000, 49600, 68000, 65200]
day_names   = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
skills_list = [
    {"name": "welding",      "enrolled": 8},
    {"name": "tiling",       "enrolled": 12},
    {"name": "copywriting",  "enrolled": 15},
    {"name": "phone repair", "enrolled": 10},
    {"name": "beekeeping",   "enrolled": 6},
]

# --- Process ---
STEP_GOAL = 10000
goal_met = [m for m in raw_members if m["steps"] >= STEP_GOAL]
avg_steps = round(sum(m["steps"] for m in raw_members) / len(raw_members))
showers   = sum(1 for m in raw_members if m["cold_shower"])
best_day  = day_names[daily_steps.index(max(daily_steps))]
top_skill = max(skills_list, key=lambda s: s["enrolled"])

# --- Output ---
W = 52
print("=" * W)
print(f"  SMP COMMAND CENTRE DASHBOARD  |  Week 2024-W47")
print("=" * W)

print(f"\n  SECTION 1: MEMBER PERFORMANCE")
print(f"  {'Total members:':<28} {len(raw_members)}")
print(f"  {'Hit {STEP_GOAL:,} step goal:':}")
print(f"  Hit {STEP_GOAL:,} step goal:          {len(goal_met)}/{len(raw_members)}")
print(f"  {'Average steps:':<28} {avg_steps:,}")
print(f"  {'Cold showers today:':<28} {showers}/{len(raw_members)}")
print(f"  Goal hitters: {', '.join(m['name'] for m in goal_met)}")

print(f"\n  SECTION 2: WEEKLY STEPS")
for day, total in zip(day_names, daily_steps):
    bar = "#" * (total // 5000)
    print(f"  {day:4} {total:>7,}  {bar}")
print(f"  Best day: {best_day} ({max(daily_steps):,} total steps)")
print(f"  Week avg: {round(sum(daily_steps)/len(daily_steps)):,} steps/day")

print(f"\n  SECTION 3: ACTIVE SMP SKILLS")
for s in sorted(skills_list, key=lambda x: -x["enrolled"]):
    print(f"  {s['name']:15} {s['enrolled']} enrolled")
print(f"  Most popular: {top_skill['name']} ({top_skill['enrolled']} enrolled)")

print(f"\n{'=' * W}")

# JSON export
export = {
    "week": "2024-W47",
    "members": {"total": len(raw_members), "goal_met": len(goal_met), "avg_steps": avg_steps},
    "weekly": {"best_day": best_day, "total_steps": sum(daily_steps)},
    "skills": {"active": len(skills_list), "most_popular": top_skill["name"]}
}
print("\nJSON export:")
print(json.dumps(export, indent=2))