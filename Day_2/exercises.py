
#1- Remove 20 from the list below.
sampleList = [10, 20, 30, 40, 50]
print(del sampleList[1])
print( sampleList.remove(20)
#2-merge the list below.
listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']

merge_list=[listOne,listTwo]
merge_list=listOne+listTwo

#3- create a nested list from the lists below
listOne  =  ['a', 'b', 'c', 'd']
listTwo =  ['e', 'f', 'g']
merge_list=[listOne,listTwo]

#4-input list >>aList = [4, 8, 12, 16, 50, 70].Conver alist to  [4, 20, 24, 28, 50, 25]
alist[1:4]=[20,24,28]
alist[5]=25

#5- Add 60 to the list below
sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
#6- Multiply all items with 2 in the list below:

aList = [1, 2, 3, 4, 5, 6, 7]
bList=[]
for x in aList:
    y=x*2
    bList.append(y)
bList=[x*2 for x in aList]

#7- Get only last 3 items from the list below:
aList = [10, 20, 30, 40, 50, 60, 70, 80]
aList[-3:-1]

#8- Print second item in the list below
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#10-Change the value from "apple" to "kiwi", in the fruits list
fruits = ["apple", "banana", "cherry"]
fruits["apple"]="kiwi"

#11-Use the insert method to add "lemon" as the second item in the fruits list
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#12-Use a range of indexes to print the third, fourth, and fifth item in the list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits[3:6]
#13-Divide 10 by 2, and print the result
10/2 > 5.0 (float)
10//2 > 5 integer
#14-Use the correct membership operator to check if "apple" is present in the fruits object.
fruits = ["apple", "banana"]
print("apple" in fruits)

#15. reverse  "Hello world"
atext="Hello world"
print(atext[::-1])

num="123456"
print(num[::-1])