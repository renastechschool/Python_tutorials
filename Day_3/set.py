"""Sets.

A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.

Set objects also support mathematical operations like union, intersection, difference, and
symmetric difference.
"""

"""Sets"""

fruits={"apple","banana","cherry"}
print(type(fruits))

# It is also possible to use the set() constructor to make a set.
# Note the double round-brackets
a_set=set((1,2,3,4))
print(a_set)

b_set=set(("Hello world"))
print(b_set)

# You may check if the item is in set by using "in" statement
print("apple" in fruits)
print("banana" not in fruits)
# Use the len() method to return the number of items.
print(len(fruits))

# You can use the add() object method to add an item.
fruits.add("pineapple")
print(fruits)
# you can join two set by using update
fruits.update({"grapes",7})
print(fruits)

numbers={2,5,6}



# Use remove() method to remove an item.

fruits.remove("grapes")
print(fruits)

# Use pop() remove  a random item from a set
fruits2={"apple","banana","cherry"}
print(fruits2.pop())


# Demonstrate set operations on unique letters from two word:
set1=set(("Java is great"))
set2=set(("Python is also great"))
print(set1)
print(set2)

# Letters in first word but not in second.
set_1_2_diff=set1.difference(set2)
print(set_1_2_diff)

set_1_2_diff=set1-set2
print(set_1_2_diff)

# Letters in first word or second word or both.
set_1_2_union=set1.union(set2)
print(set_1_2_union)
set_1_2_union=set1 | set2
print(set_1_2_union)

# Common letters in both words.
set_1_2_intersect=set1.intersection(set2)
print(set_1_2_intersect)

set_1_2_intersect=set1 & set2
print(set_1_2_intersect)

for i in set1:
    print(i)