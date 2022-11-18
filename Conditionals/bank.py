#a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. 
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    user = str(input("Type a greeting, please: ")).capitalize()
    
    if user.find("Hello")!=-1:
        print("You get $0.00")
    elif user.find("H")!=-1:
        print("You get $20.00")
    else:
        print("You get $100.00")

main()
