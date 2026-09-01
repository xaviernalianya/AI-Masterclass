import csv
import io
import json

csv_data = """name,score1,score2,score3
James Omondi,85,90,78
Sandra Weru,72,,88
Patrick Njiru,91,87,94
Grace Achieng,60,bad data,70
Brian Kamau,55,48,62"""

# Functions
def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def calculate_average(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)

def letter_grade(avg):
    if avg is None: return "N/A"
    if avg >= 90:   return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else:           return "F"

# Process CSV
f = io.StringIO(csv_data)
reader = csv.DictReader(f)
results = []

print("=" * 50)
print(f"{'NAME':<20} {'AVG':>5}  {'GRADE':>5}  NOTES")
print("=" * 50)

for row in reader:
    scores = [
        parse_score(row["score1"]),
        parse_score(row["score2"]),
        parse_score(row["score3"])
    ]
    invalid_count = scores.count(None)
    avg = calculate_average(scores)
    grade = letter_grade(avg)
    notes = f"{invalid_count} invalid score(s)" if invalid_count else "All scores valid"

    print(f"{row['name']:<20} {str(avg):>5}  {grade:>5}  {notes}")

    results.append({
        "name": row["name"],
        "scores": [row["score1"], row["score2"], row["score3"]],
        "average": avg,
        "grade": grade
    })

print("=" * 50)

# Class summary
valid_avgs = [r["average"] for r in results if r["average"] is not None]
class_avg = round(sum(valid_avgs) / len(valid_avgs), 1)
print(f"\nClass average: {class_avg}")
print(f"Students: {len(results)}")

# Export as JSON
print("\nJSON export:")
print(json.dumps(results, indent=2))