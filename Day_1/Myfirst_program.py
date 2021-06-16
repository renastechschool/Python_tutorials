## Day 1

# User Input

#Exercise 1: Categorize a person for covit-19 risk based on his/her age:
high_risk=65
mid_risk=45
low_risk=20
no_risk=15

print(type(no_risk))
age=input(" What is your age ?")

if int(age) > high_risk:
    print("You are in high risk")
if int(age) < high_risk and age > mid_risk:
    print("You are in mid risk")
if int(age) <  mid_risk and age > low_risk:
    print("You are in low risk")
if int(age) < no_risk:
    print("You are good")

# Exercise 2: Create a converter that will ask for age and convert it into days, then print it.
age2=input("What is your age?")
days=age2*365
print("You have lived " +days)

