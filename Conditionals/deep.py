# A program that prompts the user for the answer to the Great Question of Life, 
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) 
# forty-two or forty two. Otherwise output No.

user = str(input("The answer to the Great Question of Life, the Universe and Everything is? : "))

if user == "42" or user =="forty-two" or user == "forty two":
    print("Yes")
else:
    print("No. Try again.")