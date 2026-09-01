#A dairy farmer logs daily milk volumes. 
# His script receives the entry "two hundred" but needs a number. 
# Write a try / except block that tries to convert "two hundred" to a float, 
# catches the ValueError, and prints exactly:
#Invalid entry: two hundred is not a number

def dairy_log(volume):
    try:
        return int(volume)
    except:
        return "Invalid entry: two hundred is not a number"

print(dairy_log("two hundred "))