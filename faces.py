# a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 
# and any :( converted to 🙁. All other text should be returned unchanged.
# In that same file, a function called main that prompts the user for input, 
# calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, 
# as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

def main():
    user = str(input("Please enter some text, and make sure to include a smiley or frowny face. :) or :( : "))
    print("You typed: ", user)


main()