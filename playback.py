# a program in Python that prompts the user for input and then outputs that same input, 
# replacing each space with ... (i.e., three periods).

usr_inpt = input ("Please type a phrase: ")
print("")

li = list(usr_inpt.split(" "))

print("Here is your phrase with dots in between your words.")
print(*li, sep=("..."))

def splt_phrs ()
    return 
