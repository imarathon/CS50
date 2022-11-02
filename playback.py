# a program in Python that prompts the user for input and then outputs that same input, 
# replacing each space with ... (i.e., three periods).

usr_inpt = input ("Please type a phrase: ")
print("")

def dotVille():
    li = list(usr_inpt.split(" "))
    print(*li, sep="...")

print("Here is your phrase with dots in between your words.")
dotVille()

