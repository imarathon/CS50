# A program in Python that prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer
import math

def main():
    user = int(input("Please input a number in Kilograms: "))
    joules = 300000000
    result = user * (joules**2)

    print(round(user), "Kilograms equals", result, "in Joules.")

main()