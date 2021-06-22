### PYTHON DATA TYPES: String###

"""Strings.
Besides numbers, Python can also manipulate strings, which can be
expressed in several ways. They can be enclosed in single quotes ('...')
or double quotes ("...") with the same result.
"""
# String with double quotes.
name_1="John"
name_2='John'

# \ can be used to escape quotes.
# use \' to escape the single quote or use double quotes instead.

a_string="doesnt"
print(a_string)

a_string='doesn\'t'
print(a_string)

# \n means newline.
b_string="Hello World.\n Today is beautiful"
print(b_string)

# Strings can be indexed, with the first character having index 0.
# There is no separate character type; a character is simply a string
# of size one. Note that since -0 is the same as 0, negative indices

word="Python"
print(word[0])
print(word[3])
print(word[4])
print(word[-4])

# In addition to indexing, slicing is also supported. While indexing is
# used to obtain individual characters, slicing allows you to obtain

print(word[1:4])

print(word[-3:-1])

# Note how the start is always included, and the end always excluded.
# This makes sure that s[:i] + s[i:] is always equal to s:

a_var="Hello"
b_var="World"
ab_var=a_var+" "+b_var
print(ab_var)

ab_var=a_var[1:3]+" "+b_var[-3:-1]
print(ab_var)

# Python strings cannot be changed — they are immutable. Therefore,
# assigning to an indexed position in the string
# results in an error:

a_var[3]="x"
print(a_string)

# The built-in function len() returns the length of a string:
characters = 'supercalifragilisticexpialidocious3456'
print(len(characters))

"""Basic operations

Strings can be concatenated (glued together) with the + operator,
and repeated with *: 3 times 'un', followed by 'ium'
"""

word="Python"
print(word*2)

a_string=" Hello world.Today is beautiful. "

# The strip() method removes any whitespace from the beginning or the end.
print(a_string.strip())

# The lower() method returns the string in lower case.
print(a_string.lower())

# The upper() method returns the string in upper case.
print(a_string.upper())

# The replace() method replaces a string with another string.

print(a_string.replace("Today", "Tomorrow"))

# The split() method splits the string into substrings if it finds instances of the separator.
list_string=a_string.split()
print(list_string)
print(type(list_string))

a_string=" Hello world.Today is beautiful."
list_string=a_string.split(".")
print(list_string)
print(type(list_string))

list_string=a_string.split(".",1)[0]
print(list_string)
print(type(list_string))

# Converts the first character to upper case
print(a_string.capitalize())


# Returns the number of times a specified value occurs in a string.
print(a_string.count("a"))

# Converts the first character of each word to upper case
print(a_string.title())

for i in a_string:
    print(i)

a_list=[x for x in a_string ]
print(a_list)

a_list=[]
for x in a_string:
    a_list.append(x)
print(a_list)

for i in "123":
    print(i)