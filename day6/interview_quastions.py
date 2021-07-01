# Q1. What is Python and why it is so popular?
# Ans: Python is an interpreted, high-level, general-purpose programming language.
# Python’s design philosophy emphasizes code readability with its notable use of significant whitespace.
# It is popular because it has a simplified syntax which gives more emphasis on natural language.

##====================================================================================##
# Q2. Why python execution is slow and how we can improve it?
# Ans: The Reason Behind Python code execute slow is because it is an interpreted language.
# Its code is interpreted at the runtime instead of being compiled to a native language.
# To improve the speed of Python code, we can use CPython, Numba instead of core python or we can also do some changes in our code.
# 1. Reducing Memory Footprints.
# 2. Using Built-in Functions and Libraries.
# 3. Move calculation Outside the loop.
# 4. Keeping Code Base Small.
# 5. Avoid Unwanted Loops

##====================================================================================##

# Q3. What Are The Features Of Python?
# Ans: 1. Easy to Code
# 2. Free and Open Souce Language
# 3. High-Level Language
# 4. Easy to Debug
# 5. OOPS support
# 6. Large Collection of standard libraries and third-party modules
# 7. Extensible Feature(we can write python code in c and c++ also)
# 8. User-Friendly Data Structure

##====================================================================================##

# Q4. What Are The Applications of Python?
# Ans: 1. Web Development
# 2. Desktop GUI Development
# 3. Artificial Intelligence and Machine learning
# 4. Software Development
# 5. Business Application Development
# 6. Console Based Application
# 7. Software Testing
# 8. Web Automation
# 9. Audio or Video-Based Application
# 10. Image Processing application

##====================================================================================##

# Q5. Limitations of Python?
# 1. Speed
# 2. Mobile Development
# 3. Memory Consumption (Very high compare to other languages)
# 4. Incompatibility of Two Versions (2,3)
# 5. Runtime Errors (require more testing and has errors that show up only at runtime)
# 6. Simplicity

##====================================================================================##

# Q6. How Python Code is executed?
# Ans: First the Interpreter reads the python code and checks for any syntax or formatting error. if some error is found then it halts the execution.
# if there is no error found then the interpreter translates the python code into its equivalent form or byte code.
# then the byte code is sent to the python virtual machine(PVM).
# Here again, the python code is executed and if any error found then execution is halted otherwise the result is shown on the output window.

##====================================================================================##

# Q7. How Memory is Managed In Python?
# Ans: Python memory is managed by python private headspace. All the python objects and data structures are located in a private heap.
# The allocation of the private heap is taken care of by the Python memory manager.
# Python also has an inbuilt garbage collector that recycles unused memory and frees the memory and makes it available for the headspace.

##====================================================================================##

# Q8. Explain Inbuilt Data Structures of python?
# Ans: There are mainly four types of data structures in python.
# 1. Lists: List is a collection of heterogeneous data items from integers to strings even another list.
# Lists are mutable. lists do the work of most of the collection data structures found in other languages.
# A list is defined in [ ] brackets. Ex: a = [1,2,3,4]
# 2. Sets: A set is an unordered collection of unique elements. set operations like union | ,
# intersection &and difference — can be applied to a set. sets are immutable. () are used to represent a set.
# Ex: a={1,2,3,4,}
# 3. Tuple: Python tuples work exactly like Python lists except they are immutable. () use to define a tuple.
# Ex: a = (1,2,3,4)
# 4. Dictionary: Dictionary is a collection of key-value pairs. it is similar to the hash map in other languages.
# In Dictionary Keys are Unique and immutable objects.
# Ex: a = {‘numbers’:[1,2,3,4]}

##====================================================================================##

# Q9. Explain //,% and * *operators in python?
# Ans:
# // (Floor Division)- It is a division operator that returns the integer part of the division.\
#     Ex: 5//2=2
# % ( Modulus)- It returns the remainder of the division.
# Ex: 5%2=1
# ** (Power)- It performs an exponential calculation on the operator. a**b means a raised to the power of b.
# Ex: 5**2=25, 5**3 = 125

##====================================================================================##

# Q10. Difference Between append, extend, and insert in python. Explain with an example?
# Ans: append: It is used to add new elements at the end of the list.
# insert: It is used to add an element at a particular position in the list.
# extend: It is used to extend the list by adding a new list.
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
>[1,2,3,4,5,6]
numbers.insert(2,7)  ## insert(position,value)
print(numbers)
#[1,2,7,4,5,6]
numbers.extend([7,8,9])
print(numbers)
#[1,2,7,4,5,6,7,8,9]
numbers.append([4,5])
#[1,2,7,4,5,6,7,8,9,[4,5]]

##====================================================================================##

# Q11. how do break, continue, and pass works?
# Ans: break: It causes the Program to exit from the loop when the condition is met.
# Continue: It returns the control to the beginning of the loop.
# it causes the program to skip all the remaining statements in the current iteration of the loop.
# Pass: It simply causes the program to pass all the remaining statements without executing.

##====================================================================================##

# Q12. Differentiate remove, del, and pop in python?
# Ans: remove: It removes the first matching value in the list. it takes the value as a parameter.
# del: It deletes elements using an index. it does not return any value.
# pop: it removes the top element from the list. it returns the top element of the list.
numbers = [1,2,3,4,5]
numbers.remove(5)
# > [1,2,3,4]
del numbers[0]
>[2,3,4]
numbers.pop()
# >4

##====================================================================================##

# Q13. Explain the range function in python with an example?
# Ans: range: range function returns a number of sequences from the starting point to an endpoint.
# range(start,end) There is one more third parameter which is the step used to define steps in the range.
for i in range(5):  ## number
     print(i)
# > 0,1,2,3,4
 for i in range(1,5):  ##(start,end)
    print(i)
# > 1,2,3,4
 for i in range(0,5,2):   ## (start,end,step)
     print(i)
# >0,2,4

##====================================================================================##

# Q14.Difference between == and is operator in python?
# Ans: == it compares the equality of two objects or values.
# is an operator is used to check whether the two objects belong to the same memory object.
lst1 = [1,2,3]
lst2 = [1,2,3]
lst1 == lst2
#>True
lst1 is lst2
# >False  ## They Both Belong to different memory object

##====================================================================================##

# Q15. How to change the data type of a list?
# Ans: To Change the data type of a list to tuple you can use tuple() same for set set()
lst = [1,2,3,4,2]
set(lst)    ## {1,2,3,4}
tuple(lst)  ## (1,2,3,4,2)


##====================================================================================##

# Q16. What are the different ways to comment in python?
# Ans: In Python, we can comment in two ways.
# 1. ``` ``` for multiple comments.
# 2. ## for single-line comment.

##====================================================================================##

# Q17. Does Python have a main function?
# Ans: Yes, it has. it is automatically executed whenever we run a python script.

##====================================================================================##

# Q18. What is a lambda function?
# Ans: Lambda Function is a single line function with no name,
# which can have n number of arguments but it can only have on expression. It is also called an anonymous function.
 a = lambda x,y : x+y
print(a(5,6))
# > 11

##====================================================================================##

# Q19. Difference between iterables and iterators?
# Ans: iterable: An iterable is an object, which one can iterate over.
# In the case of iterable whole data is stored in the memory at a time.
# iterators: an iterator is an object used to iterate over an object.
# it is only being initialized or stored in the memory when it is called.
# iterators has next using which elements are fetched out from the object.
 ### List is an iterable
# lst = [1,2,3,4,5]
# for i in lst:
#     print(i)
 ### iterator
# lst1 = iter(lst)
 next(lst1)
# >1
 next(lst1)
# >2
 for i in lst1:
     print(i)
#>3,4,5

##====================================================================================##

# Q20. What is Map Function in python?
# Ans: a map function returns a map object after applying a certain function to each item of the iterable object.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  ## iterable object

def even_or_odd(num):  ## Function to check even and odd
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

list(map(even_or_odd,
         lst))  ## using map we are applying the function to each element of the ierable which will check whether the element is even or odd
-----------------------------------------
['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

##====================================================================================##

# Q21. How to reverse a list?
# Note how reverse() is called on the list and mutates it. It doesn’t return the mutated list itself.
li = ['a','b','c']
print(li)
li.reverse()
print(li)
#=> ['a', 'b', 'c']
#=> ['c', 'b', 'a']

##====================================================================================##

# Q22. How does string multiplication work?
# Let’s see the results of multiplying the string ‘cat’ by 3.
'cat' * 3
#=> 'catcatcat'

##====================================================================================##

# Q23. How does list multiplication work?
# Let’s see the result of multiplying a list, [1,2,3] by 2.
[1,2,3] * 2
#=> [1, 2, 3, 1, 2, 3]

##====================================================================================##

# Q24. How can you concatenate lists in python?
# Adding 2 lists together concatenates them. Note that arrays do not function the same way.
a = [1,2]
b = [3,4,5]
a + b
#=> [1, 2, 3, 4, 5]

##====================================================================================##

# Q25. What is the difference between lists and arrays?
# Note: Python’s standard library has an array object but here I’m specifically referring to the commonly used Numpy array.
# Lists exist in python’s standard library. Arrays are defined by Numpy.
# Lists can be populated with different types of data at each index. Arrays require homogeneous elements.
# Arithmetic on lists adds or removes elements from the list. Arithmetic on arrays functions per linear algebra.
# Arrays also use less memory and come with significantly more functionality.

##====================================================================================##

# Q26. Name mutable and immutable objects
# Immutable means the state cannot be modified after creation. Examples are: int, float, bool, string and tuple.
# Mutable means the state can be modified after creation. Examples are list, dict and set

##====================================================================================##

# Q27. How do you slice a list?
# Slicing notation takes 3 arguments, list[start:stop:step], where step is the interval at which elements are returned.
a = [0,1,2,3,4,5,6,7,8,9]
print(a[:2])
#=> [0, 1]
print(a[8:])
#=> [8, 9]
print(a[2:8])
#=> [2, 3, 4, 5, 6, 7]
print(a[2:8:2])
#=> [2, 4, 6]

##====================================================================================##

# Q28. What is the difference between dictionaries and JSON?
# Dict is python datatype, a collection of indexed but unordered keys and values.
# JSON is just a string which follows a specified format and is intended for transferring data.

##====================================================================================##

# Q29. Are dictionaries or lists faster for lookups?
# Looking up a value in a list takes O(n) time because the whole list needs to be iterated through until the value is found.
# Looking up a key in a dictionary takes O(1) time because it’s a hash table.
# This can make a huge time difference if there are a lot of values so dictionaries are generally recommended for speed. But they do have other limitations like needing unique keys.

##====================================================================================##

# Q30. How to increment and decrement an integer in Python?
# Increments and decrements can be done with +- and -= .

value = 5
value += 1
print(value)
#=> 6
value -= 1
value -= 1
print(value)
#=> 4

##====================================================================================##

# Q31. How to remove duplicate elements from a list?
# This can be done by converting the list to a set then back to a list.

a = [1,1,1,2,3]
a = list(set(a))
print(a)
#=> [1, 2, 3]

##====================================================================================##

# Q32. How to check if a value exists in a list?
# Use in.

# 'a' in ['a','b','c']
# #=> True
# 'a' in [1,2,3]
# #=> False
##====================================================================================##

# Q33. What is the difference between append and extend?
# append adds a value to a list while extend adds values in another list to a list.
a = [1,2,3]
b = [1,2,3]
a.append(6)
print(a)
#=> [1, 2, 3, 6]
b.extend([4,5])
print(b)
#=> [1, 2, 3, 4, 5]

##====================================================================================##

# Q34. How to combine two lists into a list of tuples?
# You can use the zip function to combine lists into a list of tuples. This isn’t
# restricted to only using 2 lists. It can also be done with 3 or more.
a = ['a', 'b', 'c']
b = [1, 2, 3]
[(k, v) for k, v in zip(a, b)]
# => [('a', 1), ('b', 2), ('c', 3)]

##====================================================================================##

# Q35. How can you sort a dictionary by key, alphabetically?
# You can’t “sort” a dictionary because dictionaries don’t have order but you can return a
# sorted list of tuples which has the keys and values that are in the dictionary.


d = {'c':3, 'd':4, 'b':2, 'a':1}
sorted(d.items())
#=> [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

##====================================================================================##

# Q36. How does a class inherit from another class in Python?
# In the below example, Audi, inherits from Car. And with that inheritance comes the instance methods of the parent class.

class Car():
    def drive(self):
        print('vroom')
class Audi(Car):
    pass
audi = Audi()
audi.drive()

##====================================================================================##

# Q37. How can you remove all whitespace from a string?
# The easiest way is to split the string on whitespace and then rejoin without spaces.
s = 'A string with     white space'
''.join(s.split())
#=> 'Astringwithwhitespace'

##====================================================================================##

# Q38. Why would you use enumerate() when iterating on a sequence?
# enumerate() allows tracking index when iterating over a sequence. It’s more pythonic than defining and incrementing an integer representing the index.
li = ['a','b','c','d','e']
for idx,val in enumerate(li):
    print(idx, val)
#=> 0 a
#=> 1 b
#=> 2 c
#=> 3 d
#=> 4 e

##====================================================================================##

#Q39.Convertthefollowingfor loop into a list comprehension.
#Thisfor loop.
a = [1, 2, 3, 4, 5]

a2 = []
for i in a:
    a2.append(i + 1)
print(a2)
# => [2, 3, 4, 5, 6]
#Becomes.
a3 = [i + 1 for i in a]
print(a3)
# => [2, 3, 4, 5, 6]
#Listcomprehension is generallyaccepted as morepythonicwhereit’sstill readable.

##====================================================================================##


# Q40. What is the zip function used for in python?
# Ans: The zip function takes iterables, aggregates them in a tuple, and returns it. The syntax of the zip() function is zip(*iterables)

numbers = [1, 2, 3]
string = ['one', 'two', 'three']
result = zip(numbers,string)
print(set(result))
-------------------------------------
{(3, 'three'), (2, 'two'), (1, 'one')}


##====================================================================================##

# Q41. Return a list of keys from a dictionary.
# This can be done by passing the dictionary to python’s list() constructor, list().
d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
list(d)
#=> ['id', 'name', 'color', 'speed']

##====================================================================================##

# Q42. How do you upper and lowercase a string?
# You can use the upper() and lower() string methods.
 small_word = 'potatocake'
big_word = 'FISHCAKE'
small_word.upper()
#=> 'POTATOCAKE'
big_word.lower()
#=> 'fishcake'

##====================================================================================##

#Q43. Write a one-liner in python to fetch out all the even and odd numbers from a given list?
a = [1,2,3,4,5,6,7,8,9,10]
odd, even = [el for el in a if el % 2==1], [el for el in a if el % 2==0]
print(odd,even)
> ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])


# Q44.What is the Difference Between a Method and a Function?
# Both essentially do the same thing but calling one either depends on the context.
# A method is associated with an object/class.
# A function is not associated with an object/class.
# Example of a function:
def greet(name):
    print("Hello, {}".format(name))
Example of the same as a method:
class Person:
    def greet(self, name):
        print("Hello, {}".format(name))
#In the above, both greet() method and the greet() function does the same thing.
# The only difference is that the method is tied to a class whereas the function is independent of the context.

# Q45.What are Comprehensions in Python?
# Comprehensions are shorthands for writing a for loop in Python. Python supports four different comprehensions:
# List comprehensions
# Dictionary comprehensions
# Set comprehensions
# Generator comprehensions
# For example, a list comprehension follows this syntax:
# newlist = [expression for item in iterable if condition == True]
# The other types of comprehensions look similar.

# Q46. What are the rules for local and global variables in Python?
#
# Here are the rules for local and global variables in Python:
#
# Local variables: If a variable is assigned a new value anywhere within the function's body, it's assumed to be local.
#
# Global variables: Those variables that are only referenced inside a function are implicitly global.

# Q47. What is a dictionary in Python?
# Python dictionary is one of the supported data types in Python. It is an unordered collection of elements. The elements in dictionaries are stored as key–value pairs. Dictionaries are indexed by keys.
#
# For example, below we have a dictionary named ‘dict’. It contains two keys, Country and Capital, along with their corresponding values, India and New Delhi.
#
# Syntax:
#
# dict={‘Country’:’India’,’Capital’:’New Delhi’, }
# Output: Country: India, Capital: New Delhi


# Q48. What are functions in Python?
# A function is a block of code which is executed only when a call is made to the function.
# def keyword is used to define a particular function as shown below:
#
# def function():
# print("Hi, Welcome to Intellipaat")
# function(); # call to the function
# Output:
# Hi, Welcome to Intellipaat

# Q49. What is __init__ in Python?
# Equivalent to constructors in OOP terminology, __init__ is a reserved method in Python classes.
# The __init__ method is called automatically whenever a new object is initiated. This method allocates
# memory to the new object as soon as it is created. This method can also be used to initialize variables.
#
# Syntax
#
# (for defining the __init__ method):
# class Human:
# # init method or constructor
# def __init__(self, age):
# self.age = age
# # Sample Method
# def say(self):
# print('Hello, my age is', self.age)
# h= Human(22)
# h.say()

# Q50. Is indentation required in Python?
# Indentation in Python is compulsory and is part of its syntax.
#
# All programming languages have some way of defining the scope and extent of the block of codes. In Python, it is indentation.
# Indentation provides better readability to the code, which is probably why Python has made it compulsory.


# Q51. Is Python fully object oriented?
# Python does follow an object-oriented programming paradigm and has all the basic OOPs concepts such as inheritance,
# polymorphism, and more, with the exception of access specifiers. Python doesn’t support strong encapsulation
# (adding a private keyword before data members).
# Although, it has a convention that can be used for data hiding, i.e., prefixing a data member with two underscores.