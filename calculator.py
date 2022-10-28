"""
#takes user input and coverts to int
x = int(input("What's x? "))
y = int(input("What's y? "))
#prints multiplies user input
print(x * y)

#takes user input and converts to float
x = float(input("What's x? "))
y = float(input("What's y? "))
#rounds to nearest integet
z = round(x + y)
#converts to f(str) and adds coma to numbers
print (f"{z:,}")
"""

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print (f"{z:.2f}")