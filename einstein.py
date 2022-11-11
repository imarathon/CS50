# A program in Python that prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer

m = int(input("m: "))
c = 300000000

E = m * (c**2)

print(E)