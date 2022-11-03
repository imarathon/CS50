'''
name = input("Whats your name?")
print("Hello, " + name)
'''

'''
# Remove whitespace from str input
namef = input("Whats your name?").strip().title()
namel = input("Whats your last name?").strip().title()

# Say hello to user
print(f"Hello, {namef} {namel}")
'''

'''
# Remove whitespace from str input
name = input("Whats your name?").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {last}")
'''

#int and floats
'''
# Simple addition calculator
x = 1
y = 2

z = x + y

print(z)
'''

'''
# Simple addition calculator with user input

x = input("What is x ?: ")
y = input("What is y ?: ")

# int() in front of variable converts str to int
z = int(x) + int(y)

print(z)
'''

'''
# Simple addition calculator with user input
# int() in front of variable converts str to int

x = int(input("What is x ?: "))
y = int(input("What is y ?: "))

print(x + y)
'''

'''
# Simple addition calculator with user input
# float() in front of variable converts str to float

x = float(input("What is x ?: "))
y = float(input("What is y ?: "))

#round will take float and round, see documentation to see how many decimals you want to round to.
z = round(x * y)

print(z)
'''

'''
# Simple addition calculator with user input
# float() in front of variable converts str to float

x = float(input("What is x ?: "))
y = float(input("What is y ?: "))

#round will take float and round, see documentation to see how many decimals you want to round to.
z = round(x * y)

#f"{z:,}" adds a coma every 3rd digit
print(f"{z:,}")
'''
'''
# Simple addition calculator with user input
# float() in front of variable converts str to float

x = float(input("What is x ?: "))
y = float(input("What is y ?: "))

#round function with added argument after "," tells how many decimal spaces to use
z = round(x / y, 0)
#Another option print(f"{z:.2f}")

print(z)
'''
'''
#Functions
def main():
    name = input("What's your name? ").strip().title()
    hello(name)
    hello()

def hello(to="World"):
    print("Hello, " + to)

main()

#https://video.cs50.io/JP7ITIXGpHk?start=5175
'''

#return
from re import X

def main():
    x = int(input("Enter a number to square it: "))
    print("Your number squared is: ", square(x))

def square(n):
    return n * n
#    return pow (n, 2)
#    return n ** 2

main()

