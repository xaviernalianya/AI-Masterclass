# Write a function called greet that takes a name
# and returns a greeting string

def greet(name):
    return f"Hello, {name}. Welcome to the program."
print(greet("Xavier"))

# Write a function called power(base, exp=2)
# that returns base raised to exp

def power(base, exp=2):
    return base**exp
print(power(3))

# Use a list comprehension to get all even numbers from 1 to 30
evens=[n for n in range(1,31) if n%2==0]
print(evens)

# Write a function that takes a list of scores
# and returns the average, highest, and lowest

def analyse(scores):
    return {
        "average": sum(scores)/len(scores),
        "highest": max(scores),
        "lowest":min(scores),
    }
print(analyse([3, 4, 5, 1, 1]))