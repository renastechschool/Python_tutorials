"""Dictionaries.

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are
written with curly brackets, and they have keys and values.

Dictionaries are sometimes found in other languages as “associative memories” or “associative
arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by
keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used
as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object
either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since
lists can be modified in place using index assignments, slice assignments, or methods like append()
and extend().

It is best to think of a dictionary as a set of key: value pairs, with the requirement that the
keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}.
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs
to the dictionary; this is also the way dictionaries are written on output.
"""
# Create a dictionary

# create a dictionary using {}
a_dict={"name":"Jessica","country":"USA","age":30}
print(a_dict)
# create a dictionary using dict()
a_dict=dict({"name":"Jessica","country":"USA","age":30})
print(a_dict)

# create a dictionary from sequence having each item as a pair
a_dict=dict([("name","Jessica"),("country","USA"),("age",30)])
print(a_dict)

#a dict
fruits={"cherry":"red","apple":"green","banana":"yellow"}

# You may access set elements by keys.
print(fruits["apple"])
print(fruits["banana"])

# You may access set elements by keys.
print(fruits.get("banana"))

# To check whether a single key is in the dictionary, use the in keyword.
print("apple" in fruits)
print("pineapple" not in fruits)

# Change the apple color to "red".
fruits["apple"]="red"
print(fruits)

# Add new key/value pair to the dictionary

fruits["apple2"]="red_green"
print(fruits)
# Add new key/value pair to the dictionary with update()
fruits_2={"orange":"orange","watermelon":"dark green"}

fruits.update(fruits_2)
print(fruits)


# Get keys from a dict
print(fruits.keys())

# # Get values from a dict
print(fruits.values())

# Get all key-value pair

print(fruits.items())

# you can get lenght of a dict with len() function
print(len(fruits))

# It is also possible to delete a key:value pair with del.
del fruits["apple2"]
fruits.pop("apple")
print(fruits)

# You can remove all items in a dict with clear() method
fruits.clear()

#We can iterate through a dictionary using a for-loop and
# access the individual keys and their corresponding values.
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
for i in person.keys():
    print(i)

for i in person.values():
    print(i)

for i , k in person.items():
    print(i, "==", k)

b_dict={x:x*2 for x in ("hello","world")}
print(b_dict)
