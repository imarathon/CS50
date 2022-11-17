#output a grade based on what the user inputs

score = int(input("What is the test score?: "))
'''
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: c")
elif score >= 60 and score < 70:
    print("Grade: D")
else: 
    print("Grade: F")
'''
#below is the same code above but improved
'''
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: c")
elif 60 <= score < 70:
    print("Grade: D")
else: 
    print("Grade: F")
'''

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: c")
elif score >= 60:
    print("Grade: D")
else: 
    print("Grade: F")
