# A program that tells user what house they belong in Hogwarts

name = input("What's your name? ").capitalize()
'''
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("New phone, who dis?") 
'''
# cleaner code 
'''
#if name == "Harry" or name == "Hermione" or name == "Ron":
if name == "Harry" or "Hermione" or "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("New phone, who dis?") 
'''
#working with match keyword
'''
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("New phone, who dis?")
'''
#condencing above code
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Hi",name,", you are in house Gryffindor")
    case "Draco":
        print("Hi",name,", you are in house Slytherin")
    case _:
        print("New phone, who dis?")

