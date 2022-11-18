#Program determines if a number is odd or even
'''
x = int(input("What is x?: "))

if x % 2 == 0:
    print("The number is even")
else: 
    print("The number is odd")
'''

def main():
    x = int(input("Type a number: "))
    if is_even(x):
        print("The number", x, "is even.")
    else: 
        print("The number", x, "is odd.")
'''
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
'''
# An improved function than above
'''
def is_even(n):
    return True if n % 2 == 0 else False
'''
# Even shorter function
def is_even(n):
    return n % 2 == 0

main()


