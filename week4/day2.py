#Error Handling
# A tiling contractor calculates cost per tile for each job.
# If zero tiles are entered by mistake, the program should not crash.

def cost_per_tile(total_cost,num_tiles):
    try:
        result= total_cost/num_tiles
    except ZeroDivisionError:
        print("Cannot divide: zero tiles entered")
    else:
        print(f"KES{total_cost}/{num_tiles}tiles=KES {result:.2f} per tile")
    finally:
        print("Calculation Attempted")
print()

cost_per_tile(3000,40)
cost_per_tile(23340,0)

def log_steps(steps):
    if not isinstance(steps, int):
        raise TypeError("Steps must be an integer.")
    if steps < 0:
        raise ValueError("Steps cannot be negative.")
    print(f"Steps logged: {steps}")

try:
    log_steps(700)
    log_steps(-500)
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)


#Write a function called safe_log_entry(data) that takes a dictionary and
#  tries to extract steps, water, and protocol. 
# If steps is not a valid integer, print an error and return None. 
# If water is missing, use a default of 0. 
# If protocol is missing, use "Unknown". Print a clean report for each valid entry.


def safe_log_entry(data):[
    {"steps":5000, "water": 8, "protocol":"OMAD"},
    {"steps":5000, "water": 8, "protocol":"OMAD"},
    {"steps":5000, "water": 8, "protocol":"OMAD"},
    ]
try:
   steps= int(data["steps"])
except(ValueError, TypeError, KeyError):
    print("Invalid steps data. Skipping entry")
    return None
                      
