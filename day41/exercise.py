commits = [
    "Initial commit",
    "Add SMP tracker script",
    "Fix loop logic in day5.py",
    "Add requirements.txt"
]
#Use a for loop with enumerate to print each one numbered.
for index, commit in enumerate(commits, start=1):
    print(f"{index}. {commit}") 
    