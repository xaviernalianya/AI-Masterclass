
#"w"	Write. Creates or overwrites the file.
#The with statement automatically closes the file when the block ends, even if an error occurs.

    
with open("daily_log.txt", "w") as f: 
    f.write("Steps: 9200\n")
    f.write("Water: 8 glasses\n")
    f.write("Protocol: OMAD\n")
    f.write("Cold shower: Yes\n")

import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write("Steps: 9000\n")
file_content.write("Water: 8 glasses\n")
file_content.write("Protocol: OMAD\n")
file_content.write("Cold shower: Yes\n")

print("File written. Contents:")
print(file_content.getvalue())

#To read a file in Python
with open("daily_log.txt", "r") as f:
    content=f.read()
    print(content)

import io
file_data="""Steps:9200
    Water: 8 glasses
    Protocol: OMAD
    Cold shower: YES
    Sleep hours: 7.5
"""
f=io.StringIO(file_data)
lines=f.readlines()
print("No. of line ", len(lines))

for l in lines:
    l=l.strip() 
    print(l)