##Exercise 1: Given a list, iterate it, and display numbers divisible by five,
## and if you find a number greater than 150, stop the loop iteration.

##Exercise 2:Given a number count the total number of digits in a number
#For example, the number is 75869, so the output should be 5


#Exercise 3: Reverse the following list using for loop
#list1 = [10, 20, 30, 40, 50]

##Exercise 4: Display numbers from -10 to -1 using for loop > -10,-9,.......,-1

##Exercise 5: Reverse 459871 integer number >- 178945

##Exercise 6: Use a loop to display elements from a given list that are present at even index positions
# given:my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#expected :20 40 60 80 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
new_list=[]
for index, i in enumerate(my_list ):
    print(index, i)
    if index % 2==0:
         new_list.append(i)
print(new_list)

new_list=[]
for i in range(0, len(my_list)-1,2):
    new_list.append(my_list[i])


#Exercise 7: Display the cube of the number up to a given integer
# given:input_number = 6
#expected:
# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216

#Exercise 8: Display a message “Done” after successful execution of for loop
#expected:
# 0
# 1
# 2
# 3
# 4
# Done!
