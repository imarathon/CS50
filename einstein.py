# A program in Python that prompts the user for mass as a number
# and then outputs the equivalent number of Joules as an integer
import math

def main():
    user = int(input("Please input a number in Kilograms and I will convert it to Joules: "))
    joules = float(300000000)
    result = user*(joules**2)

    print(round(result))
main()