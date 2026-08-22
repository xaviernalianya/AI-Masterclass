#Each contact is a dictionary. 
# The full contact book is a list of those dictionaries. 
# Start by creating five contacts and printing them.

#Step 1
#Create the data structure and verify it prints correctly.
contacts_book=[
    {
        "name":"James Omondi",
        "phone":"0723456789",
        "skill":"welding",
        "city":"Nairobi",
    },
    {
        
        "name":"Mary Wanjiku",
        "phone":"0712345678",
        "skill":"plumbing",
        "city":"Nairobi",
    },
    {
        "name":"John Mwangi",
        "phone":"0734567890",
        "skill":"carpentry",
        "city":"Mombasa",
    },
    {
        "name":"Grace Achieng",
        "phone":"0701234567",
        "skill":"electrical work",
        "city":"Kisumu",
    },
    {
        "name":"Peter Otieno",
        "phone":"0745678901",
        "skill":"painting",
        "city":"Eldoret",
    }
]
print(contacts_book)
print("Contact book has", len(contacts_book), "contacts")

#Printing the raw list is hard to read. Write a loop that prints each contact in a clean format.

#Step 2
#Loop through the list and print each contact with a readable layout
print("---------CONTACT BOOK----------")
for contact in contacts_book:
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Skill: {contact['skill']}")
    print(f"City: {contact['city']}")
    print("-" * 30)
#Loop through the list and compare each contact's name to the name you are searching for. If it matches, print that contact's details.

#Step 3
#Search by name and print the result.
search_name = " Omondi"
for contact in contacts_book:
    if contact["name"] == search_name:
        print(f"Contact found: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Skill: {contact['skill']}")
        print(f"City: {contact['city']}")
        break
else:
    print("Contact not found.")

#Seach by City
print("\n========Nairobi Contacts========")
for contact in contacts_book:
    if contact["city"]=="Nairobi":
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Skill: {contact['skill']}")
        print(f"City: {contact['city']}")
        print("-" * 30)
        