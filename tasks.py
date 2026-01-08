
# word = input("Enter a word (Food, Red, Lexus): ") 

# if word == "Food":
#     print("Food: Any nutritious substance that people or animals eat or drink, or that plants absorb, in order to maintain life and growth.")
# elif word == "Red":
#     print("Red: A color at the end of the spectrum next to orange and opposite violet, as of blood, fire, or rubies.")  
# elif word == "Lexus":
#     print("Lexus: A luxury vehicle division of the Japanese automaker Toyota.")

# else:
#     print("Sorry, the word you entered is not in the dictionary.")



# names = ["admin", "Ayo", "Dami", "Daniel", "Sarah"]

# for name in names:
#     print("The current name is:", name)


# contacts1 = ["Alice", 9484, "Bob", 9485, "Charlie", 9486, "David", 9487, "Eve", 9488]




# contacts = {
#     "Alice": 9484,
#     "Bob": 9485,
#     "Charlie": 9486,
#     "David": 9487,
#     "Eve": 9488
# }

# for cnt in contacts:
#     print(contacts[cnt])
    
# a basic, CLI phonebook application
# del memos["date"]

contacts = {}

while True:
    cmd = input("Enter command (add, view, quit, delete): ")
    if cmd == "quit":
        print("Exiting phonebook application.")
        break
    elif cmd == "add":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added.")

    elif cmd == "view":
        name = input("Enter name to view: ")
        if name in contacts:
            print(f"{name}'s phone number is {contacts[name]}.")
        else:
            print(f"Contact {name} not found.")


    



































# usernames = ["admin", "Ayo", "Dami", "Daniel", "Sarah"]

# # loops



