# A program in Python that prompts the user for mass as an integer (in kilograms) 
# and then outputs the equivalent number of Joules as an integer
import math

def main():
    user = float(input("Please input a number in Kilograms and I will convert it to Joules: "))
    joules = 89875517873681764
    result = user * joules

    print(result)
    print(round(result,12))

main()