#Compare integers. Input from user
'''
x = int(input("What is x? : "))
y = int(input("What is y? : "))

if x < y: 
    print("x is less than y")
elif x > y: 
    print("x is greater than y")
else: 
    print("x and y are equal")
'''
# Comparisons with the "or".

x = int(input("What is x? : "))
y = int(input("What is y? : "))

#if x < y or x > y:
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
