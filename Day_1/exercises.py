

# Day 1 exercises:

#1 - Create a variable named carname and assign the value Volvo to it.
carname="Volvo"
#2 -Create a variable named x and assign the value 50 to it.
x=50
#3-Print the sum of 5 + 10, using two variables: x and y.
x=5
y=10
z=x+y
print("Sum of the x and y: " +str(z))
print("Sum of the x and y: {}".format(z))
print(f" Sum of the x and y: {z}")
#4-Remove the illegal characters in the variable name below:

my_first_name = "John"
#5-Print the data type of x:
x=5
print(type(x))
#6-Convert x into a  string.
x=7

#8-  Accept two numbers from the user and calculate multiplication:

num1=int(input( "enter two numbers : "))
num2=int(input( "enter two numbers : "))

# 9- Ask a user to enter his/her name , last name and date of birth, and display user inputs
# expected result should be :
  # My name is Jonn.
  # My last name is Smith.
  # I am 35 years old.

name, lname , dob=input("Give your name, last name, and DOB : ").split()
age= 2021-int(dob)
print (f" My name is {name}")
print (f" My last  name is {lname}")
print (f" I am {age} years old")




# 10-import random module and generate a random variable by using random.radom() function
#from random module(library

import random
print(random.random())
