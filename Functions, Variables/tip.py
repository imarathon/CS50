#Simple tip calculator. 

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave a ${tip:.2f} tip")


def dollars_to_float(d):
    no_dollar = d.replace("$", " ")
    return float(no_dollar)

def percent_to_float(p):
    no_percent = p.replace("%", " ")
    return float(no_percent) / 100

main()
